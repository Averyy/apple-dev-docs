# ConversationHistoryManager.RecentConversation

**Framework**: LiveCommunicationKit  
**Kind**: struct

A structure that describes a recent conversation.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+

## Declaration

```swift
struct RecentConversation
```

## Topics

### Accessing conversation attributes
- [let date: Date](conversationhistorymanager/recentconversation/date.md)
  The point in time when the conversation started.
- [let direction: ConversationHistoryManager.RecentConversation.Direction](conversationhistorymanager/recentconversation/direction-swift.property.md)
  The direction of this conversation.
- [ConversationHistoryManager.RecentConversation.Direction](conversationhistorymanager/recentconversation/direction-swift.enum.md)
  Values that indicate whether a conversation was initiated or received.
- [let duration: TimeInterval](conversationhistorymanager/recentconversation/duration.md)
  The duration of the conversation from the time the system connected the participants.
- [let handles: [Handle]](conversationhistorymanager/recentconversation/handles.md)
  The handles of the conversation’s participants.
- [let isRead: Bool](conversationhistorymanager/recentconversation/isread.md)
  A value that indicates whether a person marked the recent conversation as read.
- [let status: ConversationHistoryManager.RecentConversation.Status](conversationhistorymanager/recentconversation/status-swift.property.md)
  The status of the conversation.
- [ConversationHistoryManager.RecentConversation.Status](conversationhistorymanager/recentconversation/status-swift.enum.md)
  Values that indicate the connection status of a recent conversation.
### Identifying a recent conversation
- [let id: UUID](conversationhistorymanager/recentconversation/id.md)
  The unique identifier of the recent conversation.

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Identifiable](../Swift/Identifiable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [func recentConversations(matching: Predicate<ConversationHistoryManager.RecentConversation>) async throws -> [ConversationHistoryManager.RecentConversation]](conversationhistorymanager/recentconversations(matching:).md)
  Returns a list of recent conversations that match the given predicate.
- [func markConversationAsRead(ConversationHistoryManager.RecentConversation) async throws](conversationhistorymanager/markconversationasread(_:).md)
  Marks a conversation as read.
- [func markConversationsAsRead([ConversationHistoryManager.RecentConversation]) async throws](conversationhistorymanager/markconversationsasread(_:).md)
  Marks the a list of conversations as read.


---

*[View on Apple Developer](https://developer.apple.com/documentation/livecommunicationkit/conversationhistorymanager/recentconversation)*