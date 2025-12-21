# ConversationHistoryManager.RecentConversation.Direction

**Framework**: LiveCommunicationKit  
**Kind**: enum

Values that indicate whether a conversation was initiated or received.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+

## Declaration

```swift
enum Direction
```

## Topics

### Conversation direction
- [ConversationHistoryManager.RecentConversation.Direction.incoming](conversationhistorymanager/recentconversation/direction-swift.enum/incoming.md)
  The conversation was received by the local participant.
- [ConversationHistoryManager.RecentConversation.Direction.outgoing](conversationhistorymanager/recentconversation/direction-swift.enum/outgoing.md)
  The conversation was initiated by the local participant.

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

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
- [let status: ConversationHistoryManager.RecentConversation.Status](conversationhistorymanager/recentconversation/status-swift.property.md)
  The status of the conversation.
- [ConversationHistoryManager.RecentConversation.Status](conversationhistorymanager/recentconversation/status-swift.enum.md)
  Values that indicate the connection status of a recent conversation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/livecommunicationkit/conversationhistorymanager/recentconversation/direction-swift.enum)*