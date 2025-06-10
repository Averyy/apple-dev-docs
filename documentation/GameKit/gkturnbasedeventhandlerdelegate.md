# GKTurnBasedEventHandlerDelegate

**Framework**: GameKit  
**Kind**: protocol

The [`GKTurnBasedEventHandlerDelegate`](gkturnbasedeventhandlerdelegate.md) protocol is implemented by an object to receive notifications events for turn-based matches. All methods are called on the main thread.

**Availability**:
- macOS 10.8+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
protocol GKTurnBasedEventHandlerDelegate
```

#### Overview

This protocol has been deprecated in iOS 7, use [`GKTurnBasedEventListener`](gkturnbasedeventlistener.md).

## Topics

### Receiving Turn-based Events
- [func handleInvite(fromGameCenter: [String])](gkturnbasedeventhandlerdelegate/handleinvite(fromgamecenter:).md)
  Sent to the delegate when the local player receives an invitation to join a new turn-based match.
- [func handleTurnEvent(for: GKTurnBasedMatch)](gkturnbasedeventhandlerdelegate/handleturnevent(for:).md)
  Sent to the delegate when it is the local player’s turn to act in a turn-based match.
- [func handleTurnEvent(for: GKTurnBasedMatch, didBecomeActive: Bool)](gkturnbasedeventhandlerdelegate/handleturnevent(for:didbecomeactive:).md)
  Sent to the delegate when it is the local player’s turn to act in a turn-based match.
- [func handleMatchEnded(GKTurnBasedMatch)](gkturnbasedeventhandlerdelegate/handlematchended(_:).md)
  Sent to the delegate when a match the local player is participating in has ended.

## See Also

- [protocol GKAchievementViewControllerDelegate](gkachievementviewcontrollerdelegate.md)
  An object implementing the [`GKAchievementViewControllerDelegate`](gkachievementviewcontrollerdelegate.md) protocol is called when the user dismisses the achievements view controller. Typically, this protocol is implemented by the object in your game that originally displayed the achievements user interface.
- [protocol GKChallengeEventHandlerDelegate](gkchallengeeventhandlerdelegate.md)
  You implement the [`GKChallengeEventHandlerDelegate`](gkchallengeeventhandlerdelegate.md) delegate to control how challenges are displayed in your game.
- [protocol GKChallengesViewControllerDelegate](gkchallengesviewcontrollerdelegate.md)
- [protocol GKChallengeListener](gkchallengelistener.md)
  An object that responds to challenge events.
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
- [protocol GKVoiceChatClient](gkvoicechatclient.md)
  The [`GKVoiceChatClient`](gkvoicechatclient.md) protocol is implemented to control the behavior of the [`GKVoiceChatService`](gkvoicechatservice.md) object. The voice chat client has a number of responsibilities:


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkturnbasedeventhandlerdelegate)*