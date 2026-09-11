# convertToAdditiveUsingRestPose()

**Framework**: RealityKit  
**Kind**: method

Converts animation to additive format by subtracting the skeleton’s rest pose.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
static func convertToAdditiveUsingRestPose() -> SampledAnimation<Value>.SkeletalAnimationOperation
```

#### Return Value

A [`SampledAnimation.SkeletalAnimationOperation`](sampledanimation/skeletalanimationoperation.md) that, when processed, produces a `SampledAnimation<JointTransforms>` in additive format.

#### Discussion

Creates a delta animation that represents the difference between this animation and the skeleton’s rest pose. Requires a skeleton to be provided to [`processAndCreateAnimation(for:operations:name:)`](sampledanimation/processandcreateanimation(for:operations:name:).md).

## See Also

- [static func convertToAdditive(baseAnimation: AnimationResource) -> SampledAnimation<Value>.SkeletalAnimationOperation](sampledanimation/skeletalanimationoperation/converttoadditive(baseanimation:).md)
  Converts animation to additive format by subtracting a base animation.
- [static func convertToAdditiveUsingFirstSample() -> SampledAnimation<Value>.SkeletalAnimationOperation](sampledanimation/skeletalanimationoperation/converttoadditiveusingfirstsample.md)
  Converts animation to additive format by subtracting the first frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/sampledanimation/skeletalanimationoperation/converttoadditiveusingrestpose())*