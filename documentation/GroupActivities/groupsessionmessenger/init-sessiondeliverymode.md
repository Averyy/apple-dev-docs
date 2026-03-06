# init(session:deliveryMode:)

**Framework**: Group Activities  
**Kind**: init

Creates a new group session messenger with the specified delivery mode, [`GroupSessionMessenger.DeliveryMode`](groupsessionmessenger/deliverymode-swift.enum.md), and associates it with the specified session object.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
init<Activity>(session: GroupSession<Activity>, deliveryMode: GroupSessionMessenger.DeliveryMode) where Activity : GroupActivity
```

## Parameters

- `session`: The group session to use for communication with participants. Specify a session object that is in either the [`GroupSession.State.waiting`](groupsession/state-swift.enum/waiting.md) or [`GroupSession.State.joined`](groupsession/state-swift.enum/joined.md) state for this parameter. However, a session must be in the joined state to send or receive messages.
- `deliveryMode`: The delivery mode for sending and receiving messages. Specify a delivery mode option for the underlying transport of either [`GroupSessionMessenger.DeliveryMode.reliable`](groupsessionmessenger/deliverymode-swift.enum/reliable.md) or [`GroupSessionMessenger.DeliveryMode.unreliable`](groupsessionmessenger/deliverymode-swift.enum/unreliable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/groupactivities/groupsessionmessenger/init(session:deliverymode:))*