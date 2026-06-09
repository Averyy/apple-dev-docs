# SampledAnimation.SkeletalAnimationOperation.RootMotionOptions

**Framework**: RealityKit  
**Kind**: struct

Options for controlling root motion extraction.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct RootMotionOptions
```

## Topics

### Extracting translation
- [static let extractAll: SampledAnimation<JointTransforms>.SkeletalAnimationOperation.RootMotionOptions](sampledanimation/skeletalanimationoperation/rootmotionoptions/extractall.md)
  All motion is extracted and returned.
- [static let translationX: SampledAnimation<JointTransforms>.SkeletalAnimationOperation.RootMotionOptions](sampledanimation/skeletalanimationoperation/rootmotionoptions/translationx.md)
  Translation X is extracted.
- [static let translationY: SampledAnimation<JointTransforms>.SkeletalAnimationOperation.RootMotionOptions](sampledanimation/skeletalanimationoperation/rootmotionoptions/translationy.md)
  Translation Y is extracted.
- [static let translationZ: SampledAnimation<JointTransforms>.SkeletalAnimationOperation.RootMotionOptions](sampledanimation/skeletalanimationoperation/rootmotionoptions/translationz.md)
  Translation Z is extracted.
- [static let translationXZ: SampledAnimation<JointTransforms>.SkeletalAnimationOperation.RootMotionOptions](sampledanimation/skeletalanimationoperation/rootmotionoptions/translationxz.md)
  Translation XZ is extracted (common for ground-based locomotion).
### Extracting rotation
- [static let rotationX: SampledAnimation<JointTransforms>.SkeletalAnimationOperation.RootMotionOptions](sampledanimation/skeletalanimationoperation/rootmotionoptions/rotationx.md)
  Rotation X is extracted.
- [static let rotationY: SampledAnimation<JointTransforms>.SkeletalAnimationOperation.RootMotionOptions](sampledanimation/skeletalanimationoperation/rootmotionoptions/rotationy.md)
  Rotation Y is extracted.
- [static let rotationZ: SampledAnimation<JointTransforms>.SkeletalAnimationOperation.RootMotionOptions](sampledanimation/skeletalanimationoperation/rootmotionoptions/rotationz.md)
  Rotation Z is extracted.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

- [static func extractRootMotion(jointName: String, options: SampledAnimation<Value>.SkeletalAnimationOperation.RootMotionOptions, lockPosition: Transform?) -> SampledAnimation<Value>.SkeletalAnimationOperation](sampledanimation/skeletalanimationoperation/extractrootmotion(jointname:options:lockposition:).md)
  Extracts root motion from the specified joint.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/sampledanimation/skeletalanimationoperation/rootmotionoptions)*