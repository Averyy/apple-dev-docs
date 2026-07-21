# convertToAdditiveUsingFirstSample()

**Framework**: RealityKit  
**Kind**: method

Converts animation to additive format by subtracting the first frame.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
static func convertToAdditiveUsingFirstSample() -> SampledAnimation<Value>.SkeletalAnimationOperation
```

#### Return Value

A [`SampledAnimation.SkeletalAnimationOperation`](sampledanimation/skeletalanimationoperation.md) that, when processed, produces a `SampledAnimation<JointTransforms>` in additive format.

#### Discussion

Creates a delta animation that represents the difference between each frame and the animation’s first frame. Useful for creating relative motion from absolute animation.

## See Also

- [static func convertToAdditive(baseAnimation: AnimationResource) -> SampledAnimation<Value>.SkeletalAnimationOperation](sampledanimation/skeletalanimationoperation/converttoadditive(baseanimation:).md)
  Converts animation to additive format by subtracting a base animation.
- [static func convertToAdditiveUsingRestPose() -> SampledAnimation<Value>.SkeletalAnimationOperation](sampledanimation/skeletalanimationoperation/converttoadditiveusingrestpose.md)
  Converts animation to additive format by subtracting the skeleton’s rest pose.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/sampledanimation/skeletalanimationoperation/converttoadditiveusingfirstsample())*