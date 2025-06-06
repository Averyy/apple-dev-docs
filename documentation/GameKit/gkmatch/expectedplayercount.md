# expectedPlayerCount

**Framework**: GameKit  
**Kind**: property

The remaining number of players invited but not yet connected to the match.

**Availability**:
- iOS 4.1+
- iPadOS 4.1+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var expectedPlayerCount: Int { get }
```

## Mentions

- [Exchanging data between players in real-time games](exchanging-data-between-players-in-real-time-games.md)

#### Discussion

GameKit decrements the value of this property when a player connects to the match. When the value reaches `0`, all expected players joined, and the game can begin.

## See Also

- [var players: [GKPlayer]](gkmatch/players.md)
  The players that join the match.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkmatch/expectedplayercount)*