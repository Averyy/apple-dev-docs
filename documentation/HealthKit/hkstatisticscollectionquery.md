# HKStatisticsCollectionQuery

**Framework**: HealthKit  
**Kind**: class

A query that performs multiple statistics queries over a series of fixed-length time intervals.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
class HKStatisticsCollectionQuery
```

## Mentions

- [Executing Statistics Collection Queries](executing-statistics-collection-queries.md)
- [Accessing condensed workout samples](accessing-condensed-workout-samples.md)

#### Overview

Statistics collection queries are often used to produce data for graphs and charts. For example, you might create a statistics collection query that calculates the total number of steps for each day or the average heart rate for each hour. Like observer queries, collection queries can also act as long-running queries, receiving updates when the HealthKit store’s content changes.

> ❗ **Important**:  You can only use statistics collection queries with quantity samples. If you want to calculate statistics over workouts or correlation samples, you must perform the appropriate query and process the data yourself.

 You can only use statistics collection queries with quantity samples. If you want to calculate statistics over workouts or correlation samples, you must perform the appropriate query and process the data yourself.

Statistics collection queries are mostly immutable. You can assign the query’s [`initialResultsHandler`](hkstatisticscollectionquery/initialresultshandler.md) and [`statisticsUpdateHandler`](hkstatisticscollectionquery/statisticsupdatehandler.md) properties after instantiating the object. You must set all other properties when you instantiate the object, and they can’t change.

For more information about statistics queries, see [`HKStatisticsQuery`](hkstatisticsquery.md).

## Topics

### Creating Statistics Collection Objects
- [Executing Statistics Collection Queries](executing-statistics-collection-queries.md)
  Calculate statistical data for graphs and charts.
- [init(quantityType: HKQuantityType, quantitySamplePredicate: NSPredicate?, options: HKStatisticsOptions, anchorDate: Date, intervalComponents: DateComponents)](hkstatisticscollectionquery/init(quantitytype:quantitysamplepredicate:options:anchordate:intervalcomponents:).md)
  Initializes a statistics collection query to perform the specified calculations over a set of time intervals.
### Getting and Setting Results Handlers
- [var initialResultsHandler: ((HKStatisticsCollectionQuery, HKStatisticsCollection?, (any Error)?) -> Void)?](hkstatisticscollectionquery/initialresultshandler.md)
  The results handler for the query’s initial results.
- [var statisticsUpdateHandler: ((HKStatisticsCollectionQuery, HKStatistics?, HKStatisticsCollection?, (any Error)?) -> Void)?](hkstatisticscollectionquery/statisticsupdatehandler.md)
  The results handler for monitoring updates to the HealthKit store.
### Getting Property Data
- [var anchorDate: Date](hkstatisticscollectionquery/anchordate.md)
  The anchor date for the collection’s time intervals.
- [var intervalComponents: DateComponents](hkstatisticscollectionquery/intervalcomponents.md)
  The date components that define the time interval for each statistics object in the collection.
- [var options: HKStatisticsOptions](hkstatisticscollectionquery/options.md)
  A list of options that define the type of statistical calculations performed and the way in which data from multiple sources are merged.

## Relationships

### Inherits From
- [HKQuery](hkquery.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [Executing Statistical Queries](executing-statistical-queries.md)
  Create and run statistical queries.
- [Executing Statistics Collection Queries](executing-statistics-collection-queries.md)
  Calculate statistical data for graphs and charts.
- [struct HKStatisticsQueryDescriptor](hkstatisticsquerydescriptor.md)
  A query descriptor that calculates the minimum, maximum, average, or sum over a set of samples from the HealthKit store.
- [class HKStatisticsQuery](hkstatisticsquery.md)
  A query that performs statistical calculations over a set of matching quantity samples, and returns the results.
- [struct HKStatisticsCollectionQueryDescriptor](hkstatisticscollectionquerydescriptor.md)
  A query descriptor that gathers a collection of statistics calculated over a series of fixed-length time intervals.
- [class HKStatistics](hkstatistics.md)
  An object that represents the result of calculating the minimum, maximum, average, or sum over a set of samples from the HealthKit store.
- [class HKStatisticsCollection](hkstatisticscollection.md)
  An object that manages a collection of statistics, representing the results calculated over separate time intervals.
- [struct HKStatisticsOptions](hkstatisticsoptions.md)
  Options for specifying the statistic to calculate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkstatisticscollectionquery)*