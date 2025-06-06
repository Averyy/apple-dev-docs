# Conversation.State

**Framework**: LiveCommunicationKit  
**Kind**: enum

Represents the state of a `Conversation` at a given moment in time.

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

### Enumeration Cases
- [Conversation.State.idle](conversation/state-swift.enum/idle.md)
  The conversation has been registered with the system, but is not yet active.
- [Conversation.State.joined](conversation/state-swift.enum/joined.md)
  Audio/video streams are active and the user is able to engage with remote participants.
- [Conversation.State.joining](conversation/state-swift.enum/joining.md)
  The conversation is being prepared, e.g. audio and video streams are being established.
- [Conversation.State.leaving](conversation/state-swift.enum/leaving.md)
  The conversation is being torn down.
- [Conversation.State.left](conversation/state-swift.enum/left.md)
  The conversation is no longer active and any audio/video sessions have ended.
- [Conversation.State.paused](conversation/state-swift.enum/paused.md)
  Audio and video streams have been paused, but may be resumed.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/livecommunicationkit/conversation/state-swift.enum)*