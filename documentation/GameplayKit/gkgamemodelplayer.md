# GKGameModelPlayer

**Framework**: GameplayKit  
**Kind**: protocol

Implement this protocol to describe a player in your turn-based game so that a strategist object can plan game moves.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.0+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
protocol GKGameModelPlayer : NSObjectProtocol
```

#### Overview

You adopt this protocol to describe the gameplay of your turn-based game for use by a [`GKStrategist`](gkstrategist.md) object. The strategist uses your player class, along with other custom classes you implement (adopting the [`GKGameModel`](gkgamemodel.md) and [`GKGameModelUpdate`](gkgamemodelupdate.md) protocols) to plan moves in your game.

You use your custom class implementing this protocol in several places:

- In the [`players`](gkgamemodel/players.md) and [`activePlayer`](gkgamemodel/activeplayer.md) properties of your game model class, to describe the set of players in your game and indicate which player’s turn it currently is
- In the [`gameModelUpdates(for:)`](gkgamemodel/gamemodelupdates(for:).md) method of your game model class, to describe the set of moves currently valid for a specified player
- In the [`isWin(for:)`](gkgamemodel/iswin(for:).md), [`isLoss(for:)`](gkgamemodel/isloss(for:).md), and [`score(for:)`](gkgamemodel/score(for:).md) method of your game model class, to rate the desirability of that particular state of the game model to a specified player
- When calling the [`bestMove(for:)`](gkminmaxstrategist/bestmove(for:).md) or [`randomMove(for:fromNumberOfBestMoves:)`](gkminmaxstrategist/randommove(for:fromnumberofbestmoves:).md) method to find an optimal move, to indicate the player for whom GameplayKit should plan moves

Your class that implements this protocol can also contain properties and methods relevant to the implementation of your game—for example, an identifying color or name.

For more information about describing your gameplay model and using a strategist, see [`The Minmax Strategist`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/General/Conceptual/GameplayKit_Guide/Minmax.html#//apple_ref/doc/uid/TP40015172-CH2) in [`GameplayKit Programming Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/General/Conceptual/GameplayKit_Guide/index.html#//apple_ref/doc/uid/TP40015172).

## Topics

### Identifying a Player
- [var playerId: Int](gkgamemodelplayer/playerid.md)
  A number uniquely identifying the player.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [protocol GKStrategist](gkstrategist.md)
  A general interface for objects that provide artificial intelligence for use in turn-based (and similar) games.
- [class GKMinmaxStrategist](gkminmaxstrategist.md)
  An AI that chooses moves in turn-based games using a  strategy.
- [class GKMonteCarloStrategist](gkmontecarlostrategist.md)
  An AI that chooses moves in turn-based games using a  strategy.
- [protocol GKGameModel](gkgamemodel.md)
  Implement this protocol to describe your gameplay model so that a strategist object can plan game moves.
- [protocol GKGameModelUpdate](gkgamemodelupdate.md)
  Implement this protocol to describe a move in your turn-based game so that a strategist object can plan game moves.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkgamemodelplayer)*