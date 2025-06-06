# GKGameModel

**Framework**: GameplayKit  
**Kind**: protocol

Implement this protocol to describe your gameplay model so that a strategist object can plan game moves.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.0+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
protocol GKGameModel : NSCopying, NSObjectProtocol
```

#### Overview

You adopt this protocol to describe the gameplay of your turn-based game for use by a [`GKStrategist`](gkstrategist.md) object. The strategist uses your game model class (that is, the class you create to adopt this protocol), along with other custom classes you create (adopting the [`GKGameModelPlayer`](gkgamemodelplayer.md) and [`GKGameModelUpdate`](gkgamemodelupdate.md) protocols), to find optimal moves.

GameplayKit relies on your game model class for several parts of its strategy algorithm.

- Identifying possible changes to the game state. Your [`gameModelUpdates(for:)`](gkgamemodel/gamemodelupdates(for:).md) method and your move class (a custom class implementing the [`GKGameModelUpdate`](gkgamemodelupdate.md) protocol) describe the set of moves available during a given player’s turn.
- Simulating future moves on a copy of the game. Your [`setGameModel(_:)`](gkgamemodel/setgamemodel(_:).md) method allows GameplayKit to work with a separate instance of the game model—that is, not the one representing the actual game in play—and your [`apply(_:)`](gkgamemodel/apply(_:).md) uses the information in your move class to perform hypothetical moves on that separate copy of the game.
- Rating the desirability of possible future states of the game. Each time GameplayKit performs a hypothetical move in its copy of the game model, it calls your [`isWin(for:)`](gkgamemodel/iswin(for:).md), [`isLoss(for:)`](gkgamemodel/isloss(for:).md), or [`score(for:)`](gkgamemodel/score(for:).md) method to evaluate that state of the game from the perspective of a particular player.

When you use a strategist to plan moves in your game, it uses your game model to combine these parts into a strategy: By identifying, performing, and rating the success of possible future moves, the strategist can choose a move most likely to result in a future win. This process involves using the [`copy(with:)`](https://developer.apple.com/documentation/foundation/nscopying/1410311-copy) and [`setGameModel(_:)`](gkgamemodel/setgamemodel(_:).md) methods to evaluate many possible states of a game model—for best results, ensure that your game model class contains only the information critical to describing your game and that it can copy that state quickly.

For more information about describing your gameplay model and using a strategist, see [`The Minmax Strategist`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/General/Conceptual/GameplayKit_Guide/Minmax.html#//apple_ref/doc/uid/TP40015172-CH2) in [`GameplayKit Programming Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/General/Conceptual/GameplayKit_Guide/index.html#//apple_ref/doc/uid/TP40015172).

## Topics

### Keeping Track of Players
- [var players: [any GKGameModelPlayer]?](gkgamemodel/players.md)
  The players currently in the game.
- [var activePlayer: (any GKGameModelPlayer)?](gkgamemodel/activeplayer.md)
  The player whose turn it currently is in the game.
### Evaluating a Game Model
- [func gameModelUpdates(for: any GKGameModelPlayer) -> [any GKGameModelUpdate]?](gkgamemodel/gamemodelupdates(for:).md)
  Returns the set of moves available to the specified player.
- [func score(for: any GKGameModelPlayer) -> Int](gkgamemodel/score(for:).md)
  Returns a number rating the desirability of the game model’s current state from the perspective of the specified player.
- [func isLoss(for: any GKGameModelPlayer) -> Bool](gkgamemodel/isloss(for:).md)
  Returns a Boolean value indicating whether the specified player has lost the game.
- [func isWin(for: any GKGameModelPlayer) -> Bool](gkgamemodel/iswin(for:).md)
  Returns a Boolean value indicating whether the current state of the game model reflects a win for the specified player.
### Modifying a Game Model
- [func apply(any GKGameModelUpdate)](gkgamemodel/apply(_:).md)
  Updates the internal state of the game model to reflect the specified changes.
- [func unapplyGameModelUpdate(any GKGameModelUpdate)](gkgamemodel/unapplygamemodelupdate(_:).md)
  Updates the internal state of the game model to remove the effect of the specified changes.
- [func setGameModel(any GKGameModel)](gkgamemodel/setgamemodel(_:).md)
  Sets the game model’s internal state to that of the specified game model.
### Constants
- [Game Model Score Limits](game-model-score-limits.md)
  Limits to values returned by the [`score(for:)`](gkgamemodel/score(for:).md) method.

## Relationships

### Inherits From
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [protocol GKStrategist](gkstrategist.md)
  A general interface for objects that provide artificial intelligence for use in turn-based (and similar) games.
- [class GKMinmaxStrategist](gkminmaxstrategist.md)
  An AI that chooses moves in turn-based games using a  strategy.
- [class GKMonteCarloStrategist](gkmontecarlostrategist.md)
  An AI that chooses moves in turn-based games using a  strategy.
- [protocol GKGameModelPlayer](gkgamemodelplayer.md)
  Implement this protocol to describe a player in your turn-based game so that a strategist object can plan game moves.
- [protocol GKGameModelUpdate](gkgamemodelupdate.md)
  Implement this protocol to describe a move in your turn-based game so that a strategist object can plan game moves.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkgamemodel)*