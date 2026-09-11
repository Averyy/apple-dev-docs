# rootMotionTransform

**Framework**: RealityKit  
**Kind**: property

The change in position and orientation since the previous frame.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
let rootMotionTransform: Transform
```

#### Discussion

This value is the delta from the previous frame, not a cumulative transform.

## See Also

- [var suppressesAutomaticApplication: Bool](animationevents/rootmotiondidupdate/suppressesautomaticapplication.md)
  A Boolean value that controls whether subscribing to the event suppresses automatic application of the root motion delta.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/animationevents/rootmotiondidupdate/rootmotiontransform)*