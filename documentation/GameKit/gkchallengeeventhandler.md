# GKChallengeEventHandler

**Framework**: GameKit  
**Kind**: class

The `GKChallengeEventHandler` class is used to respond to events related to challenges sent or received by the local player.

**Availability**:
- macOS 10.8+
- visionOS 1.0+

## Declaration

```swift
class GKChallengeEventHandler
```

#### Overview

> ❗ **Important**:  Your game must authenticate a local player before you can use any Game Center classes. If there is no authenticated player, your game receives a [`GKError.Code.notAuthenticated`](gkerror/code/notauthenticated.md) error. For more information, see [`Authenticating a player`](authenticating-a-player.md).

 Your game must authenticate a local player before you can use any Game Center classes. If there is no authenticated player, your game receives a [`GKError.Code.notAuthenticated`](gkerror/code/notauthenticated.md) error. For more information, see [`Authenticating a player`](authenticating-a-player.md).

To use it, call the [`challengeEventHandler`](gkchallengeeventhandler/challengeeventhandler.md) class method to get the [`Singleton`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Singleton.html#//apple_ref/doc/uid/TP40008195-CH49) instance and assign an object that implements the [`GKChallengeEventHandlerDelegate`](gkchallengeeventhandlerdelegate.md) protocol to its [`delegate`](gkchallengeeventhandler/delegate.md) property. You should assign a challenge event handler immediately after the local player has been authenticated, because your game may have been launched in response to a challenge notification being received by the player.

## Topics

### Getting and Setting the Delegate
- [var delegate: (any GKChallengeEventHandlerDelegate)!](gkchallengeeventhandler/delegate.md)
  The delegate for the event handler.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class GKAchievementViewController](gkachievementviewcontroller.md)
  An `GKAchievementViewController` object provides a standard user interface to display achievement progress for the local player. If the [`GKGameCenterViewController`](gkgamecenterviewcontroller.md) class is available, you should use it instead.
- [class GKChallengesViewController](gkchallengesviewcontroller.md)
- [class GKCloudPlayer](gkcloudplayer.md)
  The object representing the currently signed-in iCloud user.
- [class GKGameSession](gkgamesession.md)
  A game session you can use to save game data, invite other players, and create turn-based and real-time game apps.
- [class GKGameSessionSharingViewController](gkgamesessionsharingviewcontroller.md)
  A user interface you can use to invite other users into a tvOS game session.
- [class GKFriendRequestComposeViewController](gkfriendrequestcomposeviewcontroller.md)
  Your game uses the `GKFriendRequestComposeViewController` class to present a screen that allows the local player to send friend requests to other players.
- [class GKLeaderboardViewController](gkleaderboardviewcontroller.md)
  The `GKLeaderboardViewController` class provides a standard user interface that displays leaderboard scores to the player. If the [`GKGameCenterViewController`](gkgamecenterviewcontroller.md) class is available, you should use it instead.
- [class GKPeerPickerController](gkpeerpickercontroller.md)
  Provides a standard user interface to allow one iOS device to discover and connect to another.
- [class GKScore](gkscore.md)
  An object containing information for a score that was earned by the player.
- [class GKSession](gksession.md)
  A [`GKSession`](gksession.md) object provides the ability to discover and connect to nearby iOS devices using Bluetooth or Wi-fi.
- [class GKTurnBasedEventHandler](gkturnbasedeventhandler.md)
  The [`GKTurnBasedEventHandler`](gkturnbasedeventhandler.md) class is used to respond to important messages related to turn-based matches. To use it, call the [`shared()`](gkturnbasedeventhandler/shared().md) class method to get the singleton instance and assign an object that implements the [`GKTurnBasedEventHandlerDelegate`](gkturnbasedeventhandlerdelegate.md) protocol to its [`delegate`](gkturnbasedeventhandler/delegate.md) property. All methods are called on the main thread.
- [class GKVoiceChat](gkvoicechat.md)
  A voice channel that allows players to speak with each other in a multiplayer game.
- [class GKVoiceChatService](gkvoicechatservice.md)
  The [`GKVoiceChatService`](gkvoicechatservice.md) class allows your application to connect two iOS devices into a voice chat.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkchallengeeventhandler)*