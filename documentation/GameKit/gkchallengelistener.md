# GKChallengeListener

**Framework**: GameKit  
**Kind**: protocol

An object that responds to challenge events.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
protocol GKChallengeListener : NSObjectProtocol
```

#### Overview

Your game can ignore a challenge, start up in a specific state so the local player can respond to a challenge, or notify the challenger when the local player completes a challenge.

Don’t implement [`GKChallengeListener`](gkchallengelistener.md) directly; instead use [`GKLocalPlayerListener`](gklocalplayerlistener.md). The [`GKLocalPlayerListener`](gklocalplayerlistener.md) protocol inherits methods from [`GKChallengeListener`](gkchallengelistener.md), [`GKInviteEventListener`](gkinviteeventlistener.md), [`GKSavedGameListener`](gksavedgamelistener.md), and [`GKTurnBasedEventListener`](gkturnbasedeventlistener.md) in order to handle multiple events.

## Topics

### Responding to a Challenge
- [func player(GKPlayer, didReceive: GKChallenge)](gkchallengelistener/player(_:didreceive:).md)
  Handles when the local player issues a challenge but the other player doesn’t want to respond immediately.
- [func player(GKPlayer, wantsToPlay: GKChallenge)](gkchallengelistener/player(_:wantstoplay:).md)
  Handles when the local player issues a challenge and the other player accepts.
### Completing a Challenge
- [func player(GKPlayer, didComplete: GKChallenge, issuedByFriend: GKPlayer)](gkchallengelistener/player(_:didcomplete:issuedbyfriend:).md)
  Handles when the local player completes a challenge that a friend issues.
- [func player(GKPlayer, issuedChallengeWasCompleted: GKChallenge, byFriend: GKPlayer)](gkchallengelistener/player(_:issuedchallengewascompleted:byfriend:).md)
  Handles when a friend completes a challenge that the local player issues.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
### Inherited By
- [GKLocalPlayerListener](gklocalplayerlistener.md)

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
- [protocol GKVoiceChatClient](gkvoicechatclient.md)
  The [`GKVoiceChatClient`](gkvoicechatclient.md) protocol is implemented to control the behavior of the [`GKVoiceChatService`](gkvoicechatservice.md) object. The voice chat client has a number of responsibilities:


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkchallengelistener)*