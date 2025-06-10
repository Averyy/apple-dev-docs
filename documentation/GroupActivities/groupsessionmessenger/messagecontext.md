# GroupSessionMessenger.MessageContext

**Framework**: Group Activities  
**Kind**: struct

A structure that contains additional information about an incoming message, such as which device sent it.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
struct MessageContext
```

## Mentions

- [Synchronizing data during a SharePlay activity](synchronizing-data-during-a-shareplay-activity.md)

## Topics

### Getting the initiating participant
- [var source: Participant](groupsessionmessenger/messagecontext/source.md)
  The participant device that sent the message.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [func messages(of: Data.Type) -> GroupSessionMessenger.Messages<Data>](groupsessionmessenger/messages(of:)-626qo.md)
  Returns the asynchronous sequence of messages that contain a generic data object.
- [func messages<Message>(of: Message.Type) -> GroupSessionMessenger.Messages<Message>](groupsessionmessenger/messages(of:)-jvoz.md)
  Returns the asynchronous sequence of messages that match the app-specific type.
- [GroupSessionMessenger.Messages](groupsessionmessenger/messages.md)
  An asynchronous sequence of messages sent to the session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/groupactivities/groupsessionmessenger/messagecontext)*