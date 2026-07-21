# convertToAdditive(baseAnimation:)

**Framework**: RealityKit  
**Kind**: method

Converts animation to additive format by subtracting a base animation.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
static func convertToAdditive(baseAnimation: AnimationResource) -> SampledAnimation<Value>.SkeletalAnimationOperation
```

#### Return Value

A [`SampledAnimation.SkeletalAnimationOperation`](sampledanimation/skeletalanimationoperation.md) that, when processed, produces a `SampledAnimation<JointTransforms>` in additive format.

#### Discussion

Creates a delta animation that represents the difference between this animation and the provided base animation. You can layer the resulting animation on top of other animations using additive blending.

If the base animation has more samples than the target animation, the function subtracts the last sample from each remaining sample in the target.

The function throws an error if the base and target animations do not have the same frame interval (sample rate).

## Parameters

- `baseAnimation`: Base animation to subtract.

## See Also

- [static func convertToAdditiveUsingRestPose() -> SampledAnimation<Value>.SkeletalAnimationOperation](sampledanimation/skeletalanimationoperation/converttoadditiveusingrestpose.md)
  Converts animation to additive format by subtracting the skeleton’s rest pose.
- [static func convertToAdditiveUsingFirstSample() -> SampledAnimation<Value>.SkeletalAnimationOperation](sampledanimation/skeletalanimationoperation/converttoadditiveusingfirstsample.md)
  Converts animation to additive format by subtracting the first frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/sampledanimation/skeletalanimationoperation/converttoadditive(baseanimation:))*