# HKHeartbeatSeriesQueryDescriptor.Results

**Framework**: HealthKit  
**Kind**: struct

An asynchronous sequence that emits data about individual heartbeats from a heartbeat series sample.

**Availability**:
- iOS 15.4+
- iPadOS 15.4+
- Mac Catalyst 15.4+
- macOS 13.0+
- visionOS ?+
- watchOS 8.5+

## Declaration

```swift
struct Results
```

## Topics

### Creating an Iterator
- [HKHeartbeatSeriesQueryDescriptor.Results.Iterator](hkheartbeatseriesquerydescriptor/results/iterator.md)
  An iterator for accessing individual data entries from the series.

## Relationships

### Conforms To
- [AsyncSequence](../Swift/AsyncSequence.md)

## See Also

- [func results(for: HKHealthStore) -> HKHeartbeatSeriesQueryDescriptor.Results](hkheartbeatseriesquerydescriptor/results(for:).md)
  Runs a one-shot query that returns an asynchronous sequence of data representing individual heartbeats.
- [HKHeartbeatSeriesQueryDescriptor.Heartbeat](hkheartbeatseriesquerydescriptor/heartbeat.md)
  Data about an individual heartbeat.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkheartbeatseriesquerydescriptor/results)*