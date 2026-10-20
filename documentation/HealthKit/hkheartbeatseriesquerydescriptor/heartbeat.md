# HKHeartbeatSeriesQueryDescriptor.Heartbeat

**Framework**: HealthKit  
**Kind**: struct  
**Role**: Structure

Data about an individual heartbeat.

**Availability**:
- iOS 15.4+
- iPadOS 15.4+
- Mac Catalyst 15.4+
- macOS 13.0+
- visionOS
- watchOS 8.5+

## Declaration

```swift
struct Heartbeat
```

## Topics

### Accessing Heartbeat Data
- [let precededByGap: Bool](./heartbeat/precededbygap.md)
- [let timeIntervalSinceStart: TimeInterval](./heartbeat/timeintervalsincestart.md)

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)

## See Also

### Running Queries
- [func results(for: HKHealthStore) -> HKHeartbeatSeriesQueryDescriptor.Results](./results%28for%29.md)
  Runs a one-shot query that returns an asynchronous sequence of data representing individual heartbeats.
- [HKHeartbeatSeriesQueryDescriptor.Results](./results.md)
  An asynchronous sequence that emits data about individual heartbeats from a heartbeat series sample.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkheartbeatseriesquerydescriptor/heartbeat)*