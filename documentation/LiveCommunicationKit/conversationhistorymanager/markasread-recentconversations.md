# markAsRead(recentConversations:)

**Framework**: LiveCommunicationKit  
**Kind**: method

Marks the a list of conversations as read.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+

## Declaration

```swift
final func markAsRead(recentConversations: [ConversationHistoryManager.RecentConversation]) async throws
```

## Parameters

- `recentConversations`: A list of recent conversations.

## See Also

- [func addDelegate(delegate: any ConversationHistoryManagerDelegate)](conversationhistorymanager/adddelegate(delegate:).md)
  Adds a delegate that receives callbacks about changes to the available conversation history.
- [func fetch(request: Predicate<ConversationHistoryManager.RecentConversation>) async throws -> [ConversationHistoryManager.RecentConversation]](conversationhistorymanager/fetch(request:).md)
  Queries the conversation history for conversations that match a given condition.
- [ConversationHistoryManager.RecentConversation](conversationhistorymanager/recentconversation.md)
  A structure that describes a recent conversation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/livecommunicationkit/conversationhistorymanager/markasread(recentconversations:))*