# score(for:)

**Framework**: GameplayKit  
**Kind**: method

Returns a number rating the desirability of the game model’s current state from the perspective of the specified player.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.0+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
optional func score(for player: any GKGameModelPlayer) -> Int
```

#### Return Value

A value indicating the specified player’s evaluation of the game model’s current state. Higher values indicate that a state is more desirable than lower values.

#### Discussion

The score you return from this method is the primary heuristic by which the [`GKMinmaxStrategist`](gkminmaxstrategist.md) class evaluates possible moves. GameplayKit speculates about the effects of possible future moves by making copies of the active game model, applying possible moves to that model, and calling your [`score(for:)`](gkgamemodel/score(for:).md) method to rate the effects of those moves. Returning a high rating from your score method indicates a state of the game model that is advantageous to the given player; a low rating indicates a state that is less advantageous. GameplayKit then collects and sorts the scores resulting from many possible moves (including future moves that follow the move currently being planned) to find the most advantageous move for the active player’s current turn.

Exactly how you calculate scores to return from this method depends on the rules of your game and your strategy for evaluating possible game states. The gameplay performance of the [`GKMinmaxStrategist`](gkminmaxstrategist.md) strategist depends largely on the soundness of your metric in describing the relative advantage of different game positions. For example, if your metric can distinguish between a move that is likely to result in a win after a few turns and a move that is likely to result in a win after many turns, the strategist will be better able to predict winning moves.

This method should return [`NSIntegerMin`](https://developer.apple.com/documentation/ObjectiveC/NSIntegerMin) if the specified player is not valid.

> **Note**:  This method is optional; however, your game model class must implement at least one of the [`score(for:)`](gkgamemodel/score(for:).md), [`isLoss(for:)`](gkgamemodel/isloss(for:).md), and [`isWin(for:)`](gkgamemodel/iswin(for:).md) methods.

 This method is optional; however, your game model class must implement at least one of the [`score(for:)`](gkgamemodel/score(for:).md), [`isLoss(for:)`](gkgamemodel/isloss(for:).md), and [`isWin(for:)`](gkgamemodel/iswin(for:).md) methods.

## Parameters

- `player`: An instance of your game’s player class (a custom class implementing the   protocol) representing the player evaluating the game model.

## See Also

- [func gameModelUpdates(for: any GKGameModelPlayer) -> [any GKGameModelUpdate]?](gkgamemodel/gamemodelupdates(for:).md)
  Returns the set of moves available to the specified player.
- [func isLoss(for: any GKGameModelPlayer) -> Bool](gkgamemodel/isloss(for:).md)
  Returns a Boolean value indicating whether the specified player has lost the game.
- [func isWin(for: any GKGameModelPlayer) -> Bool](gkgamemodel/iswin(for:).md)
  Returns a Boolean value indicating whether the current state of the game model reflects a win for the specified player.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkgamemodel/score(for:))*