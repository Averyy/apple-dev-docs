# recentConversations(matching:)

**Framework**: LiveCommunicationKit  
**Kind**: method

Returns a list of recent conversations that match the given predicate.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+

## Declaration

```swift
final func recentConversations(matching request: Predicate<ConversationHistoryManager.RecentConversation>) async throws -> [ConversationHistoryManager.RecentConversation]
```

## See Also

- [func markConversationAsRead(ConversationHistoryManager.RecentConversation) async throws](conversationhistorymanager/markconversationasread(_:).md)
  Marks a conversation as read.
- [func markConversationsAsRead([ConversationHistoryManager.RecentConversation]) async throws](conversationhistorymanager/markconversationsasread(_:).md)
  Marks the a list of conversations as read.
- [ConversationHistoryManager.RecentConversation](conversationhistorymanager/recentconversation.md)
  A structure that describes a recent conversation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/livecommunicationkit/conversationhistorymanager/recentconversations(matching:))*