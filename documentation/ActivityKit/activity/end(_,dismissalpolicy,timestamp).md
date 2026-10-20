# end(_:dismissalPolicy:timestamp:)

**Framework**: ActivityKit  
**Kind**: method  
**Role**: Instance Method

Ends an active Live Activity.

**Availability**:
- iOS 17.2+
- iPadOS 17.2+

## Declaration

```swift
func end(_ content: ActivityContent<Activity<Attributes>.ContentState>?, dismissalPolicy: ActivityUIDismissalPolicy = .default, timestamp: Date) async
```

#### Discussion

End an active Live Activity while your app is in the foreground or while it’s in the background — for example, by using [Background Tasks](../../BackgroundTasks/BackgroundTasks.md). When you end a Live Activity, include a final content update using the `content` parameter to ensure the Live Activity shows the latest and final content update after it ends. This is important because the Live Activity may remain visible until the system or the person removes it.

## Parameters

- `content`: The latest and final dynamic content for the Live Activity that ended. The size of the encoded content can’t exceed 4KB in size.
- `dismissalPolicy`: Describes how and when the system should dismiss a Live Activity and remove it from the Lock Screen.
- `timestamp`: The time the data in the payload was generated. If this is older than a previous update or push payload, the system ignores this update.

## See Also

### Ending a Live Activity
- [func end(ActivityContent<Activity<Attributes>.ContentState>?, dismissalPolicy: ActivityUIDismissalPolicy) async](./end%28_,dismissalpolicy%29.md)
  Ends an active Live Activity.
- [struct ActivityUIDismissalPolicy](../activityuidismissalpolicy.md)
  The structure that describes when the system should remove a Live Activity that ended.


---

*[View on Apple Developer](https://developer.apple.com/documentation/activitykit/activity/end(_:dismissalpolicy:timestamp:))*