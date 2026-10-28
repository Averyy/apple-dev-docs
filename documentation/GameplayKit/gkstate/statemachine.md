# stateMachine

**Framework**: GameplayKit  
**Kind**: property  
**Role**: Instance Property

The state machine that owns this state object.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
weak var stateMachine: GKStateMachine? { get }
```

```objc
@property (nonatomic, weak, readonly, nullable) GKStateMachine * stateMachine;
```

## Discussion

Use this property to refer to the state machine this state object is being used in.

## See Also

### Working with State Machines
- [func isValidNextState(AnyClass) -> Bool](./isvalidnextstate%28_%29.md)
  Returns a Boolean value indicating whether a state machine currently in this state is allowed to transition into the specified state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkstate/statemachine)*