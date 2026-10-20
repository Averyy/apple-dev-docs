# ConversationHistoryManager.RecentConversation

**Framework**: LiveCommunicationKit  
**Kind**: struct  
**Role**: Structure

A structure that describes a recent conversation.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
struct RecentConversation
```

## Topics

### Accessing conversation attributes
- [let date: Date](./recentconversation/date.md)
  The point in time when the conversation started.
- [let direction: ConversationHistoryManager.RecentConversation.Direction](./recentconversation/direction-swift.property.md)
  The direction of this conversation.
- [ConversationHistoryManager.RecentConversation.Direction](./recentconversation/direction-swift.enum.md)
  Values that indicate whether a conversation was initiated or received.
- [let duration: TimeInterval](./recentconversation/duration.md)
  The duration of the conversation from the time the system connected the participants.
- [let handles: [Handle]](./recentconversation/handles.md)
  The handles of the conversation’s participants.
- [let isRead: Bool](./recentconversation/isread.md)
  A value that indicates whether a person marked the recent conversation as read.
- [let status: ConversationHistoryManager.RecentConversation.Status](./recentconversation/status-swift.property.md)
  The status of the conversation.
- [ConversationHistoryManager.RecentConversation.Status](./recentconversation/status-swift.enum.md)
  Values that indicate the connection status of a recent conversation.
### Identifying a recent conversation
- [let id: UUID](./recentconversation/id.md)
  The unique identifier of the recent conversation.

## Relationships

### Conforms To
- [Decodable](../../Swift/decodable.md)
- [Encodable](../../Swift/encodable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [Identifiable](../../Swift/identifiable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Managing recent conversations
- [func recentConversations(matching: Predicate<ConversationHistoryManager.RecentConversation>) async throws -> [ConversationHistoryManager.RecentConversation]](./recentconversations%28matching%29.md)
  Returns a list of recent conversations that match the given predicate.
- [func markConversationAsRead(ConversationHistoryManager.RecentConversation) async throws](./markconversationasread%28_%29.md)
  Marks a conversation as read.
- [func markConversationsAsRead([ConversationHistoryManager.RecentConversation]) async throws](./markconversationsasread%28_%29.md)
  Marks the a list of conversations as read.


---

*[View on Apple Developer](https://developer.apple.com/documentation/livecommunicationkit/conversationhistorymanager/recentconversation)*