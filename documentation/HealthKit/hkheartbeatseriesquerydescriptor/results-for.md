# results(for:)

**Framework**: HealthKit  
**Kind**: method

Runs a one-shot query that returns an asynchronous sequence of data representing individual heartbeats.

**Availability**:
- iOS 15.4+
- iPadOS 15.4+
- Mac Catalyst 15.4+
- macOS 13.0+
- visionOS ?+
- watchOS 8.5+

## Declaration

```swift
func results(for healthStore: HKHealthStore) -> HKHeartbeatSeriesQueryDescriptor.Results
```

## Parameters

- `healthStore`: The access point for HealthKit data.

## See Also

- [HKHeartbeatSeriesQueryDescriptor.Results](hkheartbeatseriesquerydescriptor/results.md)
  An asynchronous sequence that emits data about individual heartbeats from a heartbeat series sample.
- [HKHeartbeatSeriesQueryDescriptor.Heartbeat](hkheartbeatseriesquerydescriptor/heartbeat.md)
  Data about an individual heartbeat.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkheartbeatseriesquerydescriptor/results(for:))*