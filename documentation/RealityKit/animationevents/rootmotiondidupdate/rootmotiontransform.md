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

This is not cumulative — it represents only the delta from the last frame.

## See Also

- [var suppressesAutomaticApplication: Bool](animationevents/rootmotiondidupdate/suppressesautomaticapplication.md)
  Controls whether subscribing suppresses automatic root motion application.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/animationevents/rootmotiondidupdate/rootmotiontransform)*