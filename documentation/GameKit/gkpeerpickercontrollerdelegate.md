# GKPeerPickerControllerDelegate

**Framework**: GameKit  
**Kind**: protocol  
**Role**: Protocol

The [`GKPeerPickerControllerDelegate`](./gkpeerpickercontrollerdelegate.md) protocol is implemented on an object to customize the behavior of a [`GKPeerPickerController`](./gkpeerpickercontroller.md) object. The delegate is called by the peer picker to create a session object and to respond as the session is configured by the controller.

**Availability**:
- iOS 3.0+ - Deprecated in 7.0
- iPadOS 3.0+ - Deprecated in 7.0
- Mac Catalyst 3.0+ - Deprecated in 7.0
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: Use MCBrowserViewController along with MCBrowserViewControllerDelegate from the MultipeerConnectivity framework.

## Declaration

```swift
protocol GKPeerPickerControllerDelegate : NSObjectProtocol
```

```objc
@protocol GKPeerPickerControllerDelegate <NSObject>
```

## Topics

### Creating a Session for the Peer Picker
- [func peerPickerController(GKPeerPickerController, didSelect: GKPeerPickerConnectionType)](./gkpeerpickercontrollerdelegate/peerpickercontroller%28_,didselect%29.md)
  Tells the delegate that the user selected a connection type.
- [func peerPickerController(GKPeerPickerController, sessionFor: GKPeerPickerConnectionType) -> GKSession](./gkpeerpickercontrollerdelegate/peerpickercontroller%28_,sessionfor%29.md)
  Asks the delegate to return a session for the specified connection type.
### Responding to Connection Messages
- [func peerPickerController(GKPeerPickerController, didConnectPeer: String, to: GKSession)](./gkpeerpickercontrollerdelegate/peerpickercontroller%28_,didconnectpeer,to%29.md)
  Tells the delegate that the controller connected a peer to the session.
### Responding When the User Cancels the Connection Attempt
- [func peerPickerControllerDidCancel(GKPeerPickerController)](./gkpeerpickercontrollerdelegate/peerpickercontrollerdidcancel%28_%29.md)
  Tells the delegate that the user canceled the connection attempt.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Deprecated protocols
- [protocol GKAchievementViewControllerDelegate](./gkachievementviewcontrollerdelegate.md)
  An object implementing the [`GKAchievementViewControllerDelegate`](./gkachievementviewcontrollerdelegate.md) protocol is called when the user dismisses the achievements view controller. Typically, this protocol is implemented by the object in your game that originally displayed the achievements user interface.
- [protocol GKChallengeEventHandlerDelegate](./gkchallengeeventhandlerdelegate.md)
  You implement the [`GKChallengeEventHandlerDelegate`](./gkchallengeeventhandlerdelegate.md) delegate to control how challenges are displayed in your game.
- [protocol GKChallengesViewControllerDelegate](./gkchallengesviewcontrollerdelegate.md)
- [protocol GKChallengeListener](./gkchallengelistener.md)
  An object that responds to challenge events.
- [protocol GKFriendRequestComposeViewControllerDelegate](./gkfriendrequestcomposeviewcontrollerdelegate.md)
  The [`GKFriendRequestComposeViewControllerDelegate`](./gkfriendrequestcomposeviewcontrollerdelegate.md) protocol is implemented by delegates of the [`GKFriendRequestComposeViewController`](./gkfriendrequestcomposeviewcontroller.md) class. The delegate is called when the player dismisses the friend request.
- [protocol GKGameSessionEventListener](./gkgamesessioneventlistener.md)
  An event listener that handles game session events.
- [protocol GKLeaderboardViewControllerDelegate](./gkleaderboardviewcontrollerdelegate.md)
  The [`GKLeaderboardViewControllerDelegate`](./gkleaderboardviewcontrollerdelegate.md) protocol is implemented by delegates of the [`GKLeaderboardViewController`](./gkleaderboardviewcontroller.md) class. The delegate is called when the player dismisses the leaderboard.
- [protocol GKSessionDelegate](./gksessiondelegate.md)
  An object implements the [`GKSessionDelegate`](./gksessiondelegate.md) protocol to control the behavior of a [`GKSession`](./gksession.md) object. The delegate is called when other visible peers change their state relative to the session. It is also called to determine whether another peer is allowed to connect to the session.
- [protocol GKTurnBasedEventHandlerDelegate](./gkturnbasedeventhandlerdelegate.md)
  The [`GKTurnBasedEventHandlerDelegate`](./gkturnbasedeventhandlerdelegate.md) protocol is implemented by an object to receive notifications events for turn-based matches. All methods are called on the main thread.
- [protocol GKVoiceChatClient](./gkvoicechatclient.md)
  The [`GKVoiceChatClient`](./gkvoicechatclient.md) protocol is implemented to control the behavior of the [`GKVoiceChatService`](./gkvoicechatservice.md) object. The voice chat client has a number of responsibilities:


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkpeerpickercontrollerdelegate)*