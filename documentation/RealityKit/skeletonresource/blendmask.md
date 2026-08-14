# SkeletonResource.BlendMask

**Framework**: RealityKit  
**Kind**: struct

Describes a single blend mask for selective animation control.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct BlendMask
```

#### Overview

Blend masks enable selective application of animations by defining per-joint weights. They allow fine-grained control over which parts of a skeleton are affected by specific animations, enabling layered animation systems and partial poses.

```swift
typealias BlendMask = SkeletonResource.BlendMask
// Create blend masks for different body regions
// Joints not listed default to weight 1.0 (full animation effect)
let armOnlyMask = BlendMask(
    name: "armOnly",
    jointWeights: ["shoulder": 0.0] // Only affect upperArm, forearm, hand
)

let handOnlyMask = BlendMask(
    name: "handOnly",
    jointWeights: ["shoulder": 0.0, "upperArm": 0.0, "forearm": 0.0] // Only affect hand
)
```

## Topics

### Creating a blend mask
- [init(name: String, jointWeights: [String : Float])](skeletonresource/blendmask/init(name:jointweights:).md)
  Creates a blend mask with the specified parameters.
### Accessing mask values
- [var jointWeights: [String : Float]](skeletonresource/blendmask/jointweights.md)
  Dictionary of joint weights keyed by joint name. Each weight corresponds to a joint in the skeleton, controlling how much that joint is affected by animations using this mask. Values range from 0.0 (no effect) to 1.0 (full effect). Joints not present in the dictionary are treated as having weight 1.0 (full animation effect).
- [var id: String](skeletonresource/blendmask/id.md)
  The identifier of the blend mask, derived from its name.
### Instance Properties
- [let name: String](skeletonresource/blendmask/name.md)
  The name of the blend mask. Must be unique within the skeleton. Used to identify and reference specific masks within animation systems.

## Relationships

### Conforms To
- [Identifiable](../swift/identifiable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [let animationEvaluation: SkeletonResource.AnimationEvaluation](skeletonresource/animationevaluation-swift.property.md)
  Animation-evaluation data baked into this resource at construction time.
- [SkeletonResource.AnimationEvaluation](skeletonresource/animationevaluation-swift.struct.md)
  A bundle of additional animation-related skeletal data the runtime consumes when evaluating animations against this skeleton.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/skeletonresource/blendmask)*