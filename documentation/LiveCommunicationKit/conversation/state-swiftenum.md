# Conversation.State

**Framework**: LiveCommunicationKit  
**Kind**: enum

Values that describe the current state of a conversation.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+
- visionOS 1.1+
- watchOS 10.4+

## Declaration

```swift
enum State
```

## Topics

### States
- [Conversation.State.idle](conversation/state-swift.enum/idle.md)
  The conversation was registered with the system, but it’s not active yet.
- [Conversation.State.joined](conversation/state-swift.enum/joined.md)
  Audio and video streams are active and the local participant is able to engage with remote participants.
- [Conversation.State.joining](conversation/state-swift.enum/joining.md)
  The setup process of the conversation in progress; for example, establishing audio and video streams.
- [Conversation.State.leaving](conversation/state-swift.enum/leaving.md)
  Participants left the conversation and it’s in the process of ending.
- [Conversation.State.left](conversation/state-swift.enum/left.md)
  The conversation is no longer active and all audio and video sessions have ended.
- [Conversation.State.paused](conversation/state-swift.enum/paused.md)
  Audio and video streams are paused, but may resume.
### Initializers
- [init?(rawValue: Int)](conversation/state-swift.enum/init(rawvalue:).md)
  Creates a new instance with the specified raw value.
### Instance Properties
- [var rawValue: Int](conversation/state-swift.enum/rawvalue-swift.property.md)
  The corresponding value of the raw type.
### Type Aliases
- [Conversation.State.RawValue](conversation/state-swift.enum/rawvalue-swift.typealias.md)
  The raw type that can be used to represent all values of the conforming type.
### Default Implementations
- [Equatable Implementations](conversation/state-swift.enum/equatable-implementations.md)
- [RawRepresentable Implementations](conversation/state-swift.enum/rawrepresentable-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var localMember: Handle?](conversation/localmember.md)
  The handle that identifies the local participant to remote participants.
- [var state: Conversation.State](conversation/state-swift.property.md)
  The current state of the conversation.
- [var uuid: UUID](conversation/uuid.md)
  The unique identifier for a conversation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/livecommunicationkit/conversation/state-swift.enum)*