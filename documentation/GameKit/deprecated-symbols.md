# Deprecated symbols

**Framework**: GameKit

Review unsupported symbols and their replacements.

## Topics

### Deprecated classes
- [class GKAchievementViewController](gkachievementviewcontroller.md)
  An `GKAchievementViewController` object provides a standard user interface to display achievement progress for the local player. If the [`GKGameCenterViewController`](gkgamecenterviewcontroller.md) class is available, you should use it instead.
- [class GKChallengeEventHandler](gkchallengeeventhandler.md)
  The `GKChallengeEventHandler` class is used to respond to events related to challenges sent or received by the local player.
- [class GKChallengesViewController](gkchallengesviewcontroller.md)
- [class GKChallenge](gkchallenge.md)
  A challenge issued by the local player to another player.
- [class GKScoreChallenge](gkscorechallenge.md)
  A type of challenge where a player must beat the leaderboard score of another player.
- [class GKAchievementChallenge](gkachievementchallenge.md)
  A type of challenge where a player must earn another player’s achievement.
- [class GKCloudPlayer](gkcloudplayer.md)
  The object representing the currently signed-in iCloud user.
- [class GKGameCenterViewController](gkgamecenterviewcontroller.md)
  The dashboard that allows players to access their Game Center data in your game.
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
- [class GKNotificationBanner](gknotificationbanner.md)
  A Game Center-style banner that displays a message to the local player.
### Deprecated protocols
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
- [protocol GKTurnBasedEventHandlerDelegate](gkturnbasedeventhandlerdelegate.md)
  The [`GKTurnBasedEventHandlerDelegate`](gkturnbasedeventhandlerdelegate.md) protocol is implemented by an object to receive notifications events for turn-based matches. All methods are called on the main thread.
- [protocol GKVoiceChatClient](gkvoicechatclient.md)
  The [`GKVoiceChatClient`](gkvoicechatclient.md) protocol is implemented to control the behavior of the [`GKVoiceChatService`](gkvoicechatservice.md) object. The voice chat client has a number of responsibilities:
### Deprecated structures
- [struct GKVoiceChatServiceError](gkvoicechatserviceerror-swift.struct.md)
- [struct GKSessionError](gksessionerror-swift.struct.md)
- [struct GKGameSessionError](gkgamesessionerror.md)
  Error codes for the game session domain.
### Deprecated constants
- [let GKGameSessionErrorDomain: String](gkgamesessionerrordomain.md)
  The error domain for game sessions.
- [let GKSessionErrorDomain: String](gksessionerrordomain.md)
  An error occurred in [`GKSession`](gksession.md).
- [let GKVoiceChatServiceErrorDomain: String](gkvoicechatserviceerrordomain.md)
  An error occurred in [`GKVoiceChatService`](gkvoicechatservice.md).
### Deprecated enumerations
- [GKGameSessionError.Code](gkgamesessionerror/code.md)
  Error codes for the game session domain.
- [enum GKPeerConnectionState](gkpeerconnectionstate.md)
  The state of a peer known to the session.
- [enum GKPeerPickerConnectionType](gkpeerpickerconnectiontype.md)
  Network connections available to the peer picker dialog.
- [enum GKSendDataMode](gksenddatamode.md)
  The mechanism used to transmit data to other peers.
- [GKSessionError.Code](gksessionerror-swift.struct/code.md)
  Error codes for the session error domain.
- [struct GKSessionError](gksessionerror-swift.struct.md)
- [enum GKSessionMode](gksessionmode.md)
  Modes that determine how a session interacts with other peers.
- [GKVoiceChatServiceError.Code](gkvoicechatserviceerror-swift.struct/code.md)
  Error codes for the voice chat service error domain.
- [struct GKVoiceChatServiceError](gkvoicechatserviceerror-swift.struct.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/deprecated-symbols)*