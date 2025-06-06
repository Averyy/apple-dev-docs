# PauseConversationAction

**Framework**: LiveCommunicationKit  
**Kind**: class

Pauses or unpauses a `Conversation`. Pausing a `Conversation` will stop all audio/video streams that apply to that `Conversation`.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+
- visionOS 1.1+
- watchOS 10.4+

## Declaration

```swift
final class PauseConversationAction
```

## Topics

### Initializers
- [init(conversationUUID: UUID, isPaused: Bool)](pauseconversationaction/init(conversationuuid:ispaused:).md)
  Creates a new `PauseConversationAction`.
### Instance Properties
- [let isPaused: Bool](pauseconversationaction/ispaused.md)
  Specifies if the `Conversation` should be paused upon execution of this action.

## Relationships

### Inherits From
- [ConversationAction](conversationaction.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/livecommunicationkit/pauseconversationaction)*