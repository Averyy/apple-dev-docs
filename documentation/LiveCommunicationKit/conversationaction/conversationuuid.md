# conversationUUID

**Framework**: LiveCommunicationKit  
**Kind**: property  
**Role**: Instance Property

The unique identifier for the action’s associated conversation.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+
- visionOS 1.1+
- watchOS 10.4+

## Declaration

```swift
final var conversationUUID: UUID { get }
```

## See Also

### Accessing action attributes
- [var uuid: UUID](./uuid.md)
  The unique identifier that identifies the action.
- [var timeoutDate: Date](./timeoutdate.md)
  The point in time that marks when the action can’t be completed anymore.
- [var state: ConversationAction.State](./state-swift.property.md)
  The action’s current state.
- [ConversationAction.State](./state-swift.enum.md)
  A type that describes the current state of a conversation action.


---

*[View on Apple Developer](https://developer.apple.com/documentation/livecommunicationkit/conversationaction/conversationuuid)*