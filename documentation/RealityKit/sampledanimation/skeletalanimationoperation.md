# SampledAnimation.SkeletalAnimationOperation

**Framework**: RealityKit  
**Kind**: struct  
**Role**: Structure

Operations that can be performed on skeletal animations.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
struct SkeletalAnimationOperation
```

Available when `Value` is `JointTransforms`.

## Topics

### Converting to additive animation
- [static func convertToAdditive(baseAnimation: AnimationResource) -> SampledAnimation<Value>.SkeletalAnimationOperation](./skeletalanimationoperation/converttoadditive%28baseanimation%29.md)
  Converts animation to additive format by subtracting a base animation.
- [static func convertToAdditiveUsingRestPose() -> SampledAnimation<Value>.SkeletalAnimationOperation](./skeletalanimationoperation/converttoadditiveusingrestpose%28%29.md)
  Converts animation to additive format by subtracting the skeleton’s rest pose.
- [static func convertToAdditiveUsingFirstSample() -> SampledAnimation<Value>.SkeletalAnimationOperation](./skeletalanimationoperation/converttoadditiveusingfirstsample%28%29.md)
  Converts animation to additive format by subtracting the first frame.
### Extracting root motion
- [static func extractRootMotion(jointName: String, options: SampledAnimation<Value>.SkeletalAnimationOperation.RootMotionOptions, lockPosition: Transform?) -> SampledAnimation<Value>.SkeletalAnimationOperation](./skeletalanimationoperation/extractrootmotion%28jointname,options,lockposition%29.md)
  Extracts root motion from the specified joint.
- [SampledAnimation.SkeletalAnimationOperation.RootMotionOptions](./skeletalanimationoperation/rootmotionoptions.md)
  Options for controlling root motion extraction.
### Removing animation content
- [static func removeAnimation(for: String) -> SampledAnimation<Value>.SkeletalAnimationOperation](./skeletalanimationoperation/removeanimation%28for%29.md)
  Removes animation for the specified joint.

## See Also

### Processing skeletal animations
- [func processAndCreateAnimation(retargeting: RetargetingConfiguration, operations: [SampledAnimation<Value>.SkeletalAnimationOperation], name: String) throws -> any AnimationDefinition](./processandcreateanimation%28retargeting,operations,name%29.md)
  Processes skeletal animation with the specified retargeting and operations.
- [func processAndCreateAnimation(for: SkeletonResource?, operations: [SampledAnimation<Value>.SkeletalAnimationOperation], name: String) throws -> any AnimationDefinition](./processandcreateanimation%28for,operations,name%29.md)
  Processes skeletal animation with the specified operations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/sampledanimation/skeletalanimationoperation)*