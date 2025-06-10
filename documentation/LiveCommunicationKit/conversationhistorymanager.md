# ConversationHistoryManager

**Framework**: LiveCommunicationKit  
**Kind**: class

An interface for managing and providing conversation history.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+

## Declaration

```swift
final class ConversationHistoryManager
```

## Mentions

- [Preparing your app to be the default dialer app](preparing-your-app-to-be-the-default-dialer-app.md)

## Topics

### Creating new managers
- [init()](conversationhistorymanager/init.md)
  Creates a structure for handling conversation history and recent conversation.
### Managing recent conversations
- [func addDelegate(delegate: any ConversationHistoryManagerDelegate)](conversationhistorymanager/adddelegate(delegate:).md)
  Adds a delegate that receives callbacks about changes to the available conversation history.
- [func fetch(request: Predicate<ConversationHistoryManager.RecentConversation>) async throws -> [ConversationHistoryManager.RecentConversation]](conversationhistorymanager/fetch(request:).md)
  Queries the conversation history for conversations that match a given condition.
- [func markAsRead(recentConversations: [ConversationHistoryManager.RecentConversation]) async throws](conversationhistorymanager/markasread(recentconversations:).md)
  Marks the a list of conversations as read.
- [ConversationHistoryManager.RecentConversation](conversationhistorymanager/recentconversation.md)
  A structure that describes a recent conversation.

## See Also

- [protocol ConversationHistoryManagerDelegate](conversationhistorymanagerdelegate.md)
  Methods for receiving updates to the conversation history.


---

*[View on Apple Developer](https://developer.apple.com/documentation/livecommunicationkit/conversationhistorymanager)*