# pushTokenUpdates

**Framework**: ActivityKit  
**Kind**: property

An asynchronous sequence you use to observe changes to the push token of a Live Activity.

**Availability**:
- iOS 16.1+
- iPadOS 16.1+

## Declaration

```swift
var pushTokenUpdates: Activity<Attributes>.PushTokenUpdates { get }
```

## Mentions

- [Displaying live data with Live Activities](displaying-live-data-with-live-activities.md)
- [Starting and updating Live Activities with ActivityKit push notifications](starting-and-updating-live-activities-with-activitykit-push-notifications.md)

## See Also

- [var pushToken: Data?](activity/pushtoken.md)
  The token you use to send ActivityKit push notifications to a Live Activity.
- [Activity.PushTokenUpdates](activity/pushtokenupdates-swift.struct.md)
  A structure that offers functionality to observe changes to the push token of a Live Activity.
- [static var pushToStartToken: Data?](activity/pushtostarttoken.md)
  The token you use to start a Live Activity with an ActivityKit push notification.
- [static var pushToStartTokenUpdates: Activity<Attributes>.PushTokenUpdates](activity/pushtostarttokenupdates.md)
  An asynchronous sequence you use to observe changes to the token for starting a Live Activity with an ActivityKit push notification.


---

*[View on Apple Developer](https://developer.apple.com/documentation/activitykit/activity/pushtokenupdates-swift.property)*