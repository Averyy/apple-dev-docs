# localMember

**Framework**: LiveCommunicationKit  
**Kind**: property  
**Role**: Instance Property

The handle that identifies the local participant to remote participants.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+
- visionOS 1.1+
- watchOS 10.4+

## Declaration

```swift
final var localMember: Handle? { get }
```

## Discussion

The `localMember` is only available to the [`ConversationManager`](../conversationmanager.md) that provides the [`Conversation`](../conversation.md).

## See Also

### Describing a conversation
- [var state: Conversation.State](./state-swift.property.md)
  The current state of the conversation.
- [Conversation.State](./state-swift.enum.md)
  Values that describe the current state of a conversation.
- [let uuid: UUID](./uuid.md)
  The unique identifier for a conversation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/livecommunicationkit/conversation/localmember)*