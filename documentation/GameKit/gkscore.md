# GKScore

**Framework**: GameKit  
**Kind**: class

An object containing information for a score that was earned by the player.

**Availability**:
- iOS 4.1+
- iPadOS 4.1+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
class GKScore
```

#### Overview

> ❗ **Important**:  Your game must initialize a local player before you can use any Game Center classes. If there is no initialized player, your game receives a [`GKError.Code.notAuthenticated`](gkerror/code/notauthenticated.md) error. For more information, see [`Authenticating a player`](authenticating-a-player.md).

Your game creates `GKScore` objects to post scores to a leaderboard on Game Center. When your game retrieves score information from a leaderboard, those scores are returned as `GKScore` objects.

Scores and leaderboards work together to help you create a better game. Whenever a new `GKScore` object is created, it is associated with a leaderboard. You must ensure that the score being sent to a leaderboard is compatible with the leaderboard scoring format set in App Store Connect. See [`Leaderboards and Leaderboard Sets`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/LanguagesUtilities/Conceptual/iTunesConnectGameCenter_Guide/Leaderboards/Leaderboards.html#//apple_ref/doc/uid/TP40013726-CH2) for information on how to create a leaderboard in App Store Connect.

To report a score to Game Center, your game allocates and initializes a new object, sets the [`value`](gkscore/value.md) property to the score the player earned, and then calls the [`report(completionHandler:)`](gkscore/report(completionhandler:).md) method. The mechanism your game uses to calculate scores is up to you to design; scores are only compared within your game.

## Topics

### Reporting a New Score
- [class func report([GKLeaderboardScore], withEligibleChallenges: [GKChallenge], withCompletionHandler: (((any Error)?) -> Void)?)](gkscore/report(_:witheligiblechallenges:withcompletionhandler:)-2tycl.md)
  Submits a list of scores and all eligible challenges.
- [class func report([GKScore], withCompletionHandler: (((any Error)?) -> Void)?)](gkscore/report(_:withcompletionhandler:).md)
  Reports a list of scores to Game Center
- [class func report([GKScore], withEligibleChallenges: [GKChallenge], withCompletionHandler: (((any Error)?) -> Void)?)](gkscore/report(_:witheligiblechallenges:withcompletionhandler:)-3c5lh.md)
  Submits a list of scores and all eligible challenges.
### Issuing a Score Challenge
- [func challengeComposeController(withMessage: String?, players: [GKPlayer]?, completion: GKChallengeComposeHandler?) -> UIViewController](gkscore/challengecomposecontroller(withmessage:players:completion:).md)
  Provides a challenge compose view controller with preselected player identifiers and a preformatted, player-editable message.
- [typealias GKChallengeComposeHandler](gkchallengecomposehandler.md)
  A completion block that provides information about the player who issues a challenge and the players who receive it.
- [func challengeComposeController(withMessage: String?, players: [GKPlayer]?, completionHandler: GKChallengeComposeCompletionBlock?) -> UIViewController](gkscore/challengecomposecontroller(withmessage:players:completionhandler:).md)
  Provides a challenge compose view controller with pre-selected player identifiers and a preformatted, player-editable message.
- [func challengeComposeController(withPlayers: [String]?, message: String?, completionHandler: GKChallengeComposeCompletionBlock?) -> UIViewController?](gkscore/challengecomposecontroller(withplayers:message:completionhandler:).md)
  Provides a challenge compose view controller with pre-selected player identifiers and a preformatted, player-editable message.
### Deprecated Methods and Properties
- [var category: String?](gkscore/category.md)
  The leaderboard that this score belongs to.
- [var context: UInt64](gkscore/context.md)
  An integer value used by your game.
- [var date: Date](gkscore/date.md)
  The date and time when the score was earned.
- [var formattedValue: String?](gkscore/formattedvalue.md)
  Returns the player’s score as a localized string.
- [var leaderboardIdentifier: String](gkscore/leaderboardidentifier.md)
  The identifier for the leaderboard.
- [var player: GKPlayer](gkscore/player.md)
  The player who earned the score.
- [var rank: Int](gkscore/rank.md)
  The position of the score in the results of a leaderboard search.
- [var value: Int64](gkscore/value.md)
  The score earned by the player.
- [var shouldSetDefaultLeaderboard: Bool](gkscore/shouldsetdefaultleaderboard.md)
  A Boolean value that indicates whether this score should also update the default leaderboard.
- [init(leaderboardIdentifier: String)](gkscore/init(leaderboardidentifier:).md)
  Returns an initialized score object using the local player and the current date.
- [init(leaderboardIdentifier: String, player: GKPlayer)](gkscore/init(leaderboardidentifier:player:).md)
  Returns an initialized score object for the specified leaderboard and player.
- [init(category: String?)](gkscore/init(category:).md)
  Returns an initialized score object.
- [init?(leaderboardIdentifier: String, forPlayer: String)](gkscore/init(leaderboardidentifier:forplayer:).md)
  Returns an initialized score object for the specified leaderboard and player.
- [func issueChallenge(toPlayers: [String]?, message: String?)](gkscore/issuechallenge(toplayers:message:).md)
  Issues a score challenge to a set of players.
- [var playerID: String?](gkscore/playerid.md)
  The player identifier for the player that earned the score.
- [func report(completionHandler: (((any Error)?) -> Void)?)](gkscore/report(completionhandler:).md)
  Reports a score to Game Center.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
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
- [class GKSession](gksession.md)
  A [`GKSession`](gksession.md) object provides the ability to discover and connect to nearby iOS devices using Bluetooth or Wi-fi.
- [class GKTurnBasedEventHandler](gkturnbasedeventhandler.md)
  The [`GKTurnBasedEventHandler`](gkturnbasedeventhandler.md) class is used to respond to important messages related to turn-based matches. To use it, call the [`shared()`](gkturnbasedeventhandler/shared().md) class method to get the singleton instance and assign an object that implements the [`GKTurnBasedEventHandlerDelegate`](gkturnbasedeventhandlerdelegate.md) protocol to its [`delegate`](gkturnbasedeventhandler/delegate.md) property. All methods are called on the main thread.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkscore)*