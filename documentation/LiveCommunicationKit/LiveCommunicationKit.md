# LiveCommunicationKit

**Framework**: LiveCommunicationKit  
**Kind**: module

Initiate and handle VoIP conversations, coordinate them with other communication apps and the system, and get ready to be a default calling or dialer app.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+
- visionOS 1.1+
- watchOS 10.4+

#### Overview

LiveCommunicationKit allows you to offer VoIP conversation functionalities in your app, and to integrate your communication services with other communication apps in the system. With LiveCommunicationKit, your app can:

- Initiate and receive VoIP conversations
- Forward cellular network conversations to the system

Using LiveCommunicationKit in your app allows people to configure their device to use your app as the default dialer or calling app.

##### Manage User Privacy

With a person’s permission, an installed health research app that uses [`SensorKit`](https://developer.apple.com/documentation/SensorKit) entitlements may collect Speech Metrics data while your LiveCommunicationKit app is in use. To prevent this, set the [`SRResearchDataGeneration`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/SRResearchDataGeneration) information property list key to `NO`.

> ❗ **Important**: When someone starts a conversation in your app that uses LiveCommunicationKit, your app provides the contact information of the recipient to the system. The system may use that information to indicate communication with that person as a suggestion in the Journal app, or in other apps that use the [`Journaling Suggestions`](https://developer.apple.com/documentation/JournalingSuggestions) framework.

## Topics

### Essentials
- [Initiating VoIP conversations with LiveCommunicationKit](initiating-voip-conversations-with-livecommunicationkit.md)
  Let people initiate and receive VoIP conversations, and configure your app so it can be the default calling app on a person’s device.
- [Preparing your app to be the default dialer app](preparing-your-app-to-be-the-default-dialer-app.md)
  Let people configure their device to set your app as the default dialer app.
- [LiveCommunicationKit updates](../Updates/LiveCommunicationKit.md)
  Learn about important changes to LiveCommunicationKit.
### VoIP conversation management
- [class ConversationManager](conversationmanager.md)
  An interface for managing and observing VoIP conversations.
- [protocol ConversationManagerDelegate](conversationmanagerdelegate.md)
  Methods for managing conversations and receiving VoIP conversation updates.
- [class Conversation](conversation.md)
  A type that describes a video or audio conversation.
### VoIP conversation actions
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
- [class StartConversationAction](startconversationaction.md)
  An action that starts an outgoing conversation and causes the devices of a remote participant to ring.
- [class UnmergeConversationAction](unmergeconversationaction.md)
  An action that separates two previosuly merged conversations.
### Participant information
- [struct Handle](handle.md)
  A way to reach a participant, such as a phone number or email address.
### Conversation history
- [class ConversationHistoryManager](conversationhistorymanager.md)
  An interface for managing and providing conversation history.
- [protocol ConversationHistoryManagerDelegate](conversationhistorymanagerdelegate.md)
  Methods for receiving updates to the conversation history.
### Classes
- [class TelephonyConversationManager](telephonyconversationmanager.md)
### Structures
- [struct CellularService](cellularservice.md)
  Struct representing an account which can be used to dial a call
- [struct StartCellularConversationAction](startcellularconversationaction.md)
  Struct representing a request to dial a conversation using the default calling application


---

*[View on Apple Developer](https://developer.apple.com/documentation/LiveCommunicationKit)*