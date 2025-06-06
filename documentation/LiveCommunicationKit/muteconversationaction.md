# MuteConversationAction

**Framework**: LiveCommunicationKit  
**Kind**: class

Mutes or unmutes `Conversation`. Muting a `Conversation` means that the local member will not be heard by any remote members.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+
- visionOS 1.1+
- watchOS 10.4+

## Declaration

```swift
final class MuteConversationAction
```

## Topics

### Initializers
- [init(conversationUUID: UUID, isMuted: Bool)](muteconversationaction/init(conversationuuid:ismuted:).md)
  Creates a new `MuteConversationAction`.
### Instance Properties
- [let isMuted: Bool](muteconversationaction/ismuted.md)
  Specifies if the `Conversation` should be muted or unmuted upon execution of this action.

## Relationships

### Inherits From
- [ConversationAction](conversationaction.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/livecommunicationkit/muteconversationaction)*