# bestMove(for:)

**Framework**: GameplayKit  
**Kind**: method

Computes and returns the best possible move for the specified player.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func bestMove(for player: any GKGameModelPlayer) -> (any GKGameModelUpdate)?
```

#### Return Value

An object describing the move found by the strategist.

#### Discussion

This method looks ahead at the possible moves for the specified player, as well as possible future moves by other players on subsequent turns (according to the [`maxLookAheadDepth`](gkminmaxstrategist/maxlookaheaddepth.md) property) and examines the state of the game model resulting from each possible move. Your game model class provides a score for each state in its [`score(for:)`](gkgamemodel/score(for:).md) method, allowing the strategist to find the sequence of future moves that maximizes the score for the specified player and return the first move in that sequence.

The object returned is an instance of your custom class implementing the [`GKGameModelUpdate`](gkgamemodelupdate.md) protocol. This object was created in your game model’s [`gameModelUpdates(for:)`](gkgamemodel/gamemodelupdates(for:).md) method, describing in your game’s terms a possible move. Examine that information to make use of the strategist’s selection. For example, you could implement a computer-controlled player by performing the selected move, or provide hints to a human player by indicating the selected move in your game’s user interface.

If multiple possible moves are tied for the best score and the [`randomSource`](gkstrategist/randomsource.md) property is not `nil`, this method randomly selects from among the tied moves.

This method returns `nil` if the specified player is invalid or has no available moves.

## Parameters

- `player`: The player for whom the strategist should plan a move. This object must be in the current game model’s   array.

## See Also

- [func randomMove(for: any GKGameModelPlayer, fromNumberOfBestMoves: Int) -> (any GKGameModelUpdate)?](gkminmaxstrategist/randommove(for:fromnumberofbestmoves:).md)
  Computes several of the best possible moves for the specified player, and returns a move randomly selected from among them.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkminmaxstrategist/bestmove(for:))*