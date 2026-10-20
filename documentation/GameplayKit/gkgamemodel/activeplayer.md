# activePlayer

**Framework**: GameplayKit  
**Kind**: property  
**Role**: Instance Property  
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

```objc
@property (nonatomic, readonly, nullable) id<GKGameModelPlayer> activePlayer;
```

#### Discussion

This player is responsible for the next move. GameplayKit assumes that the next call to the [`apply(_:)`](./apply%28_%29.md) method will perform a move on behalf of this player.

## See Also

### Keeping Track of Players
- [var players: [any GKGameModelPlayer]?](./players.md)
  The players currently in the game.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkgamemodel/activeplayer)*