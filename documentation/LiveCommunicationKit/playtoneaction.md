# PlayToneAction

**Framework**: LiveCommunicationKit  
**Kind**: class

An action that plays sequence of tones to indicate that a participant of a conversation interacted with the keypad.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+
- visionOS 1.1+
- watchOS 10.4+

## Declaration

```swift
final class PlayToneAction
```

#### Overview

The action can apply to local and remote members in a conversation.

## Topics

### Creating a conversation action
- [init(conversationUUID: UUID, digits: String, tone: PlayToneAction.Tone)](playtoneaction/init(conversationuuid:digits:tone:).md)
  Creates an action that plays a sequence of tones that indicate an interaction with the keypad.
### Accessing action attributes
- [let digits: String](playtoneaction/digits.md)
  The digits tapped by the user into the keypad or included in the dial string.
- [let tone: PlayToneAction.Tone](playtoneaction/tone-swift.property.md)
  The keypad tone to play.
- [PlayToneAction.Tone](playtoneaction/tone-swift.enum.md)
  Values that describe keypad tones.

## Relationships

### Inherits From
- [ConversationAction](conversationaction.md)

## See Also

- [class ConversationAction](conversationaction.md)
  A type that represents an action for a conversation.
- [class EndConversationAction](endconversationaction.md)
  An action that removes the local participant from a conversation and stops all audio and video streams.
- [class JoinConversationAction](joinconversationaction.md)
  An action for joining an incoming conversation.
- [class MergeConversationAction](mergeconversationaction.md)
  An action that merges two separate conversations into one conversation.
- [class MuteConversationAction](muteconversationaction.md)
  An action that mutes or unmutes a conversation.
- [class PauseConversationAction](pauseconversationaction.md)
  An action that stops or restarts all audio and video streams for a conversation.
- [class SetTranslatingAction](settranslatingaction.md)
  An action that starts or stops translation.
- [class StartConversationAction](startconversationaction.md)
  An action that starts an outgoing conversation and causes the devices of a remote participant to ring.
- [class UnmergeConversationAction](unmergeconversationaction.md)
  An action that separates two previosuly merged conversations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/livecommunicationkit/playtoneaction)*