# gameModelUpdates(for:)

**Framework**: GameplayKit  
**Kind**: method  
**Required**: Yes

Returns the set of moves available to the specified player.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.0+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func gameModelUpdates(for player: any GKGameModelPlayer) -> [any GKGameModelUpdate]?
```

#### Return Value

An array of instances of your game’s move class (a custom class implementing the [`GKGameModelUpdate`](gkgamemodelupdate.md) protocol), each representing a possible move for the specified player.

#### Discussion

Your implementation of the [`GKGameModelUpdate`](gkgamemodelupdate.md) protocol, or , should add properties or methods that describe a move in terms of your game. In this method, you create one instance of your move class for each move currently allowed to the specified player, filling in each instance’s custom properties with the information that describes that move. GameplayKit calls this method to speculate about possible future moves and their effects, using a copy of the active game board.

For example, in a Tic-Tac-Toe game, the move class would identify which of the nine spaces on the board to place a mark in. Your [`gameModelUpdates(for:)`](gkgamemodel/gamemodelupdates(for:).md) method would create an instance of the move class for each space not already marked. Your implementation should also take into account whether any moves are possible at all—if the game has already been won or has resulted in a draw, this method should return `nil`.

This method should return `nil` if the specified player is not valid or if no moves are available to that player.

> **Note**:  If the current game model represents an end state for the game—that is, if one player has won, or if the game has resulted in a draw—return `nil` to indicate that the strategist should not attempt to plan further moves.

## Parameters

- `player`: An instance of your game’s player class (a custom class implementing the   protocol) representing the player whose moves are to be evaluated.

## See Also

- [func score(for: any GKGameModelPlayer) -> Int](gkgamemodel/score(for:).md)
  Returns a number rating the desirability of the game model’s current state from the perspective of the specified player.
- [func isLoss(for: any GKGameModelPlayer) -> Bool](gkgamemodel/isloss(for:).md)
  Returns a Boolean value indicating whether the specified player has lost the game.
- [func isWin(for: any GKGameModelPlayer) -> Bool](gkgamemodel/iswin(for:).md)
  Returns a Boolean value indicating whether the current state of the game model reflects a win for the specified player.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkgamemodel/gamemodelupdates(for:))*