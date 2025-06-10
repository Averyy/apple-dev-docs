# setScore(on:to:context:)

**Framework**: GameKit  
**Kind**: method

Set a score of a leaderboard with a context for a player.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
func setScore(on leaderboard: GKLeaderboard, to score: Int, context: Int)
```

## Mentions

- [Creating activities for your game](creating-activities-for-your-game.md)

#### Discussion

The score will be submitted to the leaderboard when the activity ends.

## See Also

- [var leaderboardScores: Set<GKLeaderboardScore>](gkgameactivity/leaderboardscores.md)
  All leaderboard scores that have been associated with this activity.
- [func score(on: GKLeaderboard) -> GKLeaderboardScore?](gkgameactivity/score(on:).md)
  Get the leaderboard score from a specific leaderboard of the local player if previously set.
- [func setScore(on: GKLeaderboard, to: Int)](gkgameactivity/setscore(on:to:).md)
  Set a score of a leaderboard for a player.
- [func removeScores(from: [GKLeaderboard])](gkgameactivity/removescores(from:).md)
  Removes all scores from leaderboards for a player if exist.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkgameactivity/setscore(on:to:context:))*