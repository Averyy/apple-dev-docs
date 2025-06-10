# StartConversationAction

**Framework**: LiveCommunicationKit  
**Kind**: class

An action that starts an outgoing conversation and causes the devices of a remote participant to ring.

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

## Mentions

- [Initiating VoIP conversations with LiveCommunicationKit](initiating-voip-conversations-with-livecommunicationkit.md)

## Topics

### Creating a conversation action
- [init(conversationUUID: UUID, handles: [Handle], isVideo: Bool)](startconversationaction/init(conversationuuid:handles:isvideo:).md)
  Creates an action that starts an outgoing conversation.
### Accessing action attributes
- [let handles: [Handle]](startconversationaction/handles.md)
  The handles of all remote members who receive an invite  to join the conversation.
- [let isVideo: Bool](startconversationaction/isvideo.md)
  A value that specifies if the conversation contains a video stream.
### Completing actions
- [func fulfill(dateStarted: Date)](startconversationaction/fulfill(datestarted:).md)
  Indicates that a local participant successfully started a conversation.

## Relationships

### Inherits From
- [ConversationAction](conversationaction.md)

## See Also

- [class ConversationAction](conversationaction.md)
  A type that represents a VoIP action for a conversation.
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
- [class UnmergeConversationAction](unmergeconversationaction.md)
  An action that separates two previosuly merged conversations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/livecommunicationkit/startconversationaction)*