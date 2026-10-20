# delegate

**Framework**: LiveCommunicationKit  
**Kind**: property  
**Role**: Instance Property

The object that acts as the delegate of the conversation manager.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+
- visionOS 1.1+
- watchOS 10.4+

## Declaration

```swift
weak final var delegate: (any ConversationManagerDelegate)?
```

## See Also

### Configuring the manager
- [var conversations: [Conversation]](./conversations.md)
  Currently active conversations.
- [var pendingActions: [ConversationAction]](./pendingactions.md)
  All unfinished conversation actions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/livecommunicationkit/conversationmanager/delegate)*