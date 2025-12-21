# restPoseTransform

**Framework**: RealityKit  
**Kind**: property

The local transform of this joint in skeleton’s rest pose, specified relative to this joint’s parent (or relative to model space, if this joint has no parent).

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+
- visionOS 1.0+

## Declaration

```swift
var restPoseTransform: Transform
```

#### Discussion

The rest pose of a skeleton is used when a joint is not otherwise animated.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/meshresource/skeleton/joint/restposetransform)*