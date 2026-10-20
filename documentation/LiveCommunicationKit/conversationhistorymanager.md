# ConversationHistoryManager

**Framework**: LiveCommunicationKit  
**Kind**: class  
**Role**: Class

An interface for managing and providing conversation history.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
final class ConversationHistoryManager
```

## Mentions

- [Preparing your app to be the default dialer app](./preparing-your-app-to-be-the-default-dialer-app.md)

## Topics

### Accessing the conversation history
- [static let sharedInstance: ConversationHistoryManager](./conversationhistorymanager/sharedinstance.md)
### Managing recent conversations
- [func recentConversations(matching: Predicate<ConversationHistoryManager.RecentConversation>) async throws -> [ConversationHistoryManager.RecentConversation]](./conversationhistorymanager/recentconversations%28matching%29.md)
  Returns a list of recent conversations that match the given predicate.
- [func markConversationAsRead(ConversationHistoryManager.RecentConversation) async throws](./conversationhistorymanager/markconversationasread%28_%29.md)
  Marks a conversation as read.
- [func markConversationsAsRead([ConversationHistoryManager.RecentConversation]) async throws](./conversationhistorymanager/markconversationsasread%28_%29.md)
  Marks the a list of conversations as read.
- [ConversationHistoryManager.RecentConversation](./conversationhistorymanager/recentconversation.md)
  A structure that describes a recent conversation.
### Responding to conversation history updates
- [ConversationHistoryManager.ConversationHistoryDidUpdate](./conversationhistorymanager/conversationhistorydidupdate.md)
  A message you can observe to receive conversation history updates if your app is the default dialer app.

## Relationships

### Conforms To
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### VoIP conversations
- [class ConversationManager](./conversationmanager.md)
  An interface for managing and observing VoIP conversations.
- [protocol ConversationManagerDelegate](./conversationmanagerdelegate.md)
  Methods for managing conversations and receiving VoIP conversation updates.
- [class Conversation](./conversation.md)
  A type that describes a video or audio conversation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/livecommunicationkit/conversationhistorymanager)*