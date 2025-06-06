# activePlayer

**Framework**: GameplayKit  
**Kind**: property  
**Required**: Yes

The player whose turn it currently is in the game.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.0+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var activePlayer: (any GKGameModelPlayer)? { get }
```

#### Discussion

This player is responsible for the next move. GameplayKit assumes that the next call to the [`apply(_:)`](gkgamemodel/apply(_:).md) method will perform a move on behalf of this player.

## See Also

- [var players: [any GKGameModelPlayer]?](gkgamemodel/players.md)
  The players currently in the game.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkgamemodel/activeplayer)*