# SkeletonResource.AnimationEvaluation

**Framework**: RealityKit  
**Kind**: struct  
**Role**: Structure

A bundle of additional animation-related skeletal data the runtime consumes when evaluating animations against this skeleton.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
struct AnimationEvaluation
```

#### Overview

Provided at construction time and immutable for the lifetime of the resource. Bake all the supplemental data the skeleton needs into one `AnimationEvaluation` value and pass it to `SkeletonResource(named:rootJoint:animationEvaluation:)`.

## Topics

### Creating an evaluation
- [init(ikResources: [IKResource], blendMasks: [SkeletonResource.BlendMask])](./animationevaluation-swift.struct/init%28ikresources,blendmasks%29.md)
  Creates an `AnimationEvaluation` bundle with the given IK resources and blend masks.
### Configuring the evaluation
- [let ikResources: [IKResource]](./animationevaluation-swift.struct/ikresources.md)
  The IK resources associated with the skeleton.
- [let blendMasks: [SkeletonResource.BlendMask]](./animationevaluation-swift.struct/blendmasks.md)
  The blend masks associated with the skeleton.

## Relationships

### Conforms To
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Configuring animation evaluation
- [let animationEvaluation: SkeletonResource.AnimationEvaluation](./animationevaluation-swift.property.md)
  Animation-evaluation data baked into this resource at construction time.
- [SkeletonResource.BlendMask](./blendmask.md)
  Describes a single blend mask for selective animation control.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/skeletonresource/animationevaluation-swift.struct)*