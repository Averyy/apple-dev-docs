# markConversationsAsRead(_:)

**Framework**: LiveCommunicationKit  
**Kind**: method

Marks the a list of conversations as read.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+

## Declaration

```swift
final func markConversationsAsRead(_ recentConversations: [ConversationHistoryManager.RecentConversation]) async throws
```

## Parameters

- `recentConversations`: A list of recent conversations that you want to mark as read.

## See Also

- [func recentConversations(matching: Predicate<ConversationHistoryManager.RecentConversation>) async throws -> [ConversationHistoryManager.RecentConversation]](conversationhistorymanager/recentconversations(matching:).md)
  Returns a list of recent conversations that match the given predicate.
- [func markConversationAsRead(ConversationHistoryManager.RecentConversation) async throws](conversationhistorymanager/markconversationasread(_:).md)
  Marks a conversation as read.
- [ConversationHistoryManager.RecentConversation](conversationhistorymanager/recentconversation.md)
  A structure that describes a recent conversation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/livecommunicationkit/conversationhistorymanager/markconversationsasread(_:))*