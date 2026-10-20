# Conversation.Event

**Framework**: LiveCommunicationKit  
**Kind**: enum  
**Role**: Enumeration

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

- [Conversation.Event.conversationConnected(_:)](./event/conversationconnected%28_%29.md)
  Informs that system that conversation successfully connected at a point in time.
- [case conversationEnded(Date, Conversation.EndedReason)](./event/conversationended%28_,_%29.md)
  Informs that system that a conversation ended at a point in time with a reason.
- [Conversation.Event.conversationStartedConnecting(_:)](./event/conversationstartedconnecting%28_%29.md)
  Informs the system that a conversation has started to connect participants at a point in time.
- [case conversationUpdated(Conversation.Update)](./event/conversationupdated%28_%29.md)
  Updates a conversation’s attributes and capabilities.

## Relationships

### Conforms To
- [Decodable](../../Swift/decodable.md)
- [Encodable](../../Swift/encodable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Observing a conversation
- [Conversation.EndedReason](./endedreason.md)
  Values that describe why a conversation ended.


---

*[View on Apple Developer](https://developer.apple.com/documentation/livecommunicationkit/conversation/event)*