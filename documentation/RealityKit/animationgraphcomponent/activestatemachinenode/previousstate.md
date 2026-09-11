# previousState

**Framework**: RealityKit  
**Kind**: property

The ID of the state the state machine was in immediately before [`currentState`](animationgraphcomponent/activestatemachinenode/currentstate.md).

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
var previousState: Int { get }
```

## See Also

- [var currentState: Int](animationgraphcomponent/activestatemachinenode/currentstate.md)
  The ID of the state the state machine is currently in.
- [var lastTransition: Int](animationgraphcomponent/activestatemachinenode/lasttransition.md)
  The ID of the most recent transition the state machine took.
- [var wasReset: Bool](animationgraphcomponent/activestatemachinenode/wasreset.md)
  A Boolean value that indicates whether the node was reset during the last evaluation tick.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/animationgraphcomponent/activestatemachinenode/previousstate)*