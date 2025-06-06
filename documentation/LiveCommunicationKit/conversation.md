# Conversation

**Framework**: LiveCommunicationKit  
**Kind**: class

A VoIP conversation.

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

### Structures
- [Conversation.Capabilities](conversation/capabilities.md)
  Used to configure a `Conversation` as part of a `Conversation.Update`.
- [Conversation.Update](conversation/update.md)
  An encapsulation of new, changed, or deleted information about a conversation.
### Instance Properties
- [var localMember: Handle?](conversation/localmember.md)
  The handle used to identify the local member to remote members. Only available to the `ConversationProvider` that provided the conversation.
- [var state: Conversation.State](conversation/state-swift.property.md)
  The current state of the conversation.
- [var uuid: UUID](conversation/uuid.md)
  The unique identifier for this conversation.
### Enumerations
- [Conversation.EndedReason](conversation/endedreason.md)
  The reason that a `Conversation` ended.
- [Conversation.Event](conversation/event.md)
  Specifies the type of event that has happened.
- [Conversation.State](conversation/state-swift.enum.md)
  Represents the state of a `Conversation` at a given moment in time.
### Default Implementations
- [CustomDebugStringConvertible Implementations](conversation/customdebugstringconvertible-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [Observable](../Observation/Observable.md)
- [Sendable](../Swift/Sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/livecommunicationkit/conversation)*