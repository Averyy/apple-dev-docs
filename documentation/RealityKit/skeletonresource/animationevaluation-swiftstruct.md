# SkeletonResource.AnimationEvaluation

**Framework**: RealityKit  
**Kind**: struct

A bundle of additional animation-related skeletal data the runtime consumes when evaluating animations against this skeleton.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct AnimationEvaluation
```

#### Overview

Provided at construction time and immutable for the lifetime of the resource. Bake all the supplemental data the skeleton needs into one `AnimationEvaluation` value and pass it to `SkeletonResource(named:rootJoint:animationEvaluation:)`.

## Topics

### Creating an evaluation
- [init(ikResources: [IKResource], blendMasks: [SkeletonResource.BlendMask])](skeletonresource/animationevaluation-swift.struct/init(ikresources:blendmasks:).md)
  Creates an `AnimationEvaluation` bundle with the given IK rigs and blend masks.
### Configuring the evaluation
- [let ikResources: [IKResource]](skeletonresource/animationevaluation-swift.struct/ikresources.md)
  The IK resources associated with the skeleton.
- [let blendMasks: [SkeletonResource.BlendMask]](skeletonresource/animationevaluation-swift.struct/blendmasks.md)
  The blend masks associated with the skeleton.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [let animationEvaluation: SkeletonResource.AnimationEvaluation](skeletonresource/animationevaluation-swift.property.md)
  Animation-evaluation data baked into this resource at construction time.
- [SkeletonResource.BlendMask](skeletonresource/blendmask.md)
  Describes a single blend mask for selective animation control.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/skeletonresource/animationevaluation-swift.struct)*