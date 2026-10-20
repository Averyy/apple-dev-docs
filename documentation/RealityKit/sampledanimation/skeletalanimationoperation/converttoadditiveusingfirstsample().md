# convertToAdditiveUsingFirstSample()

**Framework**: RealityKit  
**Kind**: method  
**Role**: Type Method

Converts animation to additive format by subtracting the first frame.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
static func convertToAdditiveUsingFirstSample() -> SampledAnimation<Value>.SkeletalAnimationOperation
```

#### Return Value

A [`SampledAnimation.SkeletalAnimationOperation`](../skeletalanimationoperation.md) that, when processed, produces a `SampledAnimation<JointTransforms>` in additive format.

#### Discussion

Creates a delta animation that represents the difference between each frame and the animation’s first frame. Useful for creating relative motion from absolute animation.

## See Also

### Converting to additive animation
- [static func convertToAdditive(baseAnimation: AnimationResource) -> SampledAnimation<Value>.SkeletalAnimationOperation](./converttoadditive%28baseanimation%29.md)
  Converts animation to additive format by subtracting a base animation.
- [static func convertToAdditiveUsingRestPose() -> SampledAnimation<Value>.SkeletalAnimationOperation](./converttoadditiveusingrestpose%28%29.md)
  Converts animation to additive format by subtracting the skeleton’s rest pose.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/sampledanimation/skeletalanimationoperation/converttoadditiveusingfirstsample())*