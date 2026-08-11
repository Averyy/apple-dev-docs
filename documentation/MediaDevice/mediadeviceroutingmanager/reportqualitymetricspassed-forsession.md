# reportQualityMetricsPassed(_:forSession:)

**Framework**: Media Device  
**Kind**: method

Reports whether the realtime sample delivery session has met its quality KPIs.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
@MainActor
final func reportQualityMetricsPassed(_ thresholdsMet: Bool, forSession session: MediaOutputSession)
```

#### Discussion

Call this function after [`stopRealtimeSampleDelivery(session:)`](realtimesamplehandling/stoprealtimesampledelivery(session:).md) to indicate whether the realtime streaming session has met the expected quality thresholds for the duration of the session (e.g., latency, frame rate, audio quality).

## Parameters

- `thresholdsMet`: `true` if the realtime session met quality KPIs, `false` otherwise.
- `session`: The session associated with the realtime delivery.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediadevice/mediadeviceroutingmanager/reportqualitymetricspassed(_:forsession:))*