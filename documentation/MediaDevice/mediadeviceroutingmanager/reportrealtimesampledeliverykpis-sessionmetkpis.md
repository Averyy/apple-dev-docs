# reportRealtimeSampleDeliveryKPIs(session:metKPIs:)

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
final func reportRealtimeSampleDeliveryKPIs(session: MediaOutputSession, metKPIs: Bool)
```

#### Discussion

Call this function after [`stopRealtimeSampleDelivery(session:)`](realtimesamplehandling/stoprealtimesampledelivery(session:).md) to indicate whether the realtime streaming session has met the expected quality thresholds for the duration of the session (e.g., latency, frame rate, audio quality).

## Parameters

- `session`: The session associated with the realtime delivery.
- `metKPIs`: `true` if the realtime session met quality KPIs, `false` otherwise.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediadevice/mediadeviceroutingmanager/reportrealtimesampledeliverykpis(session:metkpis:))*