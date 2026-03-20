# AVPlayerInterstitialEventMonitor.ScheduleRequestCompleted

**Framework**: AVFoundation  
**Kind**: struct

A NotificationCenter AsyncMessage that is sent when a daterange-schedule request completes

**Availability**:
- iOS 26.4+
- iPadOS 26.4+
- Mac Catalyst ?+
- macOS 26.4+
- tvOS 26.4+
- visionOS 26.4+
- watchOS 26.4+

## Declaration

```swift
struct ScheduleRequestCompleted
```

## Parameters

- `scheduleIdentifier`: The ID attribute of the daterange-schedule
- `result`: On success, the serialized JSON Data from the schedule response

## Topics

### Instance Properties
- [let result: Result<Data, any Error>](avplayerinterstitialeventmonitor/schedulerequestcompleted/result.md)
- [let scheduleIdentifier: String](avplayerinterstitialeventmonitor/schedulerequestcompleted/scheduleidentifier.md)

## Relationships

### Conforms To
- [NotificationCenter.AsyncMessage](../Foundation/NotificationCenter/AsyncMessage.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayerinterstitialeventmonitor/schedulerequestcompleted)*