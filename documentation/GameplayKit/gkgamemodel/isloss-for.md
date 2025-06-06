# isLoss(for:)

**Framework**: Gameplaykit  
**Kind**: method

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

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if this game model represents a losing state for the specified player; [`false`](https://developer.apple.com/documentation/swift/false) if the game has been won or has not yet concluded.

#### Discussion

If the game has been won or lost, a strategist evaluating the game model can avoid evaluating further moves in the game and can therefore plan a successful move more efficiently.

For some games, merely identifying winning and losing states of the game model and using a sufficiently large [`maxLookAheadDepth`](gkminmaxstrategist/maxlookaheaddepth.md) value is enough for a strategist to play the game well. However, you can improve both the game performance and the runtime efficiency of move planning by also implementing the [`score(for:)`](gkgamemodel/score(for:).md) method to distinguish the relative desirability of non-game-ending states.

> **Note**:  This method is optional; however, your game model class must implement at least one of the [`score(for:)`](gkgamemodel/score(for:).md), [`isLoss(for:)`](gkgamemodel/isloss(for:).md), and [`isWin(for:)`](gkgamemodel/iswin(for:).md) methods.

## Parameters

- `player`: An instance of your game’s player class (a custom class implementing the   protocol) representing the player evaluating the game model.

## See Also

- [func gameModelUpdates(for: any GKGameModelPlayer) -> [any GKGameModelUpdate]?](gkgamemodel/gamemodelupdates(for:).md)
  Returns the set of moves available to the specified player.
- [func score(for: any GKGameModelPlayer) -> Int](gkgamemodel/score(for:).md)
  Returns a number rating the desirability of the game model’s current state from the perspective of the specified player.
- [func isWin(for: any GKGameModelPlayer) -> Bool](gkgamemodel/iswin(for:).md)
  Returns a Boolean value indicating whether the current state of the game model reflects a win for the specified player.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkgamemodel/isloss(for:))*