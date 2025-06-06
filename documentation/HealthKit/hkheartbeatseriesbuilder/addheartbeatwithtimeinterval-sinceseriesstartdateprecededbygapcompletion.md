# addHeartbeatWithTimeInterval(sinceSeriesStartDate:precededByGap:completion:)

**Framework**: HealthKit  
**Kind**: method

Adds a heartbeat to the series.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
func addHeartbeat(at timeIntervalSinceStart: TimeInterval, precededByGap: Bool) async throws
```

## Parameters

- `timeIntervalSinceStart`: The time of the heartbeat, measured from the series builder’s start date. This must be a positive value.
- `precededByGap`: A Boolean value that indicates whether this heartbeat was immediately preceded by a gap in the data, indicating that one or more heartbeats may be missing.
- `completion`: The completion handler called by the builder after it attempts to add the heartbeat to the series. The completion handler takes the following parameters:

## See Also

- [func addMetadata([String : Any], completion: (Bool, (any Error)?) -> Void)](hkheartbeatseriesbuilder/addmetadata(_:completion:).md)
  Adds metadata to the sample.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkheartbeatseriesbuilder/addheartbeatwithtimeinterval(sinceseriesstartdate:precededbygap:completion:))*