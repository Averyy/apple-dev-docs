# unapplyGameModelUpdate(_:)

**Framework**: GameplayKit  
**Kind**: method

Updates the internal state of the game model to remove the effect of the specified changes.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.0+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
optional func unapplyGameModelUpdate(_ gameModelUpdate: any GKGameModelUpdate)
```

#### Discussion

This method is an optional counterpart to the [`apply(_:)`](gkgamemodel/apply(_:).md) method. By default, a GameplayKit strategist explores possible moves by copying the current game model, then calling that method to test the effect of a move. Copying a game model (see the [`setGameModel(_:)`](gkgamemodel/setgamemodel(_:).md) method) repeatedly can increase the time it takes for a strategist to evaluate moves. If your move class (adopting the [`GKGameModelUpdate`](gkgamemodelupdate.md) protocol) can describe not only how to perform a move, but also how to take back a move—leaving the game model in the same state it was before the move—implement the [`unapplyGameModelUpdate(_:)`](gkgamemodel/unapplygamemodelupdate(_:).md) method to undo moves. If you implement this method, the strategist can evaluate multiple moves without copying the game model, possibly increasing performance.

Some games naturally describe moves reversibly. For example, a Tic-Tac-Toe move class indicates which square to place a marker into, so unapplying that update would remove the marker from that square. To use this method in other games, however, you’ll need to design your move class carefully. For example, in a chess game, the move class would need to record both the original position and the destination position of a piece being moved, and either the move class or the game model class would need to track any pieces captured in that move so that they can be restored.

## Parameters

- `gameModelUpdate`: An instance of your custom class that implements the   protocol, describing a move to be revoked in your game.

## See Also

- [func apply(any GKGameModelUpdate)](gkgamemodel/apply(_:).md)
  Updates the internal state of the game model to reflect the specified changes.
- [func setGameModel(any GKGameModel)](gkgamemodel/setgamemodel(_:).md)
  Sets the game model’s internal state to that of the specified game model.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkgamemodel/unapplygamemodelupdate(_:))*