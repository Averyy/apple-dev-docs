# ConversationHistoryManager.RecentConversation.Status

**Framework**: LiveCommunicationKit  
**Kind**: enum

Values that indicate the connection status of a recent conversation.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+

## Declaration

```swift
enum Status
```

## Topics

### Connection status
- [ConversationHistoryManager.RecentConversation.Status.answeredElsewhere](conversationhistorymanager/recentconversation/status-swift.enum/answeredelsewhere.md)
  The conversation was answered on another device.
- [ConversationHistoryManager.RecentConversation.Status.cancelled](conversationhistorymanager/recentconversation/status-swift.enum/cancelled.md)
  The outgoing conversation was cancelled by the initiating participant before it was connected.
- [ConversationHistoryManager.RecentConversation.Status.connected](conversationhistorymanager/recentconversation/status-swift.enum/connected.md)
  The conversation was connected on this device.
- [ConversationHistoryManager.RecentConversation.Status.missed](conversationhistorymanager/recentconversation/status-swift.enum/missed.md)
  The receving participant didn’t answer the incoming conversation.
- [ConversationHistoryManager.RecentConversation.Status.unknown](conversationhistorymanager/recentconversation/status-swift.enum/unknown.md)
  The conversation’s status is unknown.

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/livecommunicationkit/conversationhistorymanager/recentconversation/status-swift.enum)*