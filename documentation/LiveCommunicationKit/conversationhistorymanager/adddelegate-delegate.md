# addDelegate(delegate:)

**Framework**: LiveCommunicationKit  
**Kind**: method

Adds a delegate that receives callbacks about changes to the available conversation history.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+

## Declaration

```swift
final func addDelegate(delegate: any ConversationHistoryManagerDelegate)
```

## See Also

- [func fetch(request: Predicate<ConversationHistoryManager.RecentConversation>) async throws -> [ConversationHistoryManager.RecentConversation]](conversationhistorymanager/fetch(request:).md)
  Queries the conversation history for conversations that match a given condition.
- [func markAsRead(recentConversations: [ConversationHistoryManager.RecentConversation]) async throws](conversationhistorymanager/markasread(recentconversations:).md)
  Marks the a list of conversations as read.
- [ConversationHistoryManager.RecentConversation](conversationhistorymanager/recentconversation.md)
  A structure that describes a recent conversation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/livecommunicationkit/conversationhistorymanager/adddelegate(delegate:))*