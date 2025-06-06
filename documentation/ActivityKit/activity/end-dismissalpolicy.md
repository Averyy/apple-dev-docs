# end(_:dismissalPolicy:)

**Framework**: ActivityKit  
**Kind**: method

Ends an active Live Activity.

**Availability**:
- iOS 16.2+
- iPadOS 16.2+

## Declaration

```swift
func end(_ content: ActivityContent<Activity<Attributes>.ContentState>?, dismissalPolicy: ActivityUIDismissalPolicy = .default) async
```

## Mentions

- [Displaying live data with Live Activities](displaying-live-data-with-live-activities.md)

#### Discussion

End an active Live Activity while your app is in the foreground or while it’s in the background — for example, by using [`Background Tasks`](https://developer.apple.com/documentation/BackgroundTasks). When you end a Live Activity, include a final content update using the `content` parameter to ensure the Live Activity shows the latest and final content update after it ends. This is important because the Live Activity may remain visible until the system or the person removes it.

## Parameters

- `content`: The latest and final dynamic content for the Live Activity that ended.   The size of the encoded content can’t exceed 4KB in size.
- `dismissalPolicy`: Describes how and when the system should dismiss a Live Activity and   and remove it from the Lock Screen.

## See Also

- [struct ActivityUIDismissalPolicy](activityuidismissalpolicy.md)
  The structure that describes when the system should remove a Live Activity that ended.
- [func end(ActivityContent<Activity<Attributes>.ContentState>?, dismissalPolicy: ActivityUIDismissalPolicy, timestamp: Date) async](activity/end(_:dismissalpolicy:timestamp:).md)
  Ends an active Live Activity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/activitykit/activity/end(_:dismissalpolicy:))*