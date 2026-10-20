# ConversationAction.State

**Framework**: LiveCommunicationKit  
**Kind**: enum  
**Role**: Enumeration

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
- [ConversationAction.State.complete](./state-swift.enum/complete.md)
  The action finished successfully.
- [ConversationAction.State.failed(reason:)](./state-swift.enum/failed%28reason%29.md)
  Indicates that the action failed.
- [ConversationAction.State.idle](./state-swift.enum/idle.md)
  The action has been created but hasn’t started.
- [ConversationAction.State.running](./state-swift.enum/running.md)
  The action is currently processing.

## Relationships

### Conforms To
- [Decodable](../../Swift/decodable.md)
- [Encodable](../../Swift/encodable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Accessing action attributes
- [var conversationUUID: UUID](./conversationuuid.md)
  The unique identifier for the action’s associated conversation.
- [var uuid: UUID](./uuid.md)
  The unique identifier that identifies the action.
- [var timeoutDate: Date](./timeoutdate.md)
  The point in time that marks when the action can’t be completed anymore.
- [var state: ConversationAction.State](./state-swift.property.md)
  The action’s current state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/livecommunicationkit/conversationaction/state-swift.enum)*