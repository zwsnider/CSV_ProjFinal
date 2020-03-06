import matplotlib.pyplot as plt
import csv
from datetime import datetime
#
#
#
def main():
    open_file = open('death_valley_2018_simple.csv', "r")  ## DEATH VALLEY
    open_file2 = open("sitka_weather_2018_simple.csv", "r") ##SITKA

    DV_file = csv.reader(open_file, delimiter=",")  ## DEATH VALLEY
    SA_file = csv.reader(open_file2, delimiter=',')  ##SITKA

    dates_D, highs_D, lows_D, station_name_D = get_attributes(DV_file)   ###################################################

    dates_S, highs_S, lows_S, station_name_S = get_attributes(SA_file) ###################################################


    fig, (death, sitka) = plt.subplots(2)

    
    fig.subplots_adjust(hspace=0.5)

    # fig = plt.figure()
    death.set_title(station_name_D , fontsize =16) # automatic station name from second row of csv in "NAME" column
    
    death.plot(dates_D, highs_D, color='red', alpha= 0.8) 
    death.plot(dates_D, lows_D, color='blue', alpha = 0.8)

    sitka.plot(dates_S, highs_S, color='red', alpha= 0.8)
    sitka.plot(dates_S, lows_S, color='blue', alpha = 0.8)

    death.fill_between(dates_D, highs_D, lows_D, facecolor = "blue", alpha = 0.3) #give it an x-axis and two points in between to fill color
    sitka.fill_between(dates_S, highs_S, lows_S, facecolor = "blue", alpha = 0.3) 

    death.set_title(station_name_D , fontsize =16) # automatic station name from second row of csv in "NAME" column
    sitka.set_title(station_name_S , fontsize =16) # automatic station name from second row of csv in "NAME" column

    death.set_xlabel("", fontsize=8)
    sitka.set_xlabel("", fontsize=8)

    death.set_ylabel("Temperature in (F)",fontsize = 12)
    sitka.set_ylabel("Temperature in (F)",fontsize = 12)

    death.tick_params(axis="both", which="major" , labelsize= 12)
    sitka.tick_params(axis="both", which="major" , labelsize= 12)

    fig.autofmt_xdate() #makes dates fit diagonally

    title_text = "Temperature comparison between" , station_name_D, "and", station_name_S   ### had to do this because suptitle() only takes 2 arguments (and that was 5)
    title_text = str(title_text)
    new_title_text = convert(title_text)   ###### this uses the convert function I defined below
    fig.suptitle(new_title_text, fontsize = 15)  ### now use the variable that i just created
    ############################################## this could have been solved a lot better with: fig.suptitle=("Temperature comparison between
    ##################### fig.suptitle=("Temperature comparison between {station_name1} and {station_name2}.")
    plt.show() #dont forget this or the plot wont show
#
#
#
#
def get_attributes(csv_file):
    header_row = next(csv_file)
    first_row = next(csv_file)  ## this selects the first row after the header row. Will need this for the title later

    print(type(header_row))

    for index, column_header in enumerate(header_row):
        if column_header == "TMIN":
            TMIN_index = index
        if column_header == "TMAX":
            TMAX_index = index
        if column_header == "NAME":
            station_name_index = index

    station_name = first_row[station_name_index]  #3 This gets the station name for the title later

    highs = []
    lows = []
    dates = []

    for row in csv_file:
        try:
            high = int(row[TMAX_index])
            low = int(row[TMIN_index])
            current_date = datetime.strptime(row[2], "%Y-%m-%d") #fixes the dates into less amount of dates
        except ValueError:
            print(f"Missing data for {current_date}") # f --> format. Shows where there is a value error (aka missing data)
        else: # if the except statement is the case, then it omits that data and keeps on going with the for loop
            highs.append(high)     #only appends values from column 5 (TMAX)
            lows.append(low)
            dates.append(current_date)
    

    return dates, highs, lows, station_name

def convert(weird_list): 
    symbols = [",", "(" , ")", "'"]
    converted_into_list = [x for x in weird_list if x not in symbols]    ### this converts the object that we had from joining string with variables into a list of characters
    new = ""     ##### here we make a new list that's in string form
    for x in converted_into_list: 
        if x not in symbols:
            new += x      # put each letter in the string  
    # return string
    return new 






#print(highs[:10]) #shows everything up till 9 (not including 10)

main()


# Submit CSV project on GitHub. Name your Github repository accordingly. Submit just the URL for the repository through this assignment.

# Your CSV project should contain:

# 5 python scripts (4 worked in class and 1 on your own)
# 3 data files ( csv files)
# README file that is an overview of your project
# For your 5th python script file - 

# Automatic Indexes: We hard coded the indexes corresponding to the TMIN and TMAX 
# columns. Use the header row to determine the indexes for these values, so your program can work 
# for Sitka or Death Valley. Use the station name to automatically generate an appropriate title 
# for your graph as well.

# create 2 subplot graphs in one visualization so you can see both graphs to compare side by side.

# Matplotlib's pyplot API has a convenience function called subplots() which acts as a 
# utility wrapper and helps in creating common layouts of subplots, including the 
# enclosing figure object, in a single call.

# # fig, ax = plt.subplots(2,2)  -  this will create a visualization with 2 charts on it
