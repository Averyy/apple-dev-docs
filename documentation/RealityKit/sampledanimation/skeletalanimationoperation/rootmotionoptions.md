# SampledAnimation.SkeletalAnimationOperation.RootMotionOptions

**Framework**: RealityKit  
**Kind**: struct  
**Role**: Structure

Options for controlling root motion extraction.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
struct RootMotionOptions
```

## Topics

### Extracting translation
- [static let extractAll: SampledAnimation<JointTransforms>.SkeletalAnimationOperation.RootMotionOptions](./rootmotionoptions/extractall.md)
  All motion is extracted and returned.
- [static let translationX: SampledAnimation<JointTransforms>.SkeletalAnimationOperation.RootMotionOptions](./rootmotionoptions/translationx.md)
  Translation X is extracted.
- [static let translationY: SampledAnimation<JointTransforms>.SkeletalAnimationOperation.RootMotionOptions](./rootmotionoptions/translationy.md)
  Translation Y is extracted.
- [static let translationZ: SampledAnimation<JointTransforms>.SkeletalAnimationOperation.RootMotionOptions](./rootmotionoptions/translationz.md)
  Translation Z is extracted.
- [static let translationXZ: SampledAnimation<JointTransforms>.SkeletalAnimationOperation.RootMotionOptions](./rootmotionoptions/translationxz.md)
  Translation XZ is extracted (common for ground-based locomotion).
### Extracting rotation
- [static let rotationX: SampledAnimation<JointTransforms>.SkeletalAnimationOperation.RootMotionOptions](./rootmotionoptions/rotationx.md)
  Rotation X is extracted.
- [static let rotationY: SampledAnimation<JointTransforms>.SkeletalAnimationOperation.RootMotionOptions](./rootmotionoptions/rotationy.md)
  Rotation Y is extracted.
- [static let rotationZ: SampledAnimation<JointTransforms>.SkeletalAnimationOperation.RootMotionOptions](./rootmotionoptions/rotationz.md)
  Rotation Z is extracted.

## Relationships

### Conforms To
- [Equatable](../../../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../../../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../../../Swift/optionset.md)
- [RawRepresentable](../../../Swift/rawrepresentable.md)
- [SetAlgebra](../../../Swift/setalgebra.md)

## See Also

### Extracting root motion
- [static func extractRootMotion(jointName: String, options: SampledAnimation<Value>.SkeletalAnimationOperation.RootMotionOptions, lockPosition: Transform?) -> SampledAnimation<Value>.SkeletalAnimationOperation](./extractrootmotion%28jointname,options,lockposition%29.md)
  Extracts root motion from the specified joint.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/sampledanimation/skeletalanimationoperation/rootmotionoptions)*