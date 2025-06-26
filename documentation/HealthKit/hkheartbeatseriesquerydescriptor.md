# HKHeartbeatSeriesQueryDescriptor

**Framework**: HealthKit  
**Kind**: struct

A query interface that reads the heartbeat series data stored in a heartbeat sample using Swift concurrency.

**Availability**:
- iOS 15.4+
- iPadOS 15.4+
- Mac Catalyst 15.4+
- macOS 13.0+
- visionOS ?+
- watchOS 8.5+

## Declaration

```swift
struct HKHeartbeatSeriesQueryDescriptor
```

#### Overview

Use [`HKHeartbeatSeriesQueryDescriptor`](hkheartbeatseriesquerydescriptor.md) to read the heartbeat data included in a [`HKHeartbeatSeriesSample`](hkheartbeatseriessample.md). To read the individual heartbeats, create a heartbeat series query descriptor using the desired series sample, and then call the [`results(for:)`](hkheartbeatseriesquerydescriptor/results(for:).md) method on the descriptor.

```swift
// Create the descriptor.
let heartbeatDescriptor = HKHeartbeatSeriesQueryDescriptor(myHeartbeatSample)

// Get the AsyncSequence that returns individual heartbeats.
let series = heartbeatDescriptor.results(for: store)

// Access the data for each haeartbeat.
for try await heartbeat in series {
    
    // Process the results here.
    print(heartbeat.precededByGap)
    print(heartbeat.timeIntervalSinceStart)
}
```

While this method returns an [`AsyncSequence`](https://developer.apple.com/documentation/Swift/AsyncSequence), unlike the long-running queries, this sequence has a finite size. Iterating over the sequence asynchronously returns heartbeat data, automatically terminating after you receive all the data.

## Topics

### Creating Heartbeat Series Query Descriptors
- [init(HKHeartbeatSeriesSample)](hkheartbeatseriesquerydescriptor/init(_:).md)
  Creates a heartbeat series query descriptor.
### Running Queries
- [func results(for: HKHealthStore) -> HKHeartbeatSeriesQueryDescriptor.Results](hkheartbeatseriesquerydescriptor/results(for:).md)
  Runs a one-shot query that returns an asynchronous sequence of data representing individual heartbeats.
- [HKHeartbeatSeriesQueryDescriptor.Results](hkheartbeatseriesquerydescriptor/results.md)
  An asynchronous sequence that emits data about individual heartbeats from a heartbeat series sample.
- [HKHeartbeatSeriesQueryDescriptor.Heartbeat](hkheartbeatseriesquerydescriptor/heartbeat.md)
  Data about an individual heartbeat.
### Accessing Query Properties
- [var sample: HKHeartbeatSeriesSample](hkheartbeatseriesquerydescriptor/sample.md)
  The sample containing the heartbeat series.
### Default Implementations
- [HKAsyncSequenceQuery Implementations](hkheartbeatseriesquerydescriptor/hkasyncsequencequery-implementations.md)

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
- [class HKHeartbeatSeriesQuery](hkheartbeatseriesquery.md)
  A query that returns the heartbeat data contained in a heartbeat series sample.
- [struct HKElectrocardiogramQueryDescriptor](hkelectrocardiogramquerydescriptor.md)
  A query interface that reads the underlying voltage measurements for an electrocardiogram sample using Swift concurrency.
- [class HKElectrocardiogramQuery](hkelectrocardiogramquery.md)
  A query that returns the underlying voltage measurements for an electrocardiogram sample.
- [class HKWorkoutEffortRelationship](hkworkouteffortrelationship.md)
- [class HKWorkoutEffortRelationshipQuery](hkworkouteffortrelationshipquery.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkheartbeatseriesquerydescriptor)*