# Executing Statistics Collection Queries

**Framework**: HealthKit

Calculate statistical data for graphs and charts.

#### Overview

Produce data for graphs and charts using statistics collection queries. For example, you might create a statistics collection query that calculates the total number of steps for each day or the average heart rate for each hour.

> **Note**:  HealthKit provides two types of queries for calculating statistics over sets of samples. [`HKStatisticsQuery`](hkstatisticsquery.md) calculates a single value over all matching samples, while [`HKStatisticsCollectionQuery`](hkstatisticscollectionquery.md) partitions the samples into time intervals and calculates a value for each time interval.

 HealthKit provides two types of queries for calculating statistics over sets of samples. [`HKStatisticsQuery`](hkstatisticsquery.md) calculates a single value over all matching samples, while [`HKStatisticsCollectionQuery`](hkstatisticscollectionquery.md) partitions the samples into time intervals and calculates a value for each time interval.

Statistics collection queries use an anchor point and a time interval to partition the set of matching samples into collections. The anchor point defines an arbitrary starting point. The position of this point often doesn’t matter. It could be in the future or in the past. Time intervals extend away from this anchor point in both directions.

![An illustration showing a value for each time interval around the specified anchor.](https://docs-assets.developer.apple.com/published/42de5e4a5895738f2d09048853669681/media-3740870%402x.png)

For example, if you use a 1-day time interval, the anchor point defines the time when each collection begins. The exact date for the anchor point doesn’t matter. It could be 3:34 a.m., January 1, 1970 or 3:34 a.m., March 15, 2065. In both cases, the statistics collection query partitions the matching samples into days, starting each day at 3:34 a.m.

The statistics collection query then calculates common statistics over each time interval. You can use statistics queries to calculate the minimum, maximum, or average value of a set of discrete quantities, or to calculate the sum for cumulative quantities. Also, like observer queries, statistics collection queries can act as long-running queries, receiving updates when the HealthKit store’s content changes.

##### Create the Query

Start by creating your anchor date and time interval. The following sample starts by creating a 1-week time interval. Next, it sets the anchor date to Monday morning at 3:00 a.m. Because the interval is 1 week long, the anchor’s exact date doesn’t matter. Each set of statistics represents exactly 1 week, starting on Monday at 3:00 a.m.

```swift
let calendar = Calendar.current

// Create a 1-week interval.
let interval = DateComponents(day: 7)

// Set the anchor for 3 a.m. on Monday.
var components = DateComponents(calendar: calendar,
                                timeZone: calendar.timeZone,
                                hour: 3,
                                minute: 0,
                                second: 0,
                                weekday: 2)

guard let anchorDate = calendar.nextDate(after: Date(),
                                         matching: components,
                                         matchingPolicy: .nextTime,
                                         repeatedTimePolicy: .first,
                                         direction: .backward) else {
    fatalError("*** unable to find the previous Monday. ***")
}
```

Next, create the quantity type and the statistics collection query. The following code creates the quantity type for step counts and then creates the query itself.

```swift
guard let quantityType = HKObjectType.quantityType(forIdentifier: .stepCount) else {
    fatalError("*** Unable to create a step count type ***")
}

// Create the query.
let query = HKStatisticsCollectionQuery(quantityType: quantityType,
                                        quantitySamplePredicate: nil,
                                        options: .cumulativeSum,
                                        anchorDate: anchorDate,
                                        intervalComponents: interval)
```

##### Add Callback Handlers

Unlike most other queries, you don’t set the callback block when you instantiate a statistics collection query. Instead, you can either set the initial result handler or the statistics update handler (or both) as needed for your app. In this case, the sample code just sets the initial results handler, letting it calculate statistics over the samples currently stored in HealthKit.

In your results handler, first check for and handle errors. Many [`HKError.Code`](hkerror/code.md) values indicate that you haven’t properly set up HealthKit. Always check HealthKit’s availability and request permission to read the specified data type before creating a query. For more information, see [`Setting up HealthKit`](setting-up-healthkit.md) and [`Authorizing access to health data`](authorizing-access-to-health-data.md).

However, your app may need to explicitly check for some errors, depending on its needs. For example, if your app can run a query in the background, you need to check for and handle the [`HKError.Code.errorDatabaseInaccessible`](hkerror/code/errordatabaseinaccessible.md) error.

```swift
// Set the results handler.
query.initialResultsHandler = {
    query, results, error in
    
    // Handle errors here.
    if let error = error as? HKError {
        switch (error.code) {
        case .errorDatabaseInaccessible:
            // HealthKit couldn't access the database because the device is locked.
            return
        default:
            // Handle other HealthKit errors here.
            return
        }
    }
    
    guard let statsCollection = results else {
        // You should only hit this case if you have an unhandled error. Check for bugs 
        // in your code that creates the query, or explicitly handle the error.
        assertionFailure("")
        return
    }

...
```

After you handle any errors, process the incoming statistics data, and then update your app. Be sure to dispatch code that updates the user interface to the [`main`](https://developer.apple.com/documentation/Dispatch/DispatchQueue/main) queue.

The following code calculates the start and end times for a 3-month window and then iterates over all the time intervals in that window. The statistics collection passes the enumeration block a statistics object for each time interval between the start and end dates. However, if the time interval doesn’t contain any samples, the provided statistics’s [`sumQuantity()`](hkstatistics/sumquantity().md) method returns `nil`. Therefore, the sample must check to see whether it has a valid quantity. If it does, it adds the data; otherwise, it skips the time interval.

```swift
...
    
    let endDate = Date()
    let threeMonthsAgo = DateComponents(month: -3)
    
    guard let startDate = calendar.date(byAdding: threeMonthsAgo, to: endDate) else {
        fatalError("*** Unable to calculate the start date ***")
    }
    
    // Plot the weekly step counts over the past 3 months.
    var weeklyData = MyWeeklyData()
    
    // Enumerate over all the statistics objects between the start and end dates.
    statsCollection.enumerateStatistics(from: startDate, to: endDate)
    { (statistics, stop) in
        if let quantity = statistics.sumQuantity() {
            let date = statistics.startDate
            let value = quantity.doubleValue(for: .count())
            
            // Extract each week's data.
            weeklyData.addWeek(date: date, stepCount: Int(value))
        }
    }
    
    // Dispatch to the main queue to update the UI.
    DispatchQueue.main.async {
        myUpdateGraph(weeklyData: weeklyData)
    }
}
```

Finally, execute the query using the HealthKit store.

```swift
healthStore.execute(query)
```

Since the sample doesn’t provide an update results handler, when the initial results block finishes processing the data, the query stops automatically. If the sample had provided an update manager, the statistics collection query would continue to monitor the HealthKit store after it had generated the initial results.

## See Also

- [Executing Statistical Queries](executing-statistical-queries.md)
  Create and run statistical queries.
- [struct HKStatisticsQueryDescriptor](hkstatisticsquerydescriptor.md)
  A query descriptor that calculates the minimum, maximum, average, or sum over a set of samples from the HealthKit store.
- [class HKStatisticsQuery](hkstatisticsquery.md)
  A query that performs statistical calculations over a set of matching quantity samples, and returns the results.
- [struct HKStatisticsCollectionQueryDescriptor](hkstatisticscollectionquerydescriptor.md)
  A query descriptor that gathers a collection of statistics calculated over a series of fixed-length time intervals.
- [class HKStatisticsCollectionQuery](hkstatisticscollectionquery.md)
  A query that performs multiple statistics queries over a series of fixed-length time intervals.
- [class HKStatistics](hkstatistics.md)
  An object that represents the result of calculating the minimum, maximum, average, or sum over a set of samples from the HealthKit store.
- [class HKStatisticsCollection](hkstatisticscollection.md)
  An object that manages a collection of statistics, representing the results calculated over separate time intervals.
- [struct HKStatisticsOptions](hkstatisticsoptions.md)
  Options for specifying the statistic to calculate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/executing-statistics-collection-queries)*