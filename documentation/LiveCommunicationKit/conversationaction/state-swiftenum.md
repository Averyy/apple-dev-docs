# ConversationAction.State

**Framework**: LiveCommunicationKit  
**Kind**: enum

Represents the current state of a `ConversationAction`.

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

### Operators
- [static func == (ConversationAction.State, ConversationAction.State) -> Bool](conversationaction/state-swift.enum/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Enumeration Cases
- [ConversationAction.State.complete](conversationaction/state-swift.enum/complete.md)
  The action completed successfully.
- [ConversationAction.State.failed(reason:)](conversationaction/state-swift.enum/failed(reason:).md)
  The action failed to complete successfully.
- [ConversationAction.State.idle](conversationaction/state-swift.enum/idle.md)
  The action has been created, but has not started executing.
- [ConversationAction.State.running](conversationaction/state-swift.enum/running.md)
  The action is currently being executed.
### Initializers
- [init(from: any Decoder) throws](conversationaction/state-swift.enum/init(from:).md)
  Creates a new instance by decoding from the given decoder.
### Instance Properties
- [var hashValue: Int](conversationaction/state-swift.enum/hashvalue.md)
  The hash value.
### Instance Methods
- [func encode(to: any Encoder) throws](conversationaction/state-swift.enum/encode(to:).md)
  Encodes this value into the given encoder.
- [func hash(into: inout Hasher)](conversationaction/state-swift.enum/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Default Implementations
- [Equatable Implementations](conversationaction/state-swift.enum/equatable-implementations.md)

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/livecommunicationkit/conversationaction/state-swift.enum)*