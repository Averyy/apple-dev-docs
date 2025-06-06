# HKHeartbeatSeriesQueryDescriptor.Heartbeat

**Framework**: HealthKit  
**Kind**: struct

Data about an individual heartbeat.

**Availability**:
- iOS 15.4+
- iPadOS 15.4+
- Mac Catalyst 15.4+
- macOS 13.0+
- visionOS ?+
- watchOS 8.5+

## Declaration

```swift
struct Heartbeat
```

## Topics

### Accessing Heartbeat Data
- [let precededByGap: Bool](hkheartbeatseriesquerydescriptor/heartbeat/precededbygap.md)
- [let timeIntervalSinceStart: TimeInterval](hkheartbeatseriesquerydescriptor/heartbeat/timeintervalsincestart.md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)

## See Also

- [func results(for: HKHealthStore) -> HKHeartbeatSeriesQueryDescriptor.Results](hkheartbeatseriesquerydescriptor/results(for:).md)
  Runs a one-shot query that returns an asynchronous sequence of data representing individual heartbeats.
- [HKHeartbeatSeriesQueryDescriptor.Results](hkheartbeatseriesquerydescriptor/results.md)
  An asynchronous sequence that emits data about individual heartbeats from a heartbeat series sample.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkheartbeatseriesquerydescriptor/heartbeat)*