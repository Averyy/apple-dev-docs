# ConversationAction

**Framework**: LiveCommunicationKit  
**Kind**: class

A type that represents an action for a conversation.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+
- visionOS 1.1+
- watchOS 10.4+

## Declaration

```swift
class ConversationAction
```

## Topics

### Creating an action
- [convenience init(conversationUUID: UUID, timeoutDate: Date)](conversationaction/init(conversationuuid:timeoutdate:).md)
  Creates a conversation action.
### Completing actions
- [func fulfill()](conversationaction/fulfill.md)
  Reports that the action was successful.
- [func fail()](conversationaction/fail.md)
  Reports that performing the action failed.
### Accessing action attributes
- [var conversationUUID: UUID](conversationaction/conversationuuid.md)
  The unique identifier for the action’s associated conversation.
- [var uuid: UUID](conversationaction/uuid.md)
  The unique identifier that identifies the action.
- [var timeoutDate: Date](conversationaction/timeoutdate.md)
  The point in time that marks when the action can’t be completed anymore.
- [var state: ConversationAction.State](conversationaction/state-swift.property.md)
  The action’s current state.
- [ConversationAction.State](conversationaction/state-swift.enum.md)
  A type that describes the current state of a conversation action.

## Relationships

### Inherited By
- [EndConversationAction](endconversationaction.md)
- [JoinConversationAction](joinconversationaction.md)
- [MergeConversationAction](mergeconversationaction.md)
- [MuteConversationAction](muteconversationaction.md)
- [PauseConversationAction](pauseconversationaction.md)
- [PlayToneAction](playtoneaction.md)
- [SetTranslatingAction](settranslatingaction.md)
- [StartConversationAction](startconversationaction.md)
- [UnmergeConversationAction](unmergeconversationaction.md)

## See Also

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
- [class PlayToneAction](playtoneaction.md)
  An action that plays sequence of tones to indicate that a participant of a conversation interacted with the keypad.
- [class SetTranslatingAction](settranslatingaction.md)
  An action that starts or stops translation.
- [class StartConversationAction](startconversationaction.md)
  An action that starts an outgoing conversation and causes the devices of a remote participant to ring.
- [class UnmergeConversationAction](unmergeconversationaction.md)
  An action that separates two previosuly merged conversations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/livecommunicationkit/conversationaction)*