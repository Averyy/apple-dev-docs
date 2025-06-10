# HKStatistics

**Framework**: HealthKit  
**Kind**: class

An object that represents the result of calculating the minimum, maximum, average, or sum over a set of samples from the HealthKit store.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class HKStatistics
```

#### Overview

HealthKit creates statistic objects using either a statistics query or a statistics collection query. For the statistics query, it performs the specified calculations over all the samples that match the query. For the statistics collection query, it partitions the matching samples into a set of time intervals and performs the calculations over each interval separately.

By default, these queries automatically merge the data from all of your data sources before performing the calculations. If you want to merge the data yourself, you can set the [`separateBySource`](hkstatisticsoptions/separatebysource.md) option. You can then request the statistical data for each source separately.

When requesting data from a statistics object, your request must match the options you used when creating the query. For example, if you create a query using the [`discreteAverage`](hkstatisticsoptions/discreteaverage.md) option, you must access the results using the [`averageQuantity()`](hkstatistics/averagequantity().md) method.

For more information on calculating statistical data, see [`HKStatisticsQuery`](hkstatisticsquery.md) Class Reference. To calculate the statistics over a series of time intervals, see the [`HKStatisticsCollectionQuery`](hkstatisticscollectionquery.md) Class Reference.

## Topics

### Getting Property Data
- [var startDate: Date](hkstatistics/startdate.md)
  The start of the time period included in these statistics.
- [var endDate: Date](hkstatistics/enddate.md)
  The end of the time period included in these statistics.
- [var quantityType: HKQuantityType](hkstatistics/quantitytype.md)
  The quantity type of the samples used to calculate these statistics.
- [var sources: [HKSource]?](hkstatistics/sources.md)
  An array containing all the sources contributing to these statistics.
### Getting Statistics Data
- [func averageQuantity() -> HKQuantity?](hkstatistics/averagequantity.md)
  Returns the average value from all the samples that match the query.
- [func averageQuantity(for: HKSource) -> HKQuantity?](hkstatistics/averagequantity(for:).md)
  Returns the average value from all the samples that match the query and that were created by the specified source.
- [func maximumQuantity() -> HKQuantity?](hkstatistics/maximumquantity.md)
  Returns the maximum value from all the samples that match the query.
- [func maximumQuantity(for: HKSource) -> HKQuantity?](hkstatistics/maximumquantity(for:).md)
  Returns the maximum value from all the samples that match the query and that were created by the specified source.
- [func minimumQuantity() -> HKQuantity?](hkstatistics/minimumquantity.md)
  Returns the minimum value from all the samples that match the query.
- [func minimumQuantity(for: HKSource) -> HKQuantity?](hkstatistics/minimumquantity(for:).md)
  Returns the minimum value from all the samples that match the query and that were created by the specified source.
- [func sumQuantity() -> HKQuantity?](hkstatistics/sumquantity.md)
  Returns the sum of all the samples that match the query.
- [func sumQuantity(for: HKSource) -> HKQuantity?](hkstatistics/sumquantity(for:).md)
  Returns the sum of all the samples that match the query and that were created by the specified source.
- [func duration() -> HKQuantity?](hkstatistics/duration.md)
  Returns the total duration covering all the samples that match the query.
- [func duration(for: HKSource) -> HKQuantity?](hkstatistics/duration(for:).md)
  Returns the total duration covering all the samples created by the specified source that also match the query.
### Getting the Most Recent Quantity
- [func mostRecentQuantity() -> HKQuantity?](hkstatistics/mostrecentquantity.md)
  Returns the most recent value from all the samples that match the query.
- [func mostRecentQuantity(for: HKSource) -> HKQuantity?](hkstatistics/mostrecentquantity(for:).md)
  Returns the most recent value from all the samples that match the query and were created by the specified source.
- [func mostRecentQuantityDateInterval() -> DateInterval?](hkstatistics/mostrecentquantitydateinterval.md)
  Returns the date interval of the most recent sample that matches the query.
- [func mostRecentQuantityDateInterval(for: HKSource) -> DateInterval?](hkstatistics/mostrecentquantitydateinterval(for:).md)
  Returns the date interval of the most recent sample that matches the query and was created by the specified source.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

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
- [class HKStatisticsCollectionQuery](hkstatisticscollectionquery.md)
  A query that performs multiple statistics queries over a series of fixed-length time intervals.
- [class HKStatisticsCollection](hkstatisticscollection.md)
  An object that manages a collection of statistics, representing the results calculated over separate time intervals.
- [struct HKStatisticsOptions](hkstatisticsoptions.md)
  Options for specifying the statistic to calculate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkstatistics)*