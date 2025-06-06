# fallDetectionManager(_:didDetect:completionHandler:)

**Framework**: Core Motion  
**Kind**: method

Indicates a fall detection event occurred.

**Availability**:
- watchOS 7.2+

## Declaration

```swift
optional func fallDetectionManager(_ fallDetectionManager: CMFallDetectionManager, didDetect event: CMFallDetectionEvent) async
```

#### Discussion

If the user authorized fall detection, the system wakes or launches your app when a fall detection event occurs. Your app receives a short amount of time to run in the background. You must process the event and call the completion handler before the time expires, or the system suspends your app.

Additionally, each time the user launches your app, the system checks to see if a fall event has occurred during the recent past. If one has occurred, it calls this method.

Note that your app may receive the same event multiple times, for example, if the app crashes and relaunches. Always check the event’s [`date`](cmfalldetectionevent/date.md) property to determine whether your app has already received the event. The system guarantees that different fall events have different `date` values.

## Parameters

- `fallDetectionManager`: The fall detection manager for the event.
- `event`: An object containing data about the event.
- `handler`: A completion handler for the event. Call this handler as soon as you finish processing the event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremotion/cmfalldetectiondelegate/falldetectionmanager(_:diddetect:completionhandler:))*