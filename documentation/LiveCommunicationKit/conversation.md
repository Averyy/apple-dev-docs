# Conversation

**Framework**: LiveCommunicationKit  
**Kind**: class

A type that describes a video or audio conversation.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+
- visionOS 1.1+
- watchOS 10.4+

## Declaration

```swift
final class Conversation
```

## Topics

### Describing a conversation
- [var localMember: Handle?](conversation/localmember.md)
  The handle that identifies the local participant to remote participants.
- [var state: Conversation.State](conversation/state-swift.property.md)
  The current state of the conversation.
- [Conversation.State](conversation/state-swift.enum.md)
  Values that describe the current state of a conversation.
- [let uuid: UUID](conversation/uuid.md)
  The unique identifier for a conversation.
### Observing a conversation
- [Conversation.Event](conversation/event.md)
  Values that tell the system what happened during a conversation.
- [Conversation.EndedReason](conversation/endedreason.md)
  Values that describe why a conversation ended.
### Updating a conversation
- [Conversation.Update](conversation/update.md)
  A type that describes new, changed, or deleted capabilities and attributes of a conversation.
- [Conversation.Capabilities](conversation/capabilities.md)
  A type that describes capabilities of a conversation.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [Observable](../Observation/Observable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class ConversationManager](conversationmanager.md)
  An interface for managing and observing VoIP conversations.
- [protocol ConversationManagerDelegate](conversationmanagerdelegate.md)
  Methods for managing conversations and receiving VoIP conversation updates.
- [class ConversationHistoryManager](conversationhistorymanager.md)
  An interface for managing and providing conversation history.


---

*[View on Apple Developer](https://developer.apple.com/documentation/livecommunicationkit/conversation)*