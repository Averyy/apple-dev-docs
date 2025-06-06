# init(states:)

**Framework**: GameplayKit  
**Kind**: init

Initializes a state machine with the specified states.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
init(states: [GKState])
```

#### Return Value

A new state machine.

#### Discussion

The newly created state machine’s [`currentState`](gkstatemachine/currentstate.md) property is `nil`. To choose and enter an initial state, use the [`enter(_:)`](gkstatemachine/enter(_:).md) method.

For more information, see [`GameplayKit Programming Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/General/Conceptual/GameplayKit_Guide/index.html#//apple_ref/doc/uid/TP40015172).

## Parameters

- `states`: An array of state objects. Each object in the array must be of a unique subclass of  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkstatemachine/init(states:))*