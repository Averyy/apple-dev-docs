# players

**Framework**: GameKit  
**Kind**: property

The players that join the match.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var players: [GKPlayer] { get }
```

## Mentions

- [Assigning players to teams using rules](assigning-players-to-teams-using-rules.md)

#### Discussion

This property includes all players except the local player.

## See Also

- [var expectedPlayerCount: Int](gkmatch/expectedplayercount.md)
  The remaining number of players invited but not yet connected to the match.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkmatch/players)*