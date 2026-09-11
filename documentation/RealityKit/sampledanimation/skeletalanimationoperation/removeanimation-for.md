# removeAnimation(for:)

**Framework**: RealityKit  
**Kind**: method

Removes animation for the specified joint.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
static func removeAnimation(for jointName: String) -> SampledAnimation<Value>.SkeletalAnimationOperation
```

#### Return Value

A [`SampledAnimation.SkeletalAnimationOperation`](sampledanimation/skeletalanimationoperation.md) that, when processed, produces a `SampledAnimation<JointTransforms>` with animation removed.

## Parameters

- `jointName`: Name of the joint to remove animation from.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/sampledanimation/skeletalanimationoperation/removeanimation(for:))*