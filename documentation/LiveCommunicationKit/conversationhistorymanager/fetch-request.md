# fetch(request:)

**Framework**: LiveCommunicationKit  
**Kind**: method

Queries the conversation history for conversations that match a given condition.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+

## Declaration

```swift
final func fetch(request: Predicate<ConversationHistoryManager.RecentConversation>) async throws -> [ConversationHistoryManager.RecentConversation]
```

## Parameters

- `request`: Conditions that LiveCommunicationKit uses to filter the list of past conversations.

## See Also

- [func addDelegate(delegate: any ConversationHistoryManagerDelegate)](conversationhistorymanager/adddelegate(delegate:).md)
  Adds a delegate that receives callbacks about changes to the available conversation history.
- [func markAsRead(recentConversations: [ConversationHistoryManager.RecentConversation]) async throws](conversationhistorymanager/markasread(recentconversations:).md)
  Marks the a list of conversations as read.
- [ConversationHistoryManager.RecentConversation](conversationhistorymanager/recentconversation.md)
  A structure that describes a recent conversation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/livecommunicationkit/conversationhistorymanager/fetch(request:))*