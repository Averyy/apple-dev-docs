# GKVoiceChatClient

**Framework**: GameKit  
**Kind**: protocol

The [`GKVoiceChatClient`](gkvoicechatclient.md) protocol is implemented to control the behavior of the [`GKVoiceChatService`](gkvoicechatservice.md) object. The voice chat client has a number of responsibilities:

**Availability**:
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
protocol GKVoiceChatClient : NSObjectProtocol
```

#### Overview

- Provides a network connection that the voice chat service uses to send and receive configuration data with other participants. If this network connection is shared with other application data, the client must also disambiguate between chat configuration data and application data.
- Provides a participant ID that identifies the user to remote participants in the chat.
- Defines how a remote user’s participant ID translates into a network connection to that user.
- Accepts or rejects requests from remote participants to join the voice chat.

## Topics

### Getting Information about the Participant
- [func participantID() -> String](gkvoicechatclient/participantid.md)
  Returns a string that uniquely identifies the local user.
### Sending data to other participants
- [func voiceChatService(GKVoiceChatService, send: Data, toParticipantID: String)](gkvoicechatclient/voicechatservice(_:send:toparticipantid:).md)
  A request for the client to send data to a participant.
- [func voiceChatService(GKVoiceChatService, sendRealTime: Data, toParticipantID: String)](gkvoicechatclient/voicechatservice(_:sendrealtime:toparticipantid:).md)
  Asks the client to send data to a participant that must get there quickly.
### Accepting Invitations from Remote Participants
- [func voiceChatService(GKVoiceChatService, didReceiveInvitationFromParticipantID: String, callID: Int)](gkvoicechatclient/voicechatservice(_:didreceiveinvitationfromparticipantid:callid:).md)
  Asks the client to accept or reject an invitation from a remote participant.
### Responding to Changes in Other Participants
- [func voiceChatService(GKVoiceChatService, didStartWithParticipantID: String)](gkvoicechatclient/voicechatservice(_:didstartwithparticipantid:).md)
  Received by the client when a voice chat with another participant is established.
- [func voiceChatService(GKVoiceChatService, didNotStartWithParticipantID: String, error: (any Error)?)](gkvoicechatclient/voicechatservice(_:didnotstartwithparticipantid:error:).md)
  Received by the client when an attempt to establish a voice chat with another participant failed.
- [func voiceChatService(GKVoiceChatService, didStopWithParticipantID: String, error: (any Error)?)](gkvoicechatclient/voicechatservice(_:didstopwithparticipantid:error:).md)
  Received by the client when a previously established voice chat has ended.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [protocol GKAchievementViewControllerDelegate](gkachievementviewcontrollerdelegate.md)
  An object implementing the [`GKAchievementViewControllerDelegate`](gkachievementviewcontrollerdelegate.md) protocol is called when the user dismisses the achievements view controller. Typically, this protocol is implemented by the object in your game that originally displayed the achievements user interface.
- [protocol GKChallengeEventHandlerDelegate](gkchallengeeventhandlerdelegate.md)
  You implement the [`GKChallengeEventHandlerDelegate`](gkchallengeeventhandlerdelegate.md) delegate to control how challenges are displayed in your game.
- [protocol GKChallengesViewControllerDelegate](gkchallengesviewcontrollerdelegate.md)
- [protocol GKFriendRequestComposeViewControllerDelegate](gkfriendrequestcomposeviewcontrollerdelegate.md)
  The [`GKFriendRequestComposeViewControllerDelegate`](gkfriendrequestcomposeviewcontrollerdelegate.md) protocol is implemented by delegates of the [`GKFriendRequestComposeViewController`](gkfriendrequestcomposeviewcontroller.md) class. The delegate is called when the player dismisses the friend request.
- [protocol GKGameSessionEventListener](gkgamesessioneventlistener.md)
  An event listener that handles game session events.
- [protocol GKLeaderboardViewControllerDelegate](gkleaderboardviewcontrollerdelegate.md)
  The [`GKLeaderboardViewControllerDelegate`](gkleaderboardviewcontrollerdelegate.md) protocol is implemented by delegates of the [`GKLeaderboardViewController`](gkleaderboardviewcontroller.md) class. The delegate is called when the player dismisses the leaderboard.
- [protocol GKPeerPickerControllerDelegate](gkpeerpickercontrollerdelegate.md)
  The [`GKPeerPickerControllerDelegate`](gkpeerpickercontrollerdelegate.md) protocol is implemented on an object to customize the behavior of a [`GKPeerPickerController`](gkpeerpickercontroller.md) object. The delegate is called by the peer picker to create a session object and to respond as the session is configured by the controller.
- [protocol GKSessionDelegate](gksessiondelegate.md)
  An object implements the [`GKSessionDelegate`](gksessiondelegate.md) protocol to control the behavior of a [`GKSession`](gksession.md) object. The delegate is called when other visible peers change their state relative to the session. It is also called to determine whether another peer is allowed to connect to the session.
- [protocol GKTurnBasedEventHandlerDelegate](gkturnbasedeventhandlerdelegate.md)
  The [`GKTurnBasedEventHandlerDelegate`](gkturnbasedeventhandlerdelegate.md) protocol is implemented by an object to receive notifications events for turn-based matches. All methods are called on the main thread.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkvoicechatclient)*