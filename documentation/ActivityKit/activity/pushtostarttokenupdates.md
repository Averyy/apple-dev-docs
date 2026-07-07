# pushToStartTokenUpdates

**Framework**: ActivityKit  
**Kind**: property

An asynchronous sequence you use to observe changes to the token for starting a Live Activity with an ActivityKit push notification.

**Availability**:
- iOS 17.2+
- iPadOS 17.2+

## Declaration

```swift
static var pushToStartTokenUpdates: Activity<Attributes>.PushTokenUpdates { get }
```

## Mentions

- [Starting and updating Live Activities with ActivityKit push notifications](starting-and-updating-live-activities-with-activitykit-push-notifications.md)

#### Discussion

Adopt push notifications to not only update ongoing Live Activities, but also to start a new Live Activity. For additional information, see [`Starting and updating Live Activities with ActivityKit push notifications`](starting-and-updating-live-activities-with-activitykit-push-notifications.md).

## See Also

- [var pushToken: Data?](activity/pushtoken.md)
  The token you use to send ActivityKit push notifications to a Live Activity.
- [var pushTokenUpdates: Activity<Attributes>.PushTokenUpdates](activity/pushtokenupdates-swift.property.md)
  An asynchronous sequence you use to observe changes to the push token of a Live Activity.
- [Activity.PushTokenUpdates](activity/pushtokenupdates-swift.struct.md)
  A structure that offers functionality to observe changes to the push token of a Live Activity.
- [static var pushToStartToken: Data?](activity/pushtostarttoken.md)
  The token you use to start a Live Activity with an ActivityKit push notification.


---

*[View on Apple Developer](https://developer.apple.com/documentation/activitykit/activity/pushtostarttokenupdates)*