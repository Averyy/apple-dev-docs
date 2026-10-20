# ConversationHistoryManager.RecentConversation.Status

**Framework**: LiveCommunicationKit  
**Kind**: enum  
**Role**: Enumeration

Values that indicate the connection status of a recent conversation.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
enum Status
```

## Topics

### Connection status
- [ConversationHistoryManager.RecentConversation.Status.answeredElsewhere](./status-swift.enum/answeredelsewhere.md)
  The conversation was answered on another device.
- [ConversationHistoryManager.RecentConversation.Status.cancelled](./status-swift.enum/cancelled.md)
  The outgoing conversation was cancelled by the initiating participant before it was connected.
- [ConversationHistoryManager.RecentConversation.Status.connected](./status-swift.enum/connected.md)
  The conversation was connected on this device.
- [ConversationHistoryManager.RecentConversation.Status.missed](./status-swift.enum/missed.md)
  The receving participant didn’t answer the incoming conversation.
- [ConversationHistoryManager.RecentConversation.Status.unknown](./status-swift.enum/unknown.md)
  The conversation’s status is unknown.

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
- [ConversationHistoryManager.RecentConversation.Direction](./direction-swift.enum.md)
  Values that indicate whether a conversation was initiated or received.
- [let duration: TimeInterval](./duration.md)
  The duration of the conversation from the time the system connected the participants.
- [let handles: [Handle]](./handles.md)
  The handles of the conversation’s participants.
- [let isRead: Bool](./isread.md)
  A value that indicates whether a person marked the recent conversation as read.
- [let status: ConversationHistoryManager.RecentConversation.Status](./status-swift.property.md)
  The status of the conversation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/livecommunicationkit/conversationhistorymanager/recentconversation/status-swift.enum)*