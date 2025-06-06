# GKLeaderboardScore

**Framework**: GameKit  
**Kind**: class

Information about a player’s score on a leaderboard.

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
class GKLeaderboardScore
```

#### Overview

A [`GKLeaderboardScore`](gkleaderboardscore.md) object represents a score on a leaderboard for scores you report for challenges or turn-based games.

When you create a [`GKLeaderboardScore`](gkleaderboardscore.md) object, set the `leaderboardID` property to the associated leaderboard, the `player` property to the player who earns the score, and the `value` property to the score. Make sure the score is compatible with the score format that you configure in App Store Connect.

Then use either the [`report(_:withEligibleChallenges:withCompletionHandler:)`](gkscore/report(_:witheligiblechallenges:withcompletionhandler:)-2tycl.md) or [`endMatchInTurn(withMatch:leaderboardScores:achievements:completionHandler:)`](gkturnbasedmatch/endmatchinturn(withmatch:leaderboardscores:achievements:completionhandler:).md) `GKTurnBasedMatch` method to report one or more scores.

For details about the score format, see [`Configure leaderboards`](https://developer.apple.comhttps://developer.apple.com/help/app-store-connect/configure-game-center/configure-leaderboards) in App Store Connect Help.

## Topics

### Accessing Properties
- [var context: Int](gkleaderboardscore/context.md)
  An integer value that your game uses.
- [var leaderboardID: String](gkleaderboardscore/leaderboardid.md)
  The ID that Game Center uses for the leaderboard.
- [var player: GKPlayer](gkleaderboardscore/player.md)
  The player who earns the score.
- [var value: Int](gkleaderboardscore/value.md)
  The score that the player earns.

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
- [Sendable](../Swift/Sendable.md)

## See Also

- [Encourage progress and competition with leaderboards](encourage-progress-and-competition-with-leaderboards.md)
  Let players measure their own progress and compare their skills with friends and others.
- [Creating recurring leaderboards](creating-recurring-leaderboards.md)
  Create a leaderboard for your game that ranks player scores based on a schedule.
- [Adding Recurring Leaderboards to Your Game](adding-recurring-leaderboards-to-your-game.md)
  Encourage competition in your games by adding leaderboards that have a duration and repeat.
- [class GKLeaderboard](gkleaderboard.md)
  A leaderboard for a game that Game Center stores.
- [class GKLeaderboardSet](gkleaderboardset.md)
  Organizes leaderboards into logical and coherent groups.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkleaderboardscore)*