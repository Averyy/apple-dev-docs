# HKElectrocardiogramQueryDescriptor

**Framework**: HealthKit  
**Kind**: struct

A query interface that reads the underlying voltage measurements for an electrocardiogram sample using Swift concurrency.

**Availability**:
- iOS 15.4+
- iPadOS 15.4+
- Mac Catalyst 15.4+
- macOS 13.0+
- visionOS ?+
- watchOS 8.5+

## Declaration

```swift
struct HKElectrocardiogramQueryDescriptor
```

#### Overview

Use [`HKElectrocardiogramQueryDescriptor`](hkelectrocardiogramquerydescriptor.md) to access the individual voltage measurements associated with an [`HKElectrocardiogram`](hkelectrocardiogram.md) sample. To read the individual voltage measurements, create an electrocardiogram query descriptor using the desired sample, and then call the [`results(for:)`](hkheartbeatseriesquerydescriptor/results(for:).md) method on the descriptor.

```swift
// Create the descriptor.
let ecgDescriptor = HKElectrocardiogramQueryDescriptor(myElectrocardiogram)

// Get the AsyncSequence that returns individual voltage measurements.
let voltages = ecgDescriptor.results(for: store)

// Access each voltage measurement.
for try await measurement in voltages {
    
    // Process the results here.
    print(measurement.quantity(for: .appleWatchSimilarToLeadI) ?? "No Measurement")
    print(measurement.timeSinceSampleStart)
}
```

While this method returns an [`AsyncSequence`](https://developer.apple.com/documentation/Swift/AsyncSequence), unlike the long-running queries, this sequence has a finite size. Iterating over the sequence asynchronously returns voltage measurements, automatically terminating after you receive all the measurements.

## Topics

### Creating Electrocardiogram Query Descriptors
- [init(HKElectrocardiogram)](hkelectrocardiogramquerydescriptor/init(_:).md)
  Creates a query descriptor that reads voltage measurements from the provided electrocardiogram sample.
### Running Queries
- [func results(for: HKHealthStore) -> HKElectrocardiogramQueryDescriptor.Results](hkelectrocardiogramquerydescriptor/results(for:).md)
  Runs a one-shot query that returns an asynchronous sequence of data representing individual heartbeats.
- [HKElectrocardiogramQueryDescriptor.Results](hkelectrocardiogramquerydescriptor/results.md)
  An asynchronous sequence that emits data about individual voltage measurements from an electrocardiogram sample.
### Accessing Query Properties
- [var electrocardiogram: HKElectrocardiogram](hkelectrocardiogramquerydescriptor/electrocardiogram.md)
  The sample that contains the voltage measurements.
### Default Implementations
- [HKAsyncSequenceQuery Implementations](hkelectrocardiogramquerydescriptor/hkasyncsequencequery-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [HKAsyncSequenceQuery](hkasyncsequencequery.md)

## See Also

- [struct HKQuantitySeriesSampleQueryDescriptor](hkquantityseriessamplequerydescriptor.md)
  A query interface that reads the series data associated with quantity samples using Swift concurrency.
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
- [class HKElectrocardiogramQuery](hkelectrocardiogramquery.md)
  A query that returns the underlying voltage measurements for an electrocardiogram sample.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkelectrocardiogramquerydescriptor)*