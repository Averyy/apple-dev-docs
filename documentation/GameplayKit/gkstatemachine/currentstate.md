# currentState

**Framework**: GameplayKit  
**Kind**: property

The state machine’s current state.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var currentState: GKState? { get }
```

#### Discussion

A state machine can be in only one of its states at a time. To transition to another state, call the [`enter(_:)`](gkstatemachine/enter(_:).md) method.

When you call the [`update(deltaTime:)`](gkstatemachine/update(deltatime:).md) method, the state machine calls the [`update(deltaTime:)`](gkstate/update(deltatime:).md) method on its current state object.

## See Also

- [func canEnterState(AnyClass) -> Bool](gkstatemachine/canenterstate(_:).md)
  Returns a Boolean value indicating whether it is valid for the state machine to transition from its current state to a state of the specified class.
- [func enter(AnyClass) -> Bool](gkstatemachine/enter(_:).md)
  Attempts to transition the state machine from its current state to a state of the specified class.
- [func update(deltaTime: TimeInterval)](gkstatemachine/update(deltatime:).md)
  Tells the current state object to perform per-frame updates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkstatemachine/currentstate)*