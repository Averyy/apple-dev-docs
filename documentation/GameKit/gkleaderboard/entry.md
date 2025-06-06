# GKLeaderboard.Entry

**Framework**: GameKit  
**Kind**: class

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

## Mentions

- [Encourage progress and competition with leaderboards](encourage-progress-and-competition-with-leaderboards.md)

## Topics

### Accessing Properties
- [var context: Int](gkleaderboard/entry/context.md)
  An integer value that your game uses.
- [var date: Date](gkleaderboard/entry/date.md)
  The date and time when the player earns the score.
- [var formattedScore: String](gkleaderboard/entry/formattedscore.md)
  The player’s score as a localized string.
- [var player: GKPlayer](gkleaderboard/entry/player.md)
  The player who earns the score.
- [var rank: Int](gkleaderboard/entry/rank.md)
  The position of the score in the results of a leaderboard search.
- [var score: Int](gkleaderboard/entry/score.md)
  The score that the player earns.
### Presenting Challenges
- [func challengeComposeController(withMessage: String?, players: [GKPlayer]?, completion: GKChallengeComposeHandler?) -> UIViewController](gkleaderboard/entry/challengecomposecontroller(withmessage:players:completion:).md)
  Provides a challenge compose view controller with preselected player identifiers and a preformatted, player-editable message.
- [typealias GKChallengeComposeHandler](gkchallengecomposehandler.md)
  A completion block that provides information about the player who issues a challenge and the players who receive it.
- [func challengeComposeController(withMessage: String?, players: [GKPlayer]?, completionHandler: GKChallengeComposeCompletionBlock?) -> UIViewController](gkleaderboard/entry/challengecomposecontroller(withmessage:players:completionhandler:).md)
  Provides a challenge compose view controller with preselected player identifiers and a preformatted, player-editable message.

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

- [func loadEntries(for: GKLeaderboard.PlayerScope, timeScope: GKLeaderboard.TimeScope, range: NSRange, completionHandler: (GKLeaderboard.Entry?, [GKLeaderboard.Entry]?, Int, (any Error)?) -> Void)](gkleaderboard/loadentries(for:timescope:range:completionhandler:).md)
  Returns the scores for the local player and other players for the specified type of player, time period, and ranks.
- [func loadEntries(for: [GKPlayer], timeScope: GKLeaderboard.TimeScope, completionHandler: (GKLeaderboard.Entry?, [GKLeaderboard.Entry]?, (any Error)?) -> Void)](gkleaderboard/loadentries(for:timescope:completionhandler:).md)
  Returns the scores for the local player and other players for the specified time period.
- [GKLeaderboard.PlayerScope](gkleaderboard/playerscope-swift.enum.md)
  Specifies the type of players for filtering data.
- [GKLeaderboard.TimeScope](gkleaderboard/timescope-swift.enum.md)
  Specifies the time period for filtering data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkleaderboard/entry)*