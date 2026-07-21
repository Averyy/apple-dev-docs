# removeAnimation(for:)

**Framework**: RealityKit  
**Kind**: method

Removes animation for the specified joint.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

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