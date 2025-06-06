# pushToken

**Framework**: ActivityKit  
**Kind**: property

The token you use to send ActivityKit push notifications to a Live Activity.

**Availability**:
- iOS 16.1+
- iPadOS 16.1+

## Declaration

```swift
var pushToken: Data? { get }
```

## Mentions

- [Starting and updating Live Activities with ActivityKit push notifications](starting-and-updating-live-activities-with-activitykit-push-notifications.md)

#### Discussion

The push token for a Live Activity may change over time. Use the [`pushTokenUpdates`](activity/pushtokenupdates-swift.property.md) asynchronous sequence to receive the updated push token. When you receive an updated push token, make sure to send it to your server and invalidate the outdated token.

## See Also

- [var pushTokenUpdates: Activity<Attributes>.PushTokenUpdates](activity/pushtokenupdates-swift.property.md)
  An asynchronous sequence you use to observe changes to the push token of a Live Activity.
- [Activity.PushTokenUpdates](activity/pushtokenupdates-swift.struct.md)
  A structure that offers functionality to observe changes to the push token of a Live Activity.
- [static var pushToStartToken: Data?](activity/pushtostarttoken.md)
  The token you use to start a Live Activity with an ActivityKit push notification.
- [static var pushToStartTokenUpdates: Activity<Attributes>.PushTokenUpdates](activity/pushtostarttokenupdates.md)
  An asynchronous sequence you use to observe changes to the token for starting a Live Activity with an ActivityKit push notification.


---

*[View on Apple Developer](https://developer.apple.com/documentation/activitykit/activity/pushtoken)*