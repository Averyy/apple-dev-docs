# HKStatisticsOptions

**Framework**: HealthKit  
**Kind**: struct

Options for specifying the statistic to calculate.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
struct HKStatisticsOptions
```

#### Overview

You cannot combine a discrete option with a cumulative option. You can, however, combine multiple discrete options together to perform multiple calculations. You can also combine the [`separateBySource`](hkstatisticsoptions/separatebysource.md) option with any of the other options.

#### Swift

```swift
let cumulativeActiveEnergyBurned = HKQuantityType(.activeEnergyBurned)
 
let discreteHeartRate = HKQuantityType(.heartRate)
 
// Cannot combine cumulative options with discrete options.
// However, you can combine a cumulative option and separated by source
let cumulativeQuery = HKStatisticsQuery(quantityType:cumulativeActiveEnergyBurned,
                                        quantitySamplePredicate:nil,
                                        options: [.cumulativeSum, .separateBySource]) {
                                            query, statistics, error in
                                            
                                            // ... process the results here
}
 
// You can also combine any number of discrete options
// and the separated by source option.
let discreteQuery = HKStatisticsQuery(quantityType: discreteHeartRate,
                                      quantitySamplePredicate: nil,
                                      options: [.discreteAverage, .discreteMin, .discreteMax, .separateBySource]) {
                                            query, statistics, error in
                                            
                                            // ... process the results here
}
```

#### Objective C

```objc
HKQuantityType *cumulativeActiveEnergyBurned =
[HKObjectType quantityTypeForIdentifier:HKQuantityTypeIdentifierActiveEnergyBurned];
 
HKQuantityType *discreteHeartRate =
[HKObjectType quantityTypeForIdentifier:HKQuantityTypeIdentifierHeartRate];
 
// Cannot combine cumulative options with discrete options.
// However, you can combine a cumulative option and seperated by source
HKStatisticsQuery *cumulativeQuery =
[[HKStatisticsQuery alloc]
 initWithQuantityType:cumulativeActiveEnergyBurned
 quantitySamplePredicate:nil
 options:HKStatisticsOptionCumulativeSum | HKStatisticsOptionSeparateBySource
 completionHandler:^(HKStatisticsQuery *query, HKStatistics *result, NSError *error) {
 
      // ... process the results here
 }];
 
// You can also combine any number of discrete options
// and the seperated by source option.
HKStatisticsQuery *discreteQuery =
[[HKStatisticsQuery alloc]
 initWithQuantityType:discreteHeartRate
 quantitySamplePredicate:nil
 options:HKStatisticsOptionDiscreteAverage | HKStatisticsOptionDiscreteMin |
 HKStatisticsOptionDiscreteMax | HKStatisticsOptionSeparateBySource
 completionHandler:^(HKStatisticsQuery *query, HKStatistics *result, NSError *error) {
 
     // ... process the results here
 }];
```

## Topics

### Constants
- [static var separateBySource: HKStatisticsOptions](hkstatisticsoptions/separatebysource.md)
  An option indicating that the system calculates the specified statistics separately for each source.
- [static var discreteAverage: HKStatisticsOptions](hkstatisticsoptions/discreteaverage.md)
  An option indicating that the system calculates the average quantity for the samples.
- [static var discreteMin: HKStatisticsOptions](hkstatisticsoptions/discretemin.md)
  An option indicating that the system calculates the minimum quantity for the samples.
- [static var discreteMax: HKStatisticsOptions](hkstatisticsoptions/discretemax.md)
  An option indicating that the system calculates the maximum quantity for the samples.
- [static var cumulativeSum: HKStatisticsOptions](hkstatisticsoptions/cumulativesum.md)
  An option indicating that the system calculates the sum of all the quantities for the samples.
- [static var mostRecent: HKStatisticsOptions](hkstatisticsoptions/mostrecent.md)
  An option indicating that the system returns the most recent quantity from the matching samples.
- [static var duration: HKStatisticsOptions](hkstatisticsoptions/duration.md)
  An option indicating that the system calculates the total duration covering all the samples.
### Deprecated Constants
- [static var discreteMostRecent: HKStatisticsOptions](hkstatisticsoptions/discretemostrecent.md)
  An option indicating that the system returns the most recent quantity from the matching samples.
### Initializers
- [init(rawValue: UInt)](hkstatisticsoptions/init(rawvalue:).md)
  Returns a newly initialized statistics option using the provided integer.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

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
- [class HKStatistics](hkstatistics.md)
  An object that represents the result of calculating the minimum, maximum, average, or sum over a set of samples from the HealthKit store.
- [class HKStatisticsCollection](hkstatisticscollection.md)
  An object that manages a collection of statistics, representing the results calculated over separate time intervals.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkstatisticsoptions)*