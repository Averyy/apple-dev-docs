# GKState

**Framework**: GameplayKit  
**Kind**: class

The abstract superclass for defining state-specific logic as part of a state machine.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
class GKState
```

#### Overview

The [`GKState`](gkstate.md) abstract class defines the features of state classes to be used with a state machine (a [`GKStateMachine`](gkstatemachine.md) object). You build a state machine by defining a separate [`GKState`](gkstate.md) subclass for each state of the machine. In each state class, you use the [`isValidNextState(_:)`](gkstate/isvalidnextstate(_:).md) method to define which other states are valid for a machine to transition into. State classes provide a place to put state-dependent game logic, such as actions that should happen when entering or exiting a specific state, or per-frame update code that is valid only when in a specific state.

For more information about state machines, read [`State Machines`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/General/Conceptual/GameplayKit_Guide/StateMachine.html#//apple_ref/doc/uid/TP40015172-CH7) in [`GameplayKit Programming Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/General/Conceptual/GameplayKit_Guide/index.html#//apple_ref/doc/uid/TP40015172).

## Topics

### Creating a State
- [init()](gkstate/init.md)
  Initializes a state object.
### Working with State Machines
- [var stateMachine: GKStateMachine?](gkstate/statemachine.md)
  The state machine that owns this state object.
- [func isValidNextState(AnyClass) -> Bool](gkstate/isvalidnextstate(_:).md)
  Returns a Boolean value indicating whether a state machine currently in this state is allowed to transition into the specified state.
### Handling State Transitions and Updates
- [func didEnter(from: GKState?)](gkstate/didenter(from:).md)
  Performs custom actions when a state machine transitions into this state.
- [func update(deltaTime: TimeInterval)](gkstate/update(deltatime:).md)
  Performs custom actions when a state machine updates while in this state.
- [func willExit(to: GKState)](gkstate/willexit(to:).md)
  Performs custom actions when a state machine transitions out of this state.

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

- [class GKStateMachine](gkstatemachine.md)
  A finite-state machine—a collection of state objects that each define logic for a particular state of gameplay and rules for transitioning between states.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkstate)*