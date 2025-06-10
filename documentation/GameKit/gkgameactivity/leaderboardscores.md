# leaderboardScores

**Framework**: GameKit  
**Kind**: property

All leaderboard scores that have been associated with this activity.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
var leaderboardScores: Set<GKLeaderboardScore> { get }
```

#### Discussion

Scores will be submitted to the leaderboards when the activity ends.

## See Also

- [func score(on: GKLeaderboard) -> GKLeaderboardScore?](gkgameactivity/score(on:).md)
  Get the leaderboard score from a specific leaderboard of the local player if previously set.
- [func setScore(on: GKLeaderboard, to: Int)](gkgameactivity/setscore(on:to:).md)
  Set a score of a leaderboard for a player.
- [func setScore(on: GKLeaderboard, to: Int, context: Int)](gkgameactivity/setscore(on:to:context:).md)
  Set a score of a leaderboard with a context for a player.
- [func removeScores(from: [GKLeaderboard])](gkgameactivity/removescores(from:).md)
  Removes all scores from leaderboards for a player if exist.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkgameactivity/leaderboardscores)*