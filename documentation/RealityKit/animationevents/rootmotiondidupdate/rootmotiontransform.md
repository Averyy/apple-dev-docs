# rootMotionTransform

**Framework**: RealityKit  
**Kind**: property

The change in position and orientation since the previous frame.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

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