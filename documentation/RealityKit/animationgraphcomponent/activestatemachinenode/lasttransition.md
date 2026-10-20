# lastTransition

**Framework**: RealityKit  
**Kind**: property  
**Role**: Instance Property

The ID of the most recent transition the state machine took.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
var lastTransition: Int { get }
```

## See Also

### Inspecting the node state
- [var currentState: Int](./currentstate.md)
  The ID of the state the state machine is currently in.
- [var previousState: Int](./previousstate.md)
  The ID of the state the state machine was in immediately before [`currentState`](./currentstate.md).
- [var wasReset: Bool](./wasreset.md)
  A Boolean value that indicates whether the node was reset during the last evaluation tick.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/animationgraphcomponent/activestatemachinenode/lasttransition)*