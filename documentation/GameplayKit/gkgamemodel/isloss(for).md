# isLoss(for:)

**Framework**: GameplayKit  
**Kind**: method  
**Role**: Instance Method

Returns a Boolean value indicating whether the specified player has lost the game.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.0+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
optional func isLoss(for player: any GKGameModelPlayer) -> Bool
```

```objc
- (BOOL) isLossForPlayer:(id<GKGameModelPlayer>) player;
```

## Return Value

[`true`](../../Swift/true.md) if this game model represents a losing state for the specified player; [`false`](../../Swift/false.md) if the game has been won or has not yet concluded.

## Discussion

If the game has been won or lost, a strategist evaluating the game model can avoid evaluating further moves in the game and can therefore plan a successful move more efficiently.

For some games, merely identifying winning and losing states of the game model and using a sufficiently large [`maxLookAheadDepth`](../gkminmaxstrategist/maxlookaheaddepth.md) value is enough for a strategist to play the game well. However, you can improve both the game performance and the runtime efficiency of move planning by also implementing the [`score(for:)`](./score%28for%29.md) method to distinguish the relative desirability of non-game-ending states.

> **Note**:  This method is optional; however, your game model class must implement at least one of the [`score(for:)`](./score%28for%29.md), [`isLoss(for:)`](./isloss%28for%29.md), and [`isWin(for:)`](./iswin%28for%29.md) methods.

## Parameters

- `player`: An instance of your game’s player class (a custom class implementing the [`GKGameModelPlayer`](../gkgamemodelplayer.md) protocol) representing the player evaluating the game model.

## See Also

### Evaluating a Game Model
- [func gameModelUpdates(for: any GKGameModelPlayer) -> [any GKGameModelUpdate]?](./gamemodelupdates%28for%29.md)
  Returns the set of moves available to the specified player.
- [func score(for: any GKGameModelPlayer) -> Int](./score%28for%29.md)
  Returns a number rating the desirability of the game model’s current state from the perspective of the specified player.
- [func isWin(for: any GKGameModelPlayer) -> Bool](./iswin%28for%29.md)
  Returns a Boolean value indicating whether the current state of the game model reflects a win for the specified player.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkgamemodel/isloss(for:))*