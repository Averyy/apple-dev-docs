# leaderboardScores

**Framework**: GameKit  
**Kind**: property  
**Role**: Instance Property

All leaderboard scores that have been associated with this activity.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
var leaderboardScores: Set<GKLeaderboardScore> { get }
```

```objc
@property (nonatomic, copy, readonly) NSSet<GKLeaderboardScore *> * leaderboardScores;
```

#### Discussion

Scores will be submitted to the leaderboards when the activity ends.

## See Also

### Getting and removing leaderboard scores
- [func score(on: GKLeaderboard) -> GKLeaderboardScore?](./score%28on%29.md)
  Get the leaderboard score from a specific leaderboard of the local player if previously set.
- [func setScore(on: GKLeaderboard, to: Int)](./setscore%28on,to%29.md)
  Set a score of a leaderboard for a player.
- [func setScore(on: GKLeaderboard, to: Int, context: Int)](./setscore%28on,to,context%29.md)
  Set a score of a leaderboard with a context for a player.
- [func removeScores(from: [GKLeaderboard])](./removescores%28from%29.md)
  Removes all scores from leaderboards for a player if exist.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkgameactivity/leaderboardscores)*