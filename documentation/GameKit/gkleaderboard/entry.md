# GKLeaderboard.Entry

**Framework**: GameKit  
**Kind**: class  
**Role**: Class

Information about a single score by a player on a leaderboard.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
class Entry
```

```objc
@interface GKLeaderboardEntry : NSObject
```

## Mentions

- [Encourage progress and competition with leaderboards](../encourage-progress-and-competition-with-leaderboards.md)

## Topics

### Accessing Properties
- [var context: Int](./entry/context.md)
  An integer value that your game uses.
- [var date: Date](./entry/date.md)
  The date and time when the player earns the score.
- [var formattedScore: String](./entry/formattedscore.md)
  The player’s score as a localized string.
- [var player: GKPlayer](./entry/player.md)
  The player who earns the score.
- [var rank: Int](./entry/rank.md)
  The position of the score in the results of a leaderboard search.
- [var score: Int](./entry/score.md)
  The score that the player earns.
### Presenting Challenges
- [func challengeComposeController(withMessage: String?, players: [GKPlayer]?, completion: GKChallengeComposeHandler?) -> UIViewController](./entry/challengecomposecontroller%28withmessage,players,completion%29.md)
  Provides a challenge compose view controller with preselected player identifiers and a preformatted, player-editable message.
- [typealias GKChallengeComposeHandler](../gkchallengecomposehandler.md)
  A completion block that provides information about the player who issues a challenge and the players who receive it.
- [func challengeComposeController(withMessage: String?, players: [GKPlayer]?, completionHandler: GKChallengeComposeCompletionBlock?) -> UIViewController](./entry/challengecomposecontroller%28withmessage,players,completionhandler%29.md)
  Provides a challenge compose view controller with preselected player identifiers and a preformatted, player-editable message.

## Relationships

### Inherits From
- [NSObject](../../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../../Swift/cvararg.md)
- [CustomDebugStringConvertible](../../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../../Swift/customstringconvertible.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [NSObjectProtocol](../../ObjectiveC/nsobjectprotocol.md)

## See Also

### Loading Scores
- [func loadEntries(for: GKLeaderboard.PlayerScope, timeScope: GKLeaderboard.TimeScope, range: NSRange, completionHandler: (GKLeaderboard.Entry?, [GKLeaderboard.Entry]?, Int, (any Error)?) -> Void)](./loadentries%28for,timescope,range,completionhandler%29.md)
  Returns the scores for the local player and other players for the specified type of player, time period, and ranks.
- [func loadEntries(for: [GKPlayer], timeScope: GKLeaderboard.TimeScope, completionHandler: (GKLeaderboard.Entry?, [GKLeaderboard.Entry]?, (any Error)?) -> Void)](./loadentries%28for,timescope,completionhandler%29.md)
  Returns the scores for the local player and other players for the specified time period.
- [GKLeaderboard.PlayerScope](./playerscope-swift.enum.md)
  Specifies the type of players for filtering data.
- [GKLeaderboard.TimeScope](./timescope-swift.enum.md)
  Specifies the time period for filtering data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkleaderboard/entry)*