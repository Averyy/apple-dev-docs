# SampledAnimation.SkeletalAnimationOperation

**Framework**: RealityKit  
**Kind**: struct

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

## Topics

### Converting to additive animation
- [static func convertToAdditive(baseAnimation: AnimationResource) -> SampledAnimation<Value>.SkeletalAnimationOperation](sampledanimation/skeletalanimationoperation/converttoadditive(baseanimation:).md)
  Converts animation to additive format by subtracting a base animation.
- [static func convertToAdditiveUsingRestPose() -> SampledAnimation<Value>.SkeletalAnimationOperation](sampledanimation/skeletalanimationoperation/converttoadditiveusingrestpose.md)
  Converts animation to additive format by subtracting the skeleton’s rest pose.
- [static func convertToAdditiveUsingFirstSample() -> SampledAnimation<Value>.SkeletalAnimationOperation](sampledanimation/skeletalanimationoperation/converttoadditiveusingfirstsample.md)
  Converts animation to additive format by subtracting the first frame.
### Extracting root motion
- [static func extractRootMotion(jointName: String, options: SampledAnimation<Value>.SkeletalAnimationOperation.RootMotionOptions, lockPosition: Transform?) -> SampledAnimation<Value>.SkeletalAnimationOperation](sampledanimation/skeletalanimationoperation/extractrootmotion(jointname:options:lockposition:).md)
  Extracts root motion from the specified joint.
- [SampledAnimation.SkeletalAnimationOperation.RootMotionOptions](sampledanimation/skeletalanimationoperation/rootmotionoptions.md)
  Options for controlling root motion extraction.
### Removing animation content
- [static func removeAnimation(for: String) -> SampledAnimation<Value>.SkeletalAnimationOperation](sampledanimation/skeletalanimationoperation/removeanimation(for:).md)
  Removes animation for the specified joint.

## See Also

- [func processAndCreateAnimation(retargeting: RetargetingConfiguration, operations: [SampledAnimation<Value>.SkeletalAnimationOperation], name: String) throws -> any AnimationDefinition](sampledanimation/processandcreateanimation(retargeting:operations:name:).md)
  Processes skeletal animation with the specified retargeting and operations.
- [func processAndCreateAnimation(for: SkeletonResource?, operations: [SampledAnimation<Value>.SkeletalAnimationOperation], name: String) throws -> any AnimationDefinition](sampledanimation/processandcreateanimation(for:operations:name:).md)
  Processes skeletal animation with the specified operations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/sampledanimation/skeletalanimationoperation)*