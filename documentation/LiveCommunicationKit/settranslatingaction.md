# SetTranslatingAction

**Framework**: LiveCommunicationKit  
**Kind**: class

An action that starts or stops translation.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+

## Declaration

```swift
final class SetTranslatingAction
```

#### Overview

To avoid interrupting or impeding call translation when a person mutes their audio during a conversation, don’t deactivate the upstream audio. Instead, mute your app’s audio input using [`MuteConversationAction`](muteconversationaction.md) and keep the upstream audio active to allow translated audio to flow when a person mutes the hardware microphone.

## Topics

### Creating a conversation action
- [init(conversationID: UUID, isTranslating: Bool, localLanguage: Locale.Language, remoteLanguage: Locale.Language)](settranslatingaction/init(conversationid:istranslating:locallanguage:remotelanguage:).md)
  Creates an action that starts or stops translation.
### Accessing action attributes
- [let isTranslating: Bool](settranslatingaction/istranslating.md)
  A value that indicates whether to start or stop translation.
- [let localLanguage: Locale.Language](settranslatingaction/locallanguage.md)
  The local participant’s language.
- [let remoteLanguage: Locale.Language](settranslatingaction/remotelanguage.md)
  The remote participant’s language.
### Completing a translation
- [func fulfill(using: SetTranslatingAction.TranslationEngine)](settranslatingaction/fulfill(using:).md)
  Reports that the translation action was successful.
- [SetTranslatingAction.TranslationEngine](settranslatingaction/translationengine.md)
  Values that describe the translation engine that provided a translation.

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
- [class PlayToneAction](playtoneaction.md)
  An action that plays sequence of tones to indicate that a participant of a conversation interacted with the keypad.
- [class StartConversationAction](startconversationaction.md)
  An action that starts an outgoing conversation and causes the devices of a remote participant to ring.
- [class UnmergeConversationAction](unmergeconversationaction.md)
  An action that separates two previosuly merged conversations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/livecommunicationkit/settranslatingaction)*