# EndConversationAction

**Framework**: LiveCommunicationKit  
**Kind**: class

Removes the local member from the specified `Conversation` and stops all audio/video streams, but doesn’t necessarily end the `Conversation` for remote members.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+
- visionOS 1.1+
- watchOS 10.4+

## Declaration

```swift
final class EndConversationAction
```

## Topics

### Initializers
- [init(conversationUUID: UUID)](endconversationaction/init(conversationuuid:).md)
  Creates a new `EndConversationAction`.
### Instance Methods
- [func fulfill(dateEnded: Date)](endconversationaction/fulfill(dateended:).md)
  Indicates that the action has been successfully executed.

## Relationships

### Inherits From
- [ConversationAction](conversationaction.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/livecommunicationkit/endconversationaction)*