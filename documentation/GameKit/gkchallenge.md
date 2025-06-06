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

- [class GKScoreChallenge](gkscorechallenge.md)
  A type of challenge where a player must beat the leaderboard score of another player.
- [class GKAchievementChallenge](gkachievementchallenge.md)
  A type of challenge where a player must earn another player’s achievement.
- [protocol GKChallengeListener](gkchallengelistener.md)
  An object that responds to challenge events.
- [GKShowChallengeBanners](../BundleResources/Information-Property-List/GKShowChallengeBanners.md)
  A Boolean value that indicates whether GameKit can display challenge banners in a game.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkchallenge)*