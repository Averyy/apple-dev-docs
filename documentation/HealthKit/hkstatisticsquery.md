# HKStatisticsQuery

**Framework**: HealthKit  
**Kind**: class

A query that performs statistical calculations over a set of matching quantity samples, and returns the results.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
class HKStatisticsQuery
```

## Mentions

- [Accessing condensed workout samples](accessing-condensed-workout-samples.md)
- [Executing Statistics Collection Queries](executing-statistics-collection-queries.md)

#### Overview

Statistics queries calculate common statistics over the set of matching samples. You can use statistical queries to calculate the minimum, maximum, or average value of a set of discrete quantities, or use them to calculate the sum for cumulative quantities. For the complete list of possible calculations, see [`HKStatisticsOptions`](hkstatisticsoptions.md). For more information about the available quantity types and to learn whether they are discrete or cumulative values, see [`Data types`](data-types.md).

You can use statistics queries with quantity samples only. If you want to calculate statistics over workouts or correlation samples, you must perform the appropriate query and process the data yourself.

Statistics queries are immutable. Their properties are set when they are first created, and they can’t change.

## Topics

### Creating Statistics Queries
- [init(quantityType: HKQuantityType, quantitySamplePredicate: NSPredicate?, options: HKStatisticsOptions, completionHandler: (HKStatisticsQuery, HKStatistics?, (any Error)?) -> Void)](hkstatisticsquery/init(quantitytype:quantitysamplepredicate:options:completionhandler:).md)
  Initializes a statistics query instance that performs the specified calculations over the matching samples in the HeathKit store.
- [Executing Statistical Queries](executing-statistical-queries.md)
  Create and run statistical queries.

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
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [Executing Statistical Queries](executing-statistical-queries.md)
  Create and run statistical queries.
- [Executing Statistics Collection Queries](executing-statistics-collection-queries.md)
  Calculate statistical data for graphs and charts.
- [struct HKStatisticsQueryDescriptor](hkstatisticsquerydescriptor.md)
  A query descriptor that calculates the minimum, maximum, average, or sum over a set of samples from the HealthKit store.
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

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkstatisticsquery)*