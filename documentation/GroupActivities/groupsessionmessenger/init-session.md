# init(session:)

**Framework**: Group Activities  
**Kind**: init

Creates a new group session messenger with [`GroupSessionMessenger.DeliveryMode.reliable`](groupsessionmessenger/deliverymode-swift.enum/reliable.md) delivery mode and associates it with the specified session object.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
init<Activity>(session: GroupSession<Activity>) where Activity : GroupActivity
```

## Parameters

- `session`: The group session to use for communication with participants.   Specify a session object that is in either the    or    state for this   parameter. However, a session must be in the joined state to send   or receive messages.


---

*[View on Apple Developer](https://developer.apple.com/documentation/groupactivities/groupsessionmessenger/init(session:))*