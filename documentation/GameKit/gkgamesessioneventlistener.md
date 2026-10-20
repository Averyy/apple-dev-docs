# GKGameSessionEventListener

**Framework**: GameKit  
**Kind**: protocol  
**Role**: Protocol

An event listener that handles game session events.

**Availability**:
- iOS 10.0+ - Deprecated in 12.0
- iPadOS 10.0+ - Deprecated in 12.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.12+ - Deprecated in 10.14
- tvOS 10.0+ - Deprecated in 12.0
- visionOS 1.0+ - Deprecated in 1.0

## Declaration

```swift
protocol GKGameSessionEventListener : NSObjectProtocol
```

```objc
@protocol GKGameSessionEventListener <NSObject>
```

## Topics

### Changing Player Status
- [func session(GKGameSession, didAdd: GKCloudPlayer)](./gkgamesessioneventlistener/session%28_,didadd%29.md)
  Tells the listener a new player has been added to a game session.
- [func session(GKGameSession, didRemove: GKCloudPlayer)](./gkgamesessioneventlistener/session%28_,didremove%29.md)
  Tells the listener a player left a game session.
- [func session(GKGameSession, player: GKCloudPlayer, didChange: GKConnectionState)](./gkgamesessioneventlistener/session%28_,player,didchange%29.md)
  Tells the listener a player’s connection state has changed.
- [enum GKConnectionState](./gkconnectionstate.md)
  Possible connection states for a player
### Transferring Data
- [func session(GKGameSession, didReceive: Data, from: GKCloudPlayer)](./gkgamesessioneventlistener/session%28_,didreceive,from%29.md)
  Tells the listener the player received data from another player.
- [func session(GKGameSession, didReceiveMessage: String, with: Data, from: GKCloudPlayer)](./gkgamesessioneventlistener/session%28_,didreceivemessage,with,from%29.md)
  Tells the listener a player has received a message from another player.
- [func session(GKGameSession, player: GKCloudPlayer, didSave: Data)](./gkgamesessioneventlistener/session%28_,player,didsave%29.md)
  Tells the listener data was saved by a player.

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

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkgamesessioneventlistener)*