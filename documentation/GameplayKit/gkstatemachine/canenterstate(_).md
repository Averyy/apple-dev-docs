# canEnterState(_:)

**Framework**: GameplayKit  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (BOOL) canEnterState:(Class) stateClass;
```

#### Return Value

[`true`](../../Swift/true.md) if a transition is allowed from the current state to a state of the specified class; otherwise [`false`](../../Swift/false.md).

#### Discussion

You build a state machine by creating a unique [`GKState`](../gkstate.md) subclass for each distinct state possible for the machine. The [`isValidNextState(_:)`](../gkstate/isvalidnextstate%28_%29.md) method of each state object determines which other states a state machine is allowed to transition into from that state.

A newly created state machine’s [`currentState`](./currentstate.md) property is `nil`. In this case, the [`canEnterState(_:)`](./canenterstate%28_%29.md) method always returns [`true`](../../Swift/true.md). To choose and enter an initial state, use the [`enter(_:)`](./enter%28_%29.md) method.

## Parameters

- `stateClass`: The class of state for which to determine whether a transition is allowed.

## See Also

### Working with States
- [var currentState: GKState?](./currentstate.md)
  The state machine’s current state.
- [func enter(AnyClass) -> Bool](./enter%28_%29.md)
  Attempts to transition the state machine from its current state to a state of the specified class.
- [func update(deltaTime: TimeInterval)](./update%28deltatime%29.md)
  Tells the current state object to perform per-frame updates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkstatemachine/canenterstate(_:))*