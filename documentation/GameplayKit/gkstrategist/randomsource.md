# randomSource

**Framework**: GameplayKit  
**Kind**: property  
**Required**: Yes

A randomizer object to be used when the strategist randomly selects a move.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.0+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var randomSource: (any GKRandom)? { get set }
```

#### Discussion

A strategist class uses this random source when you call the [`bestMoveForActivePlayer()`](gkstrategist/bestmoveforactiveplayer().md) method. Different strategist classes use randomization in different ways:

- A  strategy, such as that of the [`GKMinmaxStrategist`](gkminmaxstrategist.md) class, can reach states where multiple moves are rated the most desirable. In such cases, the strategist can randomly choose from among the best possible moves, making the behavior of a computer-controlled player appear more natural and unpredictable.

If this property is set to `nil` (the default), the [`GKMinmaxStrategist`](gkminmaxstrategist.md) class method does not randomize—that is, when repeatedly presented with the same set of equally-optimal moves, the [`bestMoveForActivePlayer()`](gkstrategist/bestmoveforactiveplayer().md) method always makes the same choice.

- A  strategy, such as that of the [`GKMonteCarloStrategist`](gkmontecarlostrategist.md) class,  a random source in order to randomly explore the set of possible moves.

If this property is set to `nil` (the default), the [`GKMonteCarloStrategist`](gkmontecarlostrategist.md) class throws an exception when you call the [`bestMoveForActivePlayer()`](gkstrategist/bestmoveforactiveplayer().md) method.

A randomizer is any object that implements the [`GKRandom`](gkrandom.md) protocol, such as the [`GKRandomSource`](gkrandomsource.md) and [`GKRandomDistribution`](gkrandomdistribution.md) classes and their subclasses. Choosing a separate randomizer instance from that used by other systems in your game ensures that the randomization of moves is independent; that is, the strategist’s selection of moves does not depend on your game’s other uses of randomization APIs. You can also use randomizer classes to reproduce a specific sequence of random actions for debugging, and to fine-tune the randomization behavior.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkstrategist/randomsource)*