# GroupSessionMessenger.Messages

**Framework**: Group Activities  
**Kind**: struct

An asynchronous sequence of messages sent to the session.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
struct Messages<Message> where Message : Decodable, Message : Encodable
```

#### Overview

When you use a [`GroupSessionMessenger`](groupsessionmessenger.md) to communicate across devices, the `Messages` structure provides the sequence of messages the other devices send. Iterate over the contents of this structure asynchronously to retrieve each message and update your app.

Don’t create this structure directly. Instead, use the [`messages(of:)`](groupsessionmessenger/messages(of:)-626qo.md) or [`messages(of:)`](groupsessionmessenger/messages(of:)-jvoz.md) method to retrieve the messages for a given session.

## Topics

### Creating an iterator
- [GroupSessionMessenger.Messages.Iterator](groupsessionmessenger/messages/iterator.md)

## Relationships

### Conforms To
- [AsyncSequence](../Swift/AsyncSequence.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [func messages(of: Data.Type) -> GroupSessionMessenger.Messages<Data>](groupsessionmessenger/messages(of:)-626qo.md)
  Returns the asynchronous sequence of messages that contain a generic data object.
- [func messages<Message>(of: Message.Type) -> GroupSessionMessenger.Messages<Message>](groupsessionmessenger/messages(of:)-jvoz.md)
  Returns the asynchronous sequence of messages that match the app-specific type.
- [GroupSessionMessenger.MessageContext](groupsessionmessenger/messagecontext.md)
  A structure that contains additional information about an incoming message, such as which device sent it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/groupactivities/groupsessionmessenger/messages)*