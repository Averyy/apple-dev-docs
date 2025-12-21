# markConversationAsRead(_:)

**Framework**: LiveCommunicationKit  
**Kind**: method

Marks a conversation as read.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+

## Declaration

```swift
final func markConversationAsRead(_ recentConversation: ConversationHistoryManager.RecentConversation) async throws
```

## Parameters

- `recentConversation`: A recent conversation in the conversation history that you want to mark as read.

## See Also

- [func recentConversations(matching: Predicate<ConversationHistoryManager.RecentConversation>) async throws -> [ConversationHistoryManager.RecentConversation]](conversationhistorymanager/recentconversations(matching:).md)
  Returns a list of recent conversations that match the given predicate.
- [func markConversationsAsRead([ConversationHistoryManager.RecentConversation]) async throws](conversationhistorymanager/markconversationsasread(_:).md)
  Marks the a list of conversations as read.
- [ConversationHistoryManager.RecentConversation](conversationhistorymanager/recentconversation.md)
  A structure that describes a recent conversation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/livecommunicationkit/conversationhistorymanager/markconversationasread(_:))*