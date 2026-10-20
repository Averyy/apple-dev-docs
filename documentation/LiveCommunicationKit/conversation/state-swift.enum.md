# Conversation.State

**Framework**: LiveCommunicationKit  
**Kind**: enum  
**Role**: Enumeration

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
- [Conversation.State.idle](./state-swift.enum/idle.md)
  The conversation was registered with the system, but it’s not active yet.
- [Conversation.State.joined](./state-swift.enum/joined.md)
  Audio and video streams are active and the local participant is able to engage with remote participants.
- [Conversation.State.joining](./state-swift.enum/joining.md)
  The setup process of the conversation in progress; for example, establishing audio and video streams.
- [Conversation.State.leaving](./state-swift.enum/leaving.md)
  Participants left the conversation and it’s in the process of ending.
- [Conversation.State.left](./state-swift.enum/left.md)
  The conversation is no longer active and all audio and video sessions have ended.
- [Conversation.State.paused](./state-swift.enum/paused.md)
  Audio and video streams are paused, but may resume.

## Relationships

### Conforms To
- [Copyable](../../Swift/copyable.md)
- [Decodable](../../Swift/decodable.md)
- [Encodable](../../Swift/encodable.md)
- [Equatable](../../Swift/equatable.md)
- [Escapable](../../Swift/escapable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Describing a conversation
- [var localMember: Handle?](./localmember.md)
  The handle that identifies the local participant to remote participants.
- [var state: Conversation.State](./state-swift.property.md)
  The current state of the conversation.
- [let uuid: UUID](./uuid.md)
  The unique identifier for a conversation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/livecommunicationkit/conversation/state-swift.enum)*