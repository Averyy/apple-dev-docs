# StartConversationAction

**Framework**: LiveCommunicationKit  
**Kind**: class

Starts an outgoing `Conversation` that will ring on remote member’s devices.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+
- visionOS 1.1+
- watchOS 10.4+

## Declaration

```swift
final class StartConversationAction
```

## Topics

### Initializers
- [init(conversationUUID: UUID, handles: [Handle], isVideo: Bool)](startconversationaction/init(conversationuuid:handles:isvideo:).md)
  Creates a new `StartConversationAction`.
### Instance Properties
- [let handles: [Handle]](startconversationaction/handles.md)
  The `Handle`s of all remote members who will be invited to join the `Conversation`.
- [let isVideo: Bool](startconversationaction/isvideo.md)
  Specifies if the `Conversation` contains a video stream.
### Instance Methods
- [func fulfill(dateStarted: Date)](startconversationaction/fulfill(datestarted:).md)
  Indicates that the action has been successfully executed.

## Relationships

### Inherits From
- [ConversationAction](conversationaction.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/livecommunicationkit/startconversationaction)*