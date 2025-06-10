# GKChallenge

**Framework**: GameKit  
**Kind**: class

A challenge issued by the local player to another player.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
class GKChallenge
```

#### Overview

Players can use Game Center to challenge other players to beat their scores and achievements that they earn in your game. When a player issues a challenge to another player, Game Center sends a push notification to the other player. That player can then accept or refuse the challenge. If the player accepts the challenge, Game Center adds the challenge to the player’s list of challenges. Later, if the player beats the challenge, Game Center notifies both players.

Game Center supports two kinds of challenges:

You never subclass the [`GKChallenge`](gkchallenge.md) class directly. However, you can subclass [`GKScoreChallenge`](gkscorechallenge.md) or [`GKAchievementChallenge`](gkachievementchallenge.md) to create specific kinds of challenges.

##### Enable Challenges

You must enable challenges for your game in App Store Connect before you can use the challenges features. For details, see [`Enable challenges`](https://developer.apple.comhttps://developer.apple.com/help/app-store-connect/configure-game-center/enable-challenges/) in App Store Connect Help.

##### Load and Issue Challenges

You can load the challenges issued by the local player using the [`loadReceivedChallenges(completionHandler:)`](gkchallenge/loadreceivedchallenges(completionhandler:).md) class method. You can issue challenges with the player’s permission using the [`challengeComposeController(withMessage:players:completion:)`](gkscore/challengecomposecontroller(withmessage:players:completion:).md) method in the [`GKLeaderboard.Entry`](gkleaderboard/entry.md), [`GKScore`](gkscore.md), or [`GKAchievement`](gkachievement.md) class.

## Topics

### Retrieving the List of Challenges to the Local Player
- [class func loadReceivedChallenges(completionHandler: (([GKChallenge]?, (any Error)?) -> Void)?)](gkchallenge/loadreceivedchallenges(completionhandler:).md)
  Loads the list of outstanding challenges.
### Examining Details about a Challenge
- [var issuingPlayer: GKPlayer?](gkchallenge/issuingplayer.md)
  The player who issues the challenge.
- [var receivingPlayer: GKPlayer?](gkchallenge/receivingplayer.md)
  The player who receives the challenge.
- [var message: String?](gkchallenge/message.md)
  A text message that describes the challenge.
- [var state: GKChallengeState](gkchallenge/state.md)
  The current state of the challenge.
- [enum GKChallengeState](gkchallengestate.md)
  The state of a challenge.
- [var issueDate: Date](gkchallenge/issuedate.md)
  The date the player issued the challenge.
- [var completionDate: Date?](gkchallenge/completiondate.md)
  The date the challenged player completed the challenge.
### Declining a Challenge
- [func decline()](gkchallenge/decline.md)
  Declines a challenge that another player issues to the local player.
### Deprecated symbols
- [var issuingPlayerID: String?](gkchallenge/issuingplayerid.md)
  The player who issues the challenge.
- [var receivingPlayerID: String?](gkchallenge/receivingplayerid.md)
  The player who receives the challenge.
- [typealias GKChallengeComposeCompletionBlock](gkchallengecomposecompletionblock.md)
  A completion block that provides information about the player who issues a challenge and the players who receive it.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [GKAchievementChallenge](gkachievementchallenge.md)
- [GKScoreChallenge](gkscorechallenge.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)

## See Also

- [class GKAchievementViewController](gkachievementviewcontroller.md)
  An `GKAchievementViewController` object provides a standard user interface to display achievement progress for the local player. If the [`GKGameCenterViewController`](gkgamecenterviewcontroller.md) class is available, you should use it instead.
- [class GKChallengeEventHandler](gkchallengeeventhandler.md)
  The `GKChallengeEventHandler` class is used to respond to events related to challenges sent or received by the local player.
- [class GKChallengesViewController](gkchallengesviewcontroller.md)
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkchallenge)*