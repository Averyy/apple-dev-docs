# canEnterState(_:)

**Framework**: GameplayKit  
**Kind**: method

Returns a Boolean value indicating whether it is valid for the state machine to transition from its current state to a state of the specified class.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func canEnterState(_ stateClass: AnyClass) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if a transition is allowed from the current state to a state of the specified class; otherwise [`false`](https://developer.apple.com/documentation/swift/false).

#### Discussion

You build a state machine by creating a unique [`GKState`](gkstate.md) subclass for each distinct state possible for the machine. The [`isValidNextState(_:)`](gkstate/isvalidnextstate(_:).md) method of each state object determines which other states a state machine is allowed to transition into from that state.

A newly created state machine’s [`currentState`](gkstatemachine/currentstate.md) property is `nil`. In this case, the [`canEnterState(_:)`](gkstatemachine/canenterstate(_:).md) method always returns [`true`](https://developer.apple.com/documentation/swift/true). To choose and enter an initial state, use the [`enter(_:)`](gkstatemachine/enter(_:).md) method.

## Parameters

- `stateClass`: The class of state for which to determine whether a transition is allowed.

## See Also

- [var currentState: GKState?](gkstatemachine/currentstate.md)
  The state machine’s current state.
- [func enter(AnyClass) -> Bool](gkstatemachine/enter(_:).md)
  Attempts to transition the state machine from its current state to a state of the specified class.
- [func update(deltaTime: TimeInterval)](gkstatemachine/update(deltatime:).md)
  Tells the current state object to perform per-frame updates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkstatemachine/canenterstate(_:))*