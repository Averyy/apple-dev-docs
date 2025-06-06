# GKMonteCarloStrategist

**Framework**: GameplayKit  
**Kind**: class

An AI that chooses moves in turn-based games using a  strategy.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
class GKMonteCarloStrategist
```

#### Overview

To use this strategy, you indicate whether a possible states of your game model represents a win, and the strategist randomly searches possible game model states in order to find moves that will likely result in winning the game. You provide information about your game model to the strategist by implementing the [`GKGameModel`](gkgamemodel.md), [`GKGameModelPlayer`](gkgamemodelplayer.md), and [`GKGameModelUpdate`](gkgamemodelupdate.md) protocols in your custom classes, then use the strategist’s methods to find optimal moves.

##### Choosing a Strategist

The Monte Carlo strategist is one of several strategist classes that GameplayKit provides. The key advantage of the [`GKMonteCarloStrategist`](gkmontecarlostrategist.md) class is performance. By using random sampling to make educated guesses about which sequences of moves to simulate, this strategy can arrive at a decision quickly even for games with large and complex state spaces. The cost of this strategy is strength of gameplay: because the strategist randomly samples possible moves, it may miss the best moves. Additionally, this strategy doesn’t need a scoring method to rate each game model state—instead, your game model class needs to implement only the [`isWin(for:)`](gkgamemodel/iswin(for:).md) method.

See the [`GKStrategist`](gkstrategist.md) protocol for alternate strategies, as well as the methods and properties supported by all strategist classes.

##### Using a Monte Carlo Strategist

Using the Monte Carlo strategist in a game requires the following steps:

1. Create classes describing your gameplay model, adopting the [`GKGameModel`](gkgamemodel.md), [`GKGameModelPlayer`](gkgamemodelplayer.md), and [`GKGameModelUpdate`](gkgamemodelupdate.md) protocols.
2. Create a [`GKMonteCarloStrategist`](gkmontecarlostrategist.md) instance and configure its properties [`budget`](gkmontecarlostrategist/budget.md), [`explorationParameter`](gkmontecarlostrategist/explorationparameter.md), and [`randomSource`](gkstrategist/randomsource.md) to determine its gameplay behavior.
3. Point the strategist’s [`gameModel`](gkstrategist/gamemodel.md) property at the instance of your game model class (that is, your class that implements the [`GKGameModel`](gkgamemodel.md) protocol) representing the current state of the game in play.
4. Use the [`bestMoveForActivePlayer()`](gkstrategist/bestmoveforactiveplayer().md) method to select the best possible move for the current player. This method returns a move object (that is, an instance of the custom class you create to adopt the [`GKGameModelUpdate`](gkgamemodelupdate.md) protocol).
5. Examine the move object to make use of the move selected by the strategist. You created this instance in the [`gameModelUpdates(for:)`](gkgamemodel/gamemodelupdates(for:).md) method of your game model class to describe a possible move in your game, so examining the object gives you the information needed to perform that move.

For more information about describing your gameplay model and using strategists, see [`The Minmax Strategist`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/General/Conceptual/GameplayKit_Guide/Minmax.html#//apple_ref/doc/uid/TP40015172-CH2) in [`GameplayKit Programming Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/General/Conceptual/GameplayKit_Guide/index.html#//apple_ref/doc/uid/TP40015172).

## Topics

### Configuring a Strategist
- [var budget: Int](gkmontecarlostrategist/budget.md)
  The maximum number of game model states the strategist will examine when searching for a move.
- [var explorationParameter: Int](gkmontecarlostrategist/explorationparameter.md)
  A value that influences whether the strategist searches more broadly or more deeply for winning game model states.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [GKStrategist](gkstrategist.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [protocol GKStrategist](gkstrategist.md)
  A general interface for objects that provide artificial intelligence for use in turn-based (and similar) games.
- [class GKMinmaxStrategist](gkminmaxstrategist.md)
  An AI that chooses moves in turn-based games using a  strategy.
- [protocol GKGameModel](gkgamemodel.md)
  Implement this protocol to describe your gameplay model so that a strategist object can plan game moves.
- [protocol GKGameModelPlayer](gkgamemodelplayer.md)
  Implement this protocol to describe a player in your turn-based game so that a strategist object can plan game moves.
- [protocol GKGameModelUpdate](gkgamemodelupdate.md)
  Implement this protocol to describe a move in your turn-based game so that a strategist object can plan game moves.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkmontecarlostrategist)*