# GKStrategist

**Framework**: GameplayKit  
**Kind**: protocol

A general interface for objects that provide artificial intelligence for use in turn-based (and similar) games.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.0+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
protocol GKStrategist : NSObjectProtocol
```

#### Overview

GameplayKit provides two strategist classes, and you can also use this protocol to implement your own. You provide information about your game model to a strategist by implementing the [`GKGameModel`](gkgamemodel.md), [`GKGameModelPlayer`](gkgamemodelplayer.md), and [`GKGameModelUpdate`](gkgamemodelupdate.md) protocols in your custom classes, then use the strategist’s methods to find optimal moves.

##### Choosing a Strategist

GameplayKit provides two strategist classes:

- The [`GKMinmaxStrategist`](gkminmaxstrategist.md) class uses a numeric score for each possible game model state, and performs an exhaustive tree search to find moves that maximize the player’s score while minimizing opponent scores. This strategy can result in optimal gameplay, but requires a scoring method for game models and has a performance cost that increases greatly with game complexity.
- The [`GKMonteCarloStrategist`](gkmontecarlostrategist.md) class performs a randomized, probabilistic search for winning end states. This strategy doesn’t always choose the  possible move, but is likely to choose  moves, and has a low performance cost even for very complex games. In addition, the Monte Carlo strategy is concerned only with whether a game model state represents a win, so you don’t need to implement a scoring method.

##### Using a Strategist

Using a strategist in a game requires the following steps:

1. Create classes describing your gameplay model, adopting the [`GKGameModel`](gkgamemodel.md), [`GKGameModelPlayer`](gkgamemodelplayer.md), and [`GKGameModelUpdate`](gkgamemodelupdate.md) protocols.
2. Choose a strategist class (one that adopts the [`GKStrategist`](gkstrategist.md) protocol), create an instance of that class, and configure its properties to determine its gameplay behavior.
3. Point the strategist’s [`gameModel`](gkstrategist/gamemodel.md) property at the instance of your game model class representing the current state of the game in play.
4. Use the [`bestMoveForActivePlayer()`](gkstrategist/bestmoveforactiveplayer().md) method to select the best possible move for the current player. This method returns a move object (that is, an instance of the custom class you create to adopt the [`GKGameModelUpdate`](gkgamemodelupdate.md) protocol).
5. Examine the move object to make use of the move selected by the strategist. You created this instance in the [`gameModelUpdates(for:)`](gkgamemodel/gamemodelupdates(for:).md) method of your game model class to describe a possible move in your game, so examining the object gives you the information needed to perform that move.

For more information about describing your gameplay model and using strategists, see [`The Minmax Strategist`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/General/Conceptual/GameplayKit_Guide/Minmax.html#//apple_ref/doc/uid/TP40015172-CH2) in [`GameplayKit Programming Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/General/Conceptual/GameplayKit_Guide/index.html#//apple_ref/doc/uid/TP40015172).

## Topics

### Specifying the Game Model
- [var gameModel: (any GKGameModel)?](gkstrategist/gamemodel.md)
  The model representing the current state of the game.
### Configuring a Strategist
- [var randomSource: (any GKRandom)?](gkstrategist/randomsource.md)
  A randomizer object to be used when the strategist randomly selects a move.
### Planning Game Moves
- [func bestMoveForActivePlayer() -> (any GKGameModelUpdate)?](gkstrategist/bestmoveforactiveplayer.md)
  Computes and returns the best possible move for the current player.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
### Conforming Types
- [GKMinmaxStrategist](gkminmaxstrategist.md)
- [GKMonteCarloStrategist](gkmontecarlostrategist.md)

## See Also

- [class GKMinmaxStrategist](gkminmaxstrategist.md)
  An AI that chooses moves in turn-based games using a  strategy.
- [class GKMonteCarloStrategist](gkmontecarlostrategist.md)
  An AI that chooses moves in turn-based games using a  strategy.
- [protocol GKGameModel](gkgamemodel.md)
  Implement this protocol to describe your gameplay model so that a strategist object can plan game moves.
- [protocol GKGameModelPlayer](gkgamemodelplayer.md)
  Implement this protocol to describe a player in your turn-based game so that a strategist object can plan game moves.
- [protocol GKGameModelUpdate](gkgamemodelupdate.md)
  Implement this protocol to describe a move in your turn-based game so that a strategist object can plan game moves.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkstrategist)*