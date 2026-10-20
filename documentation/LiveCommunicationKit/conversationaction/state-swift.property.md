# state

**Framework**: LiveCommunicationKit  
**Kind**: property  
**Role**: Instance Property

The action’s current state.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+
- visionOS 1.1+
- watchOS 10.4+

## Declaration

```swift
final var state: ConversationAction.State { get }
```

## See Also

### Accessing action attributes
- [var conversationUUID: UUID](./conversationuuid.md)
  The unique identifier for the action’s associated conversation.
- [var uuid: UUID](./uuid.md)
  The unique identifier that identifies the action.
- [var timeoutDate: Date](./timeoutdate.md)
  The point in time that marks when the action can’t be completed anymore.
- [ConversationAction.State](./state-swift.enum.md)
  A type that describes the current state of a conversation action.


---

*[View on Apple Developer](https://developer.apple.com/documentation/livecommunicationkit/conversationaction/state-swift.property)*