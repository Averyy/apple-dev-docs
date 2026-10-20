# GKSessionDelegate

**Framework**: GameKit  
**Kind**: protocol  
**Role**: Protocol

An object implements the [`GKSessionDelegate`](./gksessiondelegate.md) protocol to control the behavior of a [`GKSession`](./gksession.md) object. The delegate is called when other visible peers change their state relative to the session. It is also called to determine whether another peer is allowed to connect to the session.

**Availability**:
- iOS 3.0+ - Deprecated in 7.0
- iPadOS 3.0+ - Deprecated in 7.0
- Mac Catalyst 3.0+ - Deprecated in 7.0
- macOS 10.8+ - Deprecated in 10.10
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 2.0+ - Deprecated in 2.0

## Declaration

```swift
protocol GKSessionDelegate : NSObjectProtocol
```

```objc
@protocol GKSessionDelegate <NSObject>
```

## Topics

### Observing Changes to Peers
- [func session(GKSession, peer: String, didChange: GKPeerConnectionState)](./gksessiondelegate/session%28_,peer,didchange%29.md)
  Received by the delegate when a peer changes state.
### Connection Requests from Other Peers
- [func session(GKSession, didReceiveConnectionRequestFromPeer: String)](./gksessiondelegate/session%28_,didreceiveconnectionrequestfrompeer%29.md)
  Received by the delegate when a remote peer wants to create a connection to the session.
### Connection Errors
- [func session(GKSession, connectionWithPeerFailed: String, withError: any Error)](./gksessiondelegate/session%28_,connectionwithpeerfailed,witherror%29.md)
  Received by the delegate when an attempt to connect to another peer failed.
- [func session(GKSession, didFailWithError: any Error)](./gksessiondelegate/session%28_,didfailwitherror%29.md)
  Sent to the delegate when a serious error has occurred in the session.

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
- [protocol GKPeerPickerControllerDelegate](./gkpeerpickercontrollerdelegate.md)
  The [`GKPeerPickerControllerDelegate`](./gkpeerpickercontrollerdelegate.md) protocol is implemented on an object to customize the behavior of a [`GKPeerPickerController`](./gkpeerpickercontroller.md) object. The delegate is called by the peer picker to create a session object and to respond as the session is configured by the controller.
- [protocol GKTurnBasedEventHandlerDelegate](./gkturnbasedeventhandlerdelegate.md)
  The [`GKTurnBasedEventHandlerDelegate`](./gkturnbasedeventhandlerdelegate.md) protocol is implemented by an object to receive notifications events for turn-based matches. All methods are called on the main thread.
- [protocol GKVoiceChatClient](./gkvoicechatclient.md)
  The [`GKVoiceChatClient`](./gkvoicechatclient.md) protocol is implemented to control the behavior of the [`GKVoiceChatService`](./gkvoicechatservice.md) object. The voice chat client has a number of responsibilities:


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gksessiondelegate)*