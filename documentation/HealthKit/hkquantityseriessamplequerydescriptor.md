# HKQuantitySeriesSampleQueryDescriptor

**Framework**: HealthKit  
**Kind**: struct

A query interface that reads the series data associated with quantity samples using Swift concurrency.

**Availability**:
- iOS 15.4+
- iPadOS 15.4+
- Mac Catalyst 15.4+
- macOS 13.0+
- visionOS ?+
- watchOS 8.5+

## Declaration

```swift
struct HKQuantitySeriesSampleQueryDescriptor
```

#### Overview

Use [`HKQuantitySeriesSampleQueryDescriptor`](hkquantityseriessamplequerydescriptor.md) to read the series data included in quantity samples. Apps can save any quantity data as a series using the [`HKQuantitySeriesSampleBuilder`](hkquantityseriessamplebuilder.md) class; however, series data typically comes from high-frequency data saved during a workout. Any [`HKQuantitySample`](hkquantitysample.md) that has a [`count`](hkquantitysample/count.md) greater than `1` contains series data.

> ❗ **Important**:  Only use this query when you need direct access to the high-frequency series data, for example when visualizing the raw data or when exporting objects from the HealthKit store. For most common calculations, consider using a statistical query instead. Statistical queries correctly handle quantity data, whether the samples represent a single quantity or a series.

 Only use this query when you need direct access to the high-frequency series data, for example when visualizing the raw data or when exporting objects from the HealthKit store. For most common calculations, consider using a statistical query instead. Statistical queries correctly handle quantity data, whether the samples represent a single quantity or a series.

To read the individual data entries, create a predicate that identifies the sample type and limits the results to the desired data. For example, to read the series for a particular sample object, include a [`predicateForObject(with:)`](hkquery/predicateforobject(with:).md) predicate. However, if you’re reading high-frequency data during a workout, you may want to include a [`predicateForSamples(withStart:end:options:)`](hkquery/predicateforsamples(withstart:end:options:).md) predicate that returns matching series data based on the workout’s time period instead.

```swift
// Create the predicate for the data.
let heartRate = HKQuantityType(.heartRate)
let objectPredicate = HKQuery.predicateForObject(with: myHeartRateSample.uuid)
let predicate = HKSamplePredicate.quantitySample(type: heartRate,
                                                 predicate: objectPredicate)


// Create the source descriptor.
let seriesDescriptor =
HKQuantitySeriesSampleQueryDescriptor(predicate: predicate,
                                      options: .orderByQuantitySampleStartDate)

// Get the AsyncSequence that returns the individual data entries.
let series = seriesDescriptor.results(for: store)

// Access each data entry in the series
for try await entry in series {
    
    // Process results here.
    let steps = entry.quantity.doubleValue(for: .count())
    print(steps)
}
```

While this method returns an [`AsyncSequence`](https://developer.apple.com/documentation/Swift/AsyncSequence), unlike the long-running queries, this sequence has a finite size. Iterating over the sequence asynchronously returns data entries, automatically terminating after you receive all the data.

## Topics

### Creating Series Query Descriptors
- [init(predicate: HKSamplePredicate<HKQuantitySample>, options: HKQuantitySeriesSampleQueryDescriptor.Options)](hkquantityseriessamplequerydescriptor/init(predicate:options:).md)
  Creates a quantity series query descriptor.
- [HKQuantitySeriesSampleQueryDescriptor.Options](hkquantityseriessamplequerydescriptor/options-swift.struct.md)
  Options used when querying series data.
### Running Queries
- [func results(for: HKHealthStore) -> HKQuantitySeriesSampleQueryDescriptor.Results](hkquantityseriessamplequerydescriptor/results(for:).md)
  Runs a one-shot query that returns an asynchronous sequence of matching series samples.
- [HKQuantitySeriesSampleQueryDescriptor.Results](hkquantityseriessamplequerydescriptor/results.md)
  An asynchronous sequence that emits data from the quantity series query.
- [HKQuantitySeriesSampleQueryDescriptor.Result](hkquantityseriessamplequerydescriptor/result.md)
  A set of results from a quantity series sample descriptor.
### Accessing Query Properties
- [var options: HKQuantitySeriesSampleQueryDescriptor.Options](hkquantityseriessamplequerydescriptor/options-swift.property.md)
  A set of options for the query. For a list of possible values, see [`HKQuantitySeriesSampleQueryDescriptor.Options`](hkquantityseriessamplequerydescriptor/options-swift.struct.md).
- [var predicate: HKSamplePredicate<HKQuantitySample>](hkquantityseriessamplequerydescriptor/predicate.md)
  A predicate that defines the set of series samples that the query returns.
### Default Implementations
- [HKAsyncSequenceQuery Implementations](hkquantityseriessamplequerydescriptor/hkasyncsequencequery-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [HKAsyncSequenceQuery](hkasyncsequencequery.md)

## See Also

- [class HKQuantitySeriesSampleQuery](hkquantityseriessamplequery.md)
  A query that accesses the series data associated with a quantity sample.
- [struct HKWorkoutRouteQueryDescriptor](hkworkoutroutequerydescriptor.md)
  A query interface that reads the location data stored in a workout route using Swift concurrency.
- [class HKWorkoutRouteQuery](hkworkoutroutequery.md)
  A query to access the location data stored in a workout route.
- [struct HKHeartbeatSeriesQueryDescriptor](hkheartbeatseriesquerydescriptor.md)
  A query interface that reads the heartbeat series data stored in a heartbeat sample using Swift concurrency.
- [class HKHeartbeatSeriesQuery](hkheartbeatseriesquery.md)
  A query that returns the heartbeat data contained in a heartbeat series sample.
- [struct HKElectrocardiogramQueryDescriptor](hkelectrocardiogramquerydescriptor.md)
  A query interface that reads the underlying voltage measurements for an electrocardiogram sample using Swift concurrency.
- [class HKElectrocardiogramQuery](hkelectrocardiogramquery.md)
  A query that returns the underlying voltage measurements for an electrocardiogram sample.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkquantityseriessamplequerydescriptor)*