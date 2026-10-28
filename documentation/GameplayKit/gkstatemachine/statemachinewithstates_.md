# stateMachineWithStates:

**Framework**: GameplayKit  
**Kind**: method  
**Role**: Type Method

Creates a state machine with the specified states.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```objc
+ (instancetype) stateMachineWithStates:(NSArray<GKState *> *) states;
```

## Return Value

A new state machine.

## Discussion

The newly created state machine’s [`currentState`](./currentstate.md) property is `nil`. To choose and enter an initial state, use the [`enter(_:)`](./enter%28_%29.md) method.

## Parameters

- `states`: An array of state objects. Each object in the array must be of a unique subclass of [`GKState`](../gkstate.md).

## See Also

### Creating a State Machine
- [init(states: [GKState])](./init%28states%29.md)
  Initializes a state machine with the specified states.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkstatemachine/statemachinewithstates:)*