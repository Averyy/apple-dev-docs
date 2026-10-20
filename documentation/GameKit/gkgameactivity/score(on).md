# score(on:)

**Framework**: GameKit  
**Kind**: method  
**Role**: Instance Method

Get the leaderboard score from a specific leaderboard of the local player if previously set.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
func score(on leaderboard: GKLeaderboard) -> GKLeaderboardScore?
```

```objc
- (GKLeaderboardScore *) getScoreOnLeaderboard:(GKLeaderboard *) leaderboard;
```

## See Also

### Getting and removing leaderboard scores
- [var leaderboardScores: Set<GKLeaderboardScore>](./leaderboardscores.md)
  All leaderboard scores that have been associated with this activity.
- [func setScore(on: GKLeaderboard, to: Int)](./setscore%28on,to%29.md)
  Set a score of a leaderboard for a player.
- [func setScore(on: GKLeaderboard, to: Int, context: Int)](./setscore%28on,to,context%29.md)
  Set a score of a leaderboard with a context for a player.
- [func removeScores(from: [GKLeaderboard])](./removescores%28from%29.md)
  Removes all scores from leaderboards for a player if exist.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkgameactivity/score(on:))*