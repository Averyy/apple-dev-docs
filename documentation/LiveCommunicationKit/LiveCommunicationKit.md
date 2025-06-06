# LiveCommunicationKit

**Framework**: LiveCommunicationKit  
**Kind**: module

## Topics

### Classes
- [class Conversation](conversation.md)
  A VoIP conversation.
- [class ConversationAction](conversationaction.md)
  A programmatic interface for objects that represent a VoIP action associated with a `Conversation`.
- [class ConversationManager](conversationmanager.md)
  A programmatic interface for interacting with and observing conversations.
- [class EndConversationAction](endconversationaction.md)
  Removes the local member from the specified `Conversation` and stops all audio/video streams, but doesn’t necessarily end the `Conversation` for remote members.
- [class JoinConversationAction](joinconversationaction.md)
  Joins an incoming `Conversation` that may be currently ringing on the user’s device.
- [class MergeConversationAction](mergeconversationaction.md)
  This action is used to merge 2 separate `Conversation`s into 1.
- [class MuteConversationAction](muteconversationaction.md)
  Mutes or unmutes `Conversation`. Muting a `Conversation` means that the local member will not be heard by any remote members.
- [class PauseConversationAction](pauseconversationaction.md)
  Pauses or unpauses a `Conversation`. Pausing a `Conversation` will stop all audio/video streams that apply to that `Conversation`.
- [class PlayToneAction](playtoneaction.md)
  Plays a sequence of tones to indicate local or remote member keypad entry.
- [class StartConversationAction](startconversationaction.md)
  Starts an outgoing `Conversation` that will ring on remote member’s devices.
- [class UnmergeConversationAction](unmergeconversationaction.md)
  This action is used to unmerge 2 previosuly-merged `Conversation`s into separate `Conversation`s again.
### Protocols
- [protocol ConversationManagerDelegate](conversationmanagerdelegate.md)
### Structures
- [struct Handle](handle.md)
  Uniquely identifies a member in a `Conversation`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/LiveCommunicationKit)*