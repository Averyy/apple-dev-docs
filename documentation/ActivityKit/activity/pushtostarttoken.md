# pushToStartToken

**Framework**: ActivityKit  
**Kind**: property  
**Role**: Type Property

The token you use to start a Live Activity with an ActivityKit push notification.

**Availability**:
- iOS 17.2+
- iPadOS 17.2+

## Declaration

```swift
static var pushToStartToken: Data? { get }
```

## Discussion

The push token for a Live Activity may change over time. Use the [`pushToStartTokenUpdates`](./pushtostarttokenupdates.md) asynchronous sequence to receive an updated push-to-start token. When you receive an updated push token, make sure to send it to your server and invalidate the outdated token.

## See Also

### Using ActivityKit push notifications
- [var pushToken: Data?](./pushtoken.md)
  The token you use to send ActivityKit push notifications to a Live Activity.
- [var pushTokenUpdates: Activity<Attributes>.PushTokenUpdates](./pushtokenupdates-swift.property.md)
  An asynchronous sequence you use to observe changes to the push token of a Live Activity.
- [Activity.PushTokenUpdates](./pushtokenupdates-swift.struct.md)
  A structure that offers functionality to observe changes to the push token of a Live Activity.
- [static var pushToStartTokenUpdates: Activity<Attributes>.PushTokenUpdates](./pushtostarttokenupdates.md)
  An asynchronous sequence you use to observe changes to the token for starting a Live Activity with an ActivityKit push notification.


---

*[View on Apple Developer](https://developer.apple.com/documentation/activitykit/activity/pushtostarttoken)*