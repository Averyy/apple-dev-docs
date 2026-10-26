# enter(_:)

**Framework**: GameplayKit  
**Kind**: method  
**Role**: Instance Method

Attempts to transition the state machine from its current state to a state of the specified class.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func enter(_ stateClass: AnyClass) -> Bool
```

```objc
- (BOOL) enterState:(Class) stateClass;
```

#### Return Value

[`true`](../../Swift/true.md) if the transition was successful; otherwise [`false`](../../Swift/false.md).

#### Discussion

You build a state machine by creating a unique [`GKState`](../gkstate.md) subclass for each distinct state possible for the machine. The [`isValidNextState(_:)`](../gkstate/isvalidnextstate%28_%29.md) method of each state object determines which other states a state machine is allowed to transition into from that state. Calling this method first tests whether a transition from the current state to the specified state is valid; if not, this method returns [`false`](../../Swift/false.md).

If a transition is allowed, the state machine sends the [`willExit(to:)`](../gkstate/willexit%28to%29.md) message to its current state object. Then, the new state object replaces the value of the [`currentState`](./currentstate.md) property. Finally, the state machine sends the  [`didEnter(from:)`](../gkstate/didenter%28from%29.md) message to the new current state object, and this method returns [`true`](../../Swift/true.md).

A newly created state machine’s [`currentState`](./currentstate.md) property is `nil`—to choose and enter an initial state, use the [`enter(_:)`](./enter%28_%29.md) method. In this case, the [`enter(_:)`](./enter%28_%29.md) call always succeeds.

## Parameters

- `stateClass`: The class of state into which to attempt a transition.

## See Also

### Working with States
- [var currentState: GKState?](./currentstate.md)
  The state machine’s current state.
- [func canEnterState(AnyClass) -> Bool](./canenterstate%28_%29.md)
  Returns a Boolean value indicating whether it is valid for the state machine to transition from its current state to a state of the specified class.
- [func update(deltaTime: TimeInterval)](./update%28deltatime%29.md)
  Tells the current state object to perform per-frame updates.
- [- stateForClass:](./stateforclass_.md)
  Returns the state object in the state machine corresponding to the specified class.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkstatemachine/enter(_:))*