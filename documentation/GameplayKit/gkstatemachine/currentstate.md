# currentState

**Framework**: GameplayKit  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic, readonly, nullable) GKState * currentState;
```

## Discussion

A state machine can be in only one of its states at a time. To transition to another state, call the [`enter(_:)`](./enter%28_%29.md) method.

When you call the [`update(deltaTime:)`](./update%28deltatime%29.md) method, the state machine calls the [`update(deltaTime:)`](../gkstate/update%28deltatime%29.md) method on its current state object.

## See Also

### Working with States
- [func canEnterState(AnyClass) -> Bool](./canenterstate%28_%29.md)
  Returns a Boolean value indicating whether it is valid for the state machine to transition from its current state to a state of the specified class.
- [func enter(AnyClass) -> Bool](./enter%28_%29.md)
  Attempts to transition the state machine from its current state to a state of the specified class.
- [func update(deltaTime: TimeInterval)](./update%28deltatime%29.md)
  Tells the current state object to perform per-frame updates.
- [- stateForClass:](./stateforclass_.md)
  Returns the state object in the state machine corresponding to the specified class.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkstatemachine/currentstate)*