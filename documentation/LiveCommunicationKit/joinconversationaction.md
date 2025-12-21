# JoinConversationAction

**Framework**: LiveCommunicationKit  
**Kind**: class

An action for joining an incoming conversation.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+
- visionOS 1.1+
- watchOS 10.4+

## Declaration

```swift
final class JoinConversationAction
```

#### Overview

The incoming conversation might be currently ringing on a person’s device.

## Topics

### Creating a conversation action
- [init(conversationUUID: UUID)](joinconversationaction/init(conversationuuid:).md)
  Creates an action for joining an incoming conversation.
### Completing actions
- [func fulfill(dateConnected: Date)](joinconversationaction/fulfill(dateconnected:).md)
  Indicates that the local participant successfully joined an incoming conversation.

## Relationships

### Inherits From
- [ConversationAction](conversationaction.md)

## See Also

- [class ConversationAction](conversationaction.md)
  A type that represents an action for a conversation.
- [class EndConversationAction](endconversationaction.md)
  An action that removes the local participant from a conversation and stops all audio and video streams.
- [class MergeConversationAction](mergeconversationaction.md)
  An action that merges two separate conversations into one conversation.
- [class MuteConversationAction](muteconversationaction.md)
  An action that mutes or unmutes a conversation.
- [class PauseConversationAction](pauseconversationaction.md)
  An action that stops or restarts all audio and video streams for a conversation.
- [class PlayToneAction](playtoneaction.md)
  An action that plays sequence of tones to indicate that a participant of a conversation interacted with the keypad.
- [class SetTranslatingAction](settranslatingaction.md)
  An action that starts or stops translation.
- [class StartConversationAction](startconversationaction.md)
  An action that starts an outgoing conversation and causes the devices of a remote participant to ring.
- [class UnmergeConversationAction](unmergeconversationaction.md)
  An action that separates two previosuly merged conversations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/livecommunicationkit/joinconversationaction)*