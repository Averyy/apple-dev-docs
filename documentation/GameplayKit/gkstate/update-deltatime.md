# update(deltaTime:)

**Framework**: GameplayKit  
**Kind**: method

Performs custom actions when a state machine updates while in this state.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func update(deltaTime seconds: TimeInterval)
```

#### Discussion

A state machine calls this method when its own [`update(deltaTime:)`](gkstatemachine/update(deltatime:).md) method is called—typically, in preparation for each animation frame to be rendered in your game. Override this method to implement per-frame logic specific to this state in the state machine.

For example, in a game where each enemy character has Chase, Flee, Dead, and Respawn states, the update method for the Chase state might find the player’s location and move the enemy in the direction of the player, the update method for the Flee state might move the enemy away from the player, and the update method for the Dead state might move what remains of the enemy towards its respawn location.

## Parameters

- `seconds`: The time step to use for any time-dependent actions performed by this method (typically, the elapsed time since the previous call to this method).

## See Also

- [func didEnter(from: GKState?)](gkstate/didenter(from:).md)
  Performs custom actions when a state machine transitions into this state.
- [func willExit(to: GKState)](gkstate/willexit(to:).md)
  Performs custom actions when a state machine transitions out of this state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkstate/update(deltatime:))*