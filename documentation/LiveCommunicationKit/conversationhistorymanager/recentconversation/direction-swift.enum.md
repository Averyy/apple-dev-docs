# ConversationHistoryManager.RecentConversation.Direction

**Framework**: LiveCommunicationKit  
**Kind**: enum  
**Role**: Enumeration

Values that indicate whether a conversation was initiated or received.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
enum Direction
```

## Topics

### Conversation direction
- [ConversationHistoryManager.RecentConversation.Direction.incoming](./direction-swift.enum/incoming.md)
  The conversation was received by the local participant.
- [ConversationHistoryManager.RecentConversation.Direction.outgoing](./direction-swift.enum/outgoing.md)
  The conversation was initiated by the local participant.

## Relationships

### Conforms To
- [Decodable](../../../Swift/decodable.md)
- [Encodable](../../../Swift/encodable.md)
- [Equatable](../../../Swift/equatable.md)
- [Hashable](../../../Swift/hashable.md)
- [Sendable](../../../Swift/sendable.md)
- [SendableMetatype](../../../Swift/sendablemetatype.md)

## See Also

### Accessing conversation attributes
- [let date: Date](./date.md)
  The point in time when the conversation started.
- [let direction: ConversationHistoryManager.RecentConversation.Direction](./direction-swift.property.md)
  The direction of this conversation.
- [let duration: TimeInterval](./duration.md)
  The duration of the conversation from the time the system connected the participants.
- [let handles: [Handle]](./handles.md)
  The handles of the conversation’s participants.
- [let isRead: Bool](./isread.md)
  A value that indicates whether a person marked the recent conversation as read.
- [let status: ConversationHistoryManager.RecentConversation.Status](./status-swift.property.md)
  The status of the conversation.
- [ConversationHistoryManager.RecentConversation.Status](./status-swift.enum.md)
  Values that indicate the connection status of a recent conversation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/livecommunicationkit/conversationhistorymanager/recentconversation/direction-swift.enum)*