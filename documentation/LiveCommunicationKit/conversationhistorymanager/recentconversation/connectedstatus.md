# ConversationHistoryManager.RecentConversation.ConnectedStatus

**Framework**: LiveCommunicationKit  
**Kind**: enum

Values that indicate the connection status of a recent conversation.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+

## Declaration

```swift
enum ConnectedStatus
```

## Topics

### Connection status
- [ConversationHistoryManager.RecentConversation.ConnectedStatus.answeredElsewhere](conversationhistorymanager/recentconversation/connectedstatus/answeredelsewhere.md)
  The conversation was answered on another device.
- [ConversationHistoryManager.RecentConversation.ConnectedStatus.cancelled](conversationhistorymanager/recentconversation/connectedstatus/cancelled.md)
  The outgoing conversation was cancelled by the initiating participant before it was connected.
- [ConversationHistoryManager.RecentConversation.ConnectedStatus.connected](conversationhistorymanager/recentconversation/connectedstatus/connected.md)
  The conversation was connected on this device.
- [ConversationHistoryManager.RecentConversation.ConnectedStatus.missed](conversationhistorymanager/recentconversation/connectedstatus/missed.md)
  The receving participant didn’t answer the incoming conversation.
- [ConversationHistoryManager.RecentConversation.ConnectedStatus.unknown](conversationhistorymanager/recentconversation/connectedstatus/unknown.md)
  The conversation’s status is unknown.
### Operators
- [static func == (ConversationHistoryManager.RecentConversation.ConnectedStatus, ConversationHistoryManager.RecentConversation.ConnectedStatus) -> Bool](conversationhistorymanager/recentconversation/connectedstatus/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Instance Properties
- [var hashValue: Int](conversationhistorymanager/recentconversation/connectedstatus/hashvalue.md)
  The hash value.
### Instance Methods
- [func hash(into: inout Hasher)](conversationhistorymanager/recentconversation/connectedstatus/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Default Implementations
- [Equatable Implementations](conversationhistorymanager/recentconversation/connectedstatus/equatable-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)

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
- [let status: ConversationHistoryManager.RecentConversation.ConnectedStatus](conversationhistorymanager/recentconversation/status.md)
  The status of the conversation.
- [ConversationHistoryManager.RecentConversation.Direction](conversationhistorymanager/recentconversation/direction-swift.enum.md)
  Values that indicate whether a conversation was initiated or received.


---

*[View on Apple Developer](https://developer.apple.com/documentation/livecommunicationkit/conversationhistorymanager/recentconversation/connectedstatus)*