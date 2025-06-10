# removeScores(from:)

**Framework**: GameKit  
**Kind**: method

Removes all scores from leaderboards for a player if exist.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
func removeScores(from leaderboards: [GKLeaderboard])
```

## See Also

- [var leaderboardScores: Set<GKLeaderboardScore>](gkgameactivity/leaderboardscores.md)
  All leaderboard scores that have been associated with this activity.
- [func score(on: GKLeaderboard) -> GKLeaderboardScore?](gkgameactivity/score(on:).md)
  Get the leaderboard score from a specific leaderboard of the local player if previously set.
- [func setScore(on: GKLeaderboard, to: Int)](gkgameactivity/setscore(on:to:).md)
  Set a score of a leaderboard for a player.
- [func setScore(on: GKLeaderboard, to: Int, context: Int)](gkgameactivity/setscore(on:to:context:).md)
  Set a score of a leaderboard with a context for a player.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkgameactivity/removescores(from:))*