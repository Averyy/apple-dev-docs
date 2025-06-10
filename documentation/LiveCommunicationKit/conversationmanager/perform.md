# perform(_:)

**Framework**: LiveCommunicationKit  
**Kind**: method

Tells the conversation manager to asynchronously perform actions for a conversation.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+
- visionOS 1.1+
- watchOS 10.4+

## Declaration

```swift
final func perform(_ actions: [ConversationAction]) async throws
```

## Parameters

- `actions`: An array of actions to perform for a conversation.

## See Also

- [func invalidate()](conversationmanager/invalidate.md)
  Invalidates the conversation manager, ends all conversations, and fails all pending concersation actions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/livecommunicationkit/conversationmanager/perform(_:))*