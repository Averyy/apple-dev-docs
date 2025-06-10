# ConversationHistoryManager.RecentConversation

**Framework**: LiveCommunicationKit  
**Kind**: struct

A structure that describes a recent conversation.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+

## Declaration

```swift
struct RecentConversation
```

## Topics

### Accessing a recent conversation
- [let date: Date](conversationhistorymanager/recentconversation/date.md)
  The point in time when the conversation started.
- [let direction: ConversationHistoryManager.RecentConversation.Direction](conversationhistorymanager/recentconversation/direction-swift.property.md)
  The direction of this conversation.
- [let duration: TimeInterval](conversationhistorymanager/recentconversation/duration.md)
  The duration of the conversation from the time the system connected the participants.
- [let handles: [Handle]](conversationhistorymanager/recentconversation/handles.md)
  The handles of the conversation’s participants.
- [let isRead: Bool](conversationhistorymanager/recentconversation/isread.md)
  A value that indicates whether a person marked the recent conversation as read.
- [let status: ConversationHistoryManager.RecentConversation.ConnectedStatus](conversationhistorymanager/recentconversation/status.md)
  The status of the conversation.
- [ConversationHistoryManager.RecentConversation.ConnectedStatus](conversationhistorymanager/recentconversation/connectedstatus.md)
  Values that indicate the connection status of a recent conversation.
- [ConversationHistoryManager.RecentConversation.Direction](conversationhistorymanager/recentconversation/direction-swift.enum.md)
  Values that indicate whether a conversation was initiated or received.
### Identifying a recent conversation
- [let id: UUID](conversationhistorymanager/recentconversation/id-swift.property.md)
  The unique identifier of the recent conversation.
- [ConversationHistoryManager.RecentConversation.ID](conversationhistorymanager/recentconversation/id-swift.typealias.md)
  A type representing the stable identity of the entity associated with an instance.

## Relationships

### Conforms To
- [Identifiable](../Swift/Identifiable.md)

## See Also

- [func addDelegate(delegate: any ConversationHistoryManagerDelegate)](conversationhistorymanager/adddelegate(delegate:).md)
  Adds a delegate that receives callbacks about changes to the available conversation history.
- [func fetch(request: Predicate<ConversationHistoryManager.RecentConversation>) async throws -> [ConversationHistoryManager.RecentConversation]](conversationhistorymanager/fetch(request:).md)
  Queries the conversation history for conversations that match a given condition.
- [func markAsRead(recentConversations: [ConversationHistoryManager.RecentConversation]) async throws](conversationhistorymanager/markasread(recentconversations:).md)
  Marks the a list of conversations as read.


---

*[View on Apple Developer](https://developer.apple.com/documentation/livecommunicationkit/conversationhistorymanager/recentconversation)*