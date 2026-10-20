# recentConversations(matching:)

**Framework**: LiveCommunicationKit  
**Kind**: method  
**Role**: Instance Method

Returns a list of recent conversations that match the given predicate.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
final func recentConversations(matching request: Predicate<ConversationHistoryManager.RecentConversation>) async throws -> [ConversationHistoryManager.RecentConversation]
```

## See Also

### Managing recent conversations
- [func markConversationAsRead(ConversationHistoryManager.RecentConversation) async throws](./markconversationasread%28_%29.md)
  Marks a conversation as read.
- [func markConversationsAsRead([ConversationHistoryManager.RecentConversation]) async throws](./markconversationsasread%28_%29.md)
  Marks the a list of conversations as read.
- [ConversationHistoryManager.RecentConversation](./recentconversation.md)
  A structure that describes a recent conversation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/livecommunicationkit/conversationhistorymanager/recentconversations(matching:))*