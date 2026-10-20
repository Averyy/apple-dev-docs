# setScore(on:to:)

**Framework**: GameKit  
**Kind**: method

Set a score of a leaderboard for a player.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
func setScore(on leaderboard: GKLeaderboard, to score: Int)
```

#### Discussion

The framewowrk submits the score to the leaderboard when the activity ends.

## See Also

- [var leaderboardScores: Set<GKLeaderboardScore>](gkgameactivity/leaderboardscores.md)
  All leaderboard scores that have been associated with this activity.
- [func score(on: GKLeaderboard) -> GKLeaderboardScore?](gkgameactivity/score(on:).md)
  Get the leaderboard score from a specific leaderboard of the local player if previously set.
- [func setScore(on: GKLeaderboard, to: Int, context: Int)](gkgameactivity/setscore(on:to:context:).md)
  Set a score of a leaderboard with a context for a player.
- [func removeScores(from: [GKLeaderboard])](gkgameactivity/removescores(from:).md)
  Removes all scores from leaderboards for a player if exist.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkgameactivity/setscore(on:to:))*