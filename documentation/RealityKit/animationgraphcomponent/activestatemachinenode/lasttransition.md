# lastTransition

**Framework**: RealityKit  
**Kind**: property

The ID of the most recent transition the state machine took.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
var lastTransition: Int { get }
```

## See Also

- [var currentState: Int](animationgraphcomponent/activestatemachinenode/currentstate.md)
  The ID of the state the state machine is currently in.
- [var previousState: Int](animationgraphcomponent/activestatemachinenode/previousstate.md)
  The ID of the state the state machine was in immediately before [`currentState`](animationgraphcomponent/activestatemachinenode/currentstate.md).
- [var wasReset: Bool](animationgraphcomponent/activestatemachinenode/wasreset.md)
  A Boolean value that indicates whether the node was reset during the last evaluation tick.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/animationgraphcomponent/activestatemachinenode/lasttransition)*