# GKChallengeEventHandlerDelegate

**Framework**: GameKit  
**Kind**: protocol  
**Role**: Protocol

You implement the [`GKChallengeEventHandlerDelegate`](./gkchallengeeventhandlerdelegate.md) delegate to control how challenges are displayed in your game.

**Availability**:
- iOS 6.0+ - Deprecated in 7.0
- iPadOS 6.0+ - Deprecated in 7.0
- Mac Catalyst 6.0+ - Deprecated in 7.0
- macOS 10.8+ - Deprecated in 10.10
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: You should instead implement the GKChallengeListener protocol and register a listener with GKLocalPlayer.

## Declaration

```swift
protocol GKChallengeEventHandlerDelegate : NSObjectProtocol
```

```objc
@protocol GKChallengeEventHandlerDelegate <NSObject>
```

#### Overview

By default, GameKit briefly displays a banner over your game when any of the following events occur:

- The local player receives a challenge.
- The local player completes a challenge.
- A remote player completes a challenge issued by the local player.

Your event handler can override or extend this behavior:

- It can prevent a banner from being displayed.
- It can be notified when a player taps in a banner.
- It can handle the events directly.

## Topics

### Detecting When a User Taps a Banner
- [func localPlayerDidSelect(GKChallenge!)](./gkchallengeeventhandlerdelegate/localplayerdidselect%28_%29.md)
  Called when the local player selects a challenge banner displayed by GameKit.
### Responding When a New Challenge is Received
- [func localPlayerDidReceive(GKChallenge!)](./gkchallengeeventhandlerdelegate/localplayerdidreceive%28_%29.md)
  Called when the local player receives a new challenge.
- [func shouldShowBanner(forLocallyReceivedChallenge: GKChallenge!) -> Bool](./gkchallengeeventhandlerdelegate/shouldshowbanner%28forlocallyreceivedchallenge%29.md)
  Called to determine whether a banner should be shown when the local player receives a challenge.
### Responding to Challenges Completed By the Local Player
- [func localPlayerDidComplete(GKChallenge!)](./gkchallengeeventhandlerdelegate/localplayerdidcomplete%28_%29.md)
  Called when the local player completes a challenge.
- [func shouldShowBanner(forLocallyCompletedChallenge: GKChallenge!) -> Bool](./gkchallengeeventhandlerdelegate/shouldshowbanner%28forlocallycompletedchallenge%29.md)
  Called to determine whether a banner should be shown when the local player completes a challenge.
### Responding to Challenges Issued by the Local Player
- [func remotePlayerDidComplete(GKChallenge!)](./gkchallengeeventhandlerdelegate/remoteplayerdidcomplete%28_%29.md)
  Called when a remote player completes a challenge issued by the local player.
- [func shouldShowBanner(forRemotelyCompletedChallenge: GKChallenge!) -> Bool](./gkchallengeeventhandlerdelegate/shouldshowbanner%28forremotelycompletedchallenge%29.md)
  Called to determine whether a banner should be shown when a remote player completes a challenge.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Deprecated protocols
- [protocol GKAchievementViewControllerDelegate](./gkachievementviewcontrollerdelegate.md)
  An object implementing the [`GKAchievementViewControllerDelegate`](./gkachievementviewcontrollerdelegate.md) protocol is called when the user dismisses the achievements view controller. Typically, this protocol is implemented by the object in your game that originally displayed the achievements user interface.
- [protocol GKChallengesViewControllerDelegate](./gkchallengesviewcontrollerdelegate.md)
- [protocol GKChallengeListener](./gkchallengelistener.md)
  An object that responds to challenge events.
- [protocol GKFriendRequestComposeViewControllerDelegate](./gkfriendrequestcomposeviewcontrollerdelegate.md)
  The [`GKFriendRequestComposeViewControllerDelegate`](./gkfriendrequestcomposeviewcontrollerdelegate.md) protocol is implemented by delegates of the [`GKFriendRequestComposeViewController`](./gkfriendrequestcomposeviewcontroller.md) class. The delegate is called when the player dismisses the friend request.
- [protocol GKGameSessionEventListener](./gkgamesessioneventlistener.md)
  An event listener that handles game session events.
- [protocol GKLeaderboardViewControllerDelegate](./gkleaderboardviewcontrollerdelegate.md)
  The [`GKLeaderboardViewControllerDelegate`](./gkleaderboardviewcontrollerdelegate.md) protocol is implemented by delegates of the [`GKLeaderboardViewController`](./gkleaderboardviewcontroller.md) class. The delegate is called when the player dismisses the leaderboard.
- [protocol GKPeerPickerControllerDelegate](./gkpeerpickercontrollerdelegate.md)
  The [`GKPeerPickerControllerDelegate`](./gkpeerpickercontrollerdelegate.md) protocol is implemented on an object to customize the behavior of a [`GKPeerPickerController`](./gkpeerpickercontroller.md) object. The delegate is called by the peer picker to create a session object and to respond as the session is configured by the controller.
- [protocol GKSessionDelegate](./gksessiondelegate.md)
  An object implements the [`GKSessionDelegate`](./gksessiondelegate.md) protocol to control the behavior of a [`GKSession`](./gksession.md) object. The delegate is called when other visible peers change their state relative to the session. It is also called to determine whether another peer is allowed to connect to the session.
- [protocol GKTurnBasedEventHandlerDelegate](./gkturnbasedeventhandlerdelegate.md)
  The [`GKTurnBasedEventHandlerDelegate`](./gkturnbasedeventhandlerdelegate.md) protocol is implemented by an object to receive notifications events for turn-based matches. All methods are called on the main thread.
- [protocol GKVoiceChatClient](./gkvoicechatclient.md)
  The [`GKVoiceChatClient`](./gkvoicechatclient.md) protocol is implemented to control the behavior of the [`GKVoiceChatService`](./gkvoicechatservice.md) object. The voice chat client has a number of responsibilities:


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkchallengeeventhandlerdelegate)*