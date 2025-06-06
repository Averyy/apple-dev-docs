# HKStatisticsQueryDescriptor

**Framework**: HealthKit  
**Kind**: struct

A query descriptor that calculates the minimum, maximum, average, or sum over a set of samples from the HealthKit store.

**Availability**:
- iOS 15.4+
- iPadOS 15.4+
- Mac Catalyst 15.4+
- macOS 13.0+
- visionOS ?+
- watchOS 8.5+

## Declaration

```swift
struct HKStatisticsQueryDescriptor
```

## Mentions

- [Reading data from HealthKit](reading-data-from-healthkit.md)

#### Overview

Use the [`HKStatisticsQueryDescriptor`](hkstatisticsquerydescriptor.md) to perform calculations over sets of samples currently saved in the HealthKit store.

```swift
// Create a predicate for today's samples.
let calendar = Calendar(identifier: .gregorian)
let startDate = calendar.startOfDay(for: Date())
let endDate = calendar.date(byAdding: .day, value: 1, to: startDate)
let today = HKQuery.predicateForSamples(withStart: startDate, end: endDate)

// Create the query descriptor.
let stepType = HKQuantityType(.stepCount)
let stepsToday = HKSamplePredicate.quantitySample(type: stepType, predicate:today)
let sumOfStepsQuery = HKStatisticsQueryDescriptor(predicate: stepsToday, options: .cumulativeSum)

// Run the query.
let stepCount = try await sumOfStepsQuery.result(for: store)?
    .sumQuantity()?
    .doubleValue(for: HKUnit.count())

// Use the step count here.
```

## Topics

### Creating Query Descriptors
- [init(predicate: HKSamplePredicate<HKQuantitySample>, options: HKStatisticsOptions)](hkstatisticsquerydescriptor/init(predicate:options:).md)
  Creates a statistics query descriptor.
### Running Queries
- [func result(for: HKHealthStore) async throws -> HKStatistics?](hkstatisticsquerydescriptor/result(for:).md)
  Runs a one-shot query and asynchronously returns a snapshot of the current matching results.
### Accessing Query Properties
- [var predicate: HKSamplePredicate<HKQuantitySample>](hkstatisticsquerydescriptor/predicate.md)
  A predicate that defines the set of data that the query uses to calculate the statistics.
- [var options: HKStatisticsOptions](hkstatisticsquerydescriptor/options.md)
  A list of options that define the type of statistical calculations performed and the way in which HealthKit merges data from multiple sources.
### Default Implementations
- [HKAsyncQuery Implementations](hkstatisticsquerydescriptor/hkasyncquery-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [HKAsyncQuery](hkasyncquery.md)

## See Also

- [Executing Statistical Queries](executing-statistical-queries.md)
  Create and run statistical queries.
- [Executing Statistics Collection Queries](executing-statistics-collection-queries.md)
  Calculate statistical data for graphs and charts.
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

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkstatisticsquerydescriptor)*