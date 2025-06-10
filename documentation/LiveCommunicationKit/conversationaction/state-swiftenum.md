# ConversationAction.State

**Framework**: LiveCommunicationKit  
**Kind**: enum

A type that describes the current state of a conversation action.

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

### Constants
- [ConversationAction.State.complete](conversationaction/state-swift.enum/complete.md)
  The action finished successfully.
- [ConversationAction.State.failed(reason:)](conversationaction/state-swift.enum/failed(reason:).md)
  Indicates that the action failed.
- [ConversationAction.State.idle](conversationaction/state-swift.enum/idle.md)
  The action has been created but hasn’t started.
- [ConversationAction.State.running](conversationaction/state-swift.enum/running.md)
  The action is currently processing.
### Operators
- [static func == (ConversationAction.State, ConversationAction.State) -> Bool](conversationaction/state-swift.enum/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
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
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var conversationUUID: UUID](conversationaction/conversationuuid.md)
  The unique identifier for the action’s associated conversation.
- [var uuid: UUID](conversationaction/uuid.md)
  The unique identifier that identifies the action.
- [var timeoutDate: Date](conversationaction/timeoutdate.md)
  The point in time that marks when the action can’t be completed anymore.
- [var state: ConversationAction.State](conversationaction/state-swift.property.md)
  The action’s current state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/livecommunicationkit/conversationaction/state-swift.enum)*