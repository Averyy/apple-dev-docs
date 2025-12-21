# ConversationHistoryManager

**Framework**: LiveCommunicationKit  
**Kind**: class

An interface for managing and providing conversation history.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+

## Declaration

```swift
final class ConversationHistoryManager
```

## Mentions

- [Preparing your app to be the default dialer app](preparing-your-app-to-be-the-default-dialer-app.md)

## Topics

### Accessing the conversation history
- [static let sharedInstance: ConversationHistoryManager](conversationhistorymanager/sharedinstance.md)
### Managing recent conversations
- [func recentConversations(matching: Predicate<ConversationHistoryManager.RecentConversation>) async throws -> [ConversationHistoryManager.RecentConversation]](conversationhistorymanager/recentconversations(matching:).md)
  Returns a list of recent conversations that match the given predicate.
- [func markConversationAsRead(ConversationHistoryManager.RecentConversation) async throws](conversationhistorymanager/markconversationasread(_:).md)
  Marks a conversation as read.
- [func markConversationsAsRead([ConversationHistoryManager.RecentConversation]) async throws](conversationhistorymanager/markconversationsasread(_:).md)
  Marks the a list of conversations as read.
- [ConversationHistoryManager.RecentConversation](conversationhistorymanager/recentconversation.md)
  A structure that describes a recent conversation.
### Responding to conversation history updates
- [ConversationHistoryManager.ConversationHistoryDidUpdate](conversationhistorymanager/conversationhistorydidupdate.md)
  A message you can observe to receive conversation history updates if your app is the default dialer app.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class ConversationManager](conversationmanager.md)
  An interface for managing and observing VoIP conversations.
- [protocol ConversationManagerDelegate](conversationmanagerdelegate.md)
  Methods for managing conversations and receiving VoIP conversation updates.
- [class Conversation](conversation.md)
  A type that describes a video or audio conversation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/livecommunicationkit/conversationhistorymanager)*