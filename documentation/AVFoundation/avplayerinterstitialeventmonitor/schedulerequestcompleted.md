# AVPlayerInterstitialEventMonitor.ScheduleRequestCompleted

**Framework**: AVFoundation  
**Kind**: struct

A NotificationCenter AsyncMessage that is sent when a daterange-schedule request completes

**Availability**:
- iOS 26.4+
- iPadOS 26.4+
- Mac Catalyst 26.4+
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

### Inspecting the completion
- [let scheduleIdentifier: String](avplayerinterstitialeventmonitor/schedulerequestcompleted/scheduleidentifier.md)
- [let result: Result<Data, any Error>](avplayerinterstitialeventmonitor/schedulerequestcompleted/result.md)

## Relationships

### Conforms To
- [NotificationCenter.AsyncMessage](../foundation/notificationcenter/asyncmessage.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayerinterstitialeventmonitor/schedulerequestcompleted)*