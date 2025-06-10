# ConversationHistoryManager.RecentConversation.Direction

**Framework**: LiveCommunicationKit  
**Kind**: enum

Values that indicate whether a conversation was initiated or received.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
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
### Operators
- [static func == (ConversationHistoryManager.RecentConversation.Direction, ConversationHistoryManager.RecentConversation.Direction) -> Bool](conversationhistorymanager/recentconversation/direction-swift.enum/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Instance Properties
- [var hashValue: Int](conversationhistorymanager/recentconversation/direction-swift.enum/hashvalue.md)
  The hash value.
### Instance Methods
- [func hash(into: inout Hasher)](conversationhistorymanager/recentconversation/direction-swift.enum/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Default Implementations
- [Equatable Implementations](conversationhistorymanager/recentconversation/direction-swift.enum/equatable-implementations.md)

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
- [ConversationHistoryManager.RecentConversation.ConnectedStatus](conversationhistorymanager/recentconversation/connectedstatus.md)
  Values that indicate the connection status of a recent conversation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/livecommunicationkit/conversationhistorymanager/recentconversation/direction-swift.enum)*