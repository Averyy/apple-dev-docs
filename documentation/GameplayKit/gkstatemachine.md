# GKStateMachine

**Framework**: GameplayKit  
**Kind**: class

A finite-state machine—a collection of state objects that each define logic for a particular state of gameplay and rules for transitioning between states.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
class GKStateMachine
```

#### Overview

In GameplayKit, you subclass [`GKState`](gkstate.md) to define each state and the rules for allowed transitions between states, and use a [`GKStateMachine`](gkstatemachine.md) instance to manage a machine that combines several states. This system provides a way to organize code in your game by organizing state-dependent actions into methods that run when entering a state, when exiting a state, and periodically while in a state (for example, on every animation frame your game renders).

You can use state machines to govern various aspects of a game. For example:

- An enemy character might use a state machine with Chase, Flee, Dead, and Respawn states, each of which drives the enemy’s behavior, with state transitions determined by player actions and elapsed time.
- An automated turret might use a state machine with Ready, Firing, and Cooldown states, controlling when it seeks out nearby targets and how often it fires.
- A game user interface might use Menu, Playing, Paused, and GameOver states, each of which determines what UI elements are shown and what other game elements are running.

To build a state machine, first define a distinct subclass of [`GKState`](gkstate.md) for each possible state of the machine. In each state class, the [`isValidNextState(_:)`](gkstate/isvalidnextstate(_:).md) method determines which other state classes the machine may transition into from that state. Then, create a state machine object by constructing instances of the state classes and passing them to one of the methods listed in Creating a State Machine below. Finally, set the machine in motion by choosing an initial state for it to enter with the [`enter(_:)`](gkstatemachine/enter(_:).md) method.

To define state-dependent behavior, override the [`didEnter(from:)`](gkstate/didenter(from:).md), [`update(deltaTime:)`](gkstate/update(deltatime:).md), and [`willExit(to:)`](gkstate/willexit(to:).md) methods in each [`GKState`](gkstate.md) subclass.

- The state machine notifies the current state whenever a state change happens. Use the [`didEnter(from:)`](gkstate/didenter(from:).md) and [`willExit(to:)`](gkstate/willexit(to:).md) methods to perform actions in response to a state change. For example, an enemy character entering the Flee state might change its appearance to indicate that is has become vulnerable to attack by the player.
- When you call a state machine’s [`update(deltaTime:)`](gkstatemachine/update(deltatime:).md) method, the state machine calls the [`update(deltaTime:)`](gkstate/update(deltatime:).md) method of its current state. Use this method to organize per-frame update code by state. For example, an enemy character in the Chase state can update its position to pursue the player, and an enemy in the Flee state can update its position to evade the player.

For more information about state machines, read [`State Machines`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/General/Conceptual/GameplayKit_Guide/StateMachine.html#//apple_ref/doc/uid/TP40015172-CH7) in [`GameplayKit Programming Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/General/Conceptual/GameplayKit_Guide/index.html#//apple_ref/doc/uid/TP40015172).

## Topics

### Creating a State Machine
- [init(states: [GKState])](gkstatemachine/init(states:).md)
  Initializes a state machine with the specified states.
### Working with States
- [var currentState: GKState?](gkstatemachine/currentstate.md)
  The state machine’s current state.
- [func canEnterState(AnyClass) -> Bool](gkstatemachine/canenterstate(_:).md)
  Returns a Boolean value indicating whether it is valid for the state machine to transition from its current state to a state of the specified class.
- [func enter(AnyClass) -> Bool](gkstatemachine/enter(_:).md)
  Attempts to transition the state machine from its current state to a state of the specified class.
- [func update(deltaTime: TimeInterval)](gkstatemachine/update(deltatime:).md)
  Tells the current state object to perform per-frame updates.
### Instance Methods
- [func state<StateType>(forClass: StateType.Type) -> StateType?](gkstatemachine/state(forclass:).md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class GKState](gkstate.md)
  The abstract superclass for defining state-specific logic as part of a state machine.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkstatemachine)*