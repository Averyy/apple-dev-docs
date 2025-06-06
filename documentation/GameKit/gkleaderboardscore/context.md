# context

**Framework**: GameKit  
**Kind**: property

An integer value that your game uses.

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
var context: Int { get set }
```

#### Discussion

Game Center stores this custom game-specific property for you. It allows you to associate an arbitrary 64-bit unsigned integer value with the score data that you report to Game Center. You decide how to interpret this integer value in your game.

## See Also

- [var leaderboardID: String](gkleaderboardscore/leaderboardid.md)
  The ID that Game Center uses for the leaderboard.
- [var player: GKPlayer](gkleaderboardscore/player.md)
  The player who earns the score.
- [var value: Int](gkleaderboardscore/value.md)
  The score that the player earns.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkleaderboardscore/context)*