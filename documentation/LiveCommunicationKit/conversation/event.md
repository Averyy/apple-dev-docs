# Conversation.Event

**Framework**: LiveCommunicationKit  
**Kind**: enum

Values that tell the system what happened during a conversation.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+
- visionOS 1.1+
- watchOS 10.4+

## Declaration

```swift
enum Event
```

## Topics

- [Conversation.Event.conversationConnected(_:)](conversation/event/conversationconnected(_:).md)
  Informs that system that conversation successfully connected at a point in time.
- [case conversationEnded(Date, Conversation.EndedReason)](conversation/event/conversationended(_:_:).md)
  Informs that system that a conversation ended at a point in time with a reason.
- [Conversation.Event.conversationStartedConnecting(_:)](conversation/event/conversationstartedconnecting(_:).md)
  Informs the system that a conversation has started to connect participants at a point in time.
- [case conversationUpdated(Conversation.Update)](conversation/event/conversationupdated(_:).md)
  Updates a conversation’s attributes and capabilities.

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [Conversation.EndedReason](conversation/endedreason.md)
  Values that describe why a conversation ended.


---

*[View on Apple Developer](https://developer.apple.com/documentation/livecommunicationkit/conversation/event)*