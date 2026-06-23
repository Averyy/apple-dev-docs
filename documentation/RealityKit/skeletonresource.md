# SkeletonResource

**Framework**: RealityKit  
**Kind**: class

Represents a skeleton asset with joint hierarchy and animation capabilities.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
final class SkeletonResource
```

#### Overview

`SkeletonResource` is the single type for defining and using skeletons. It encapsulates the joint hierarchy together with additional animation-related skeletal data into one self-contained, immutable animation resource.

#### Basic Usage

Create a skeleton resource with joints and (optionally) animation-evaluation data:

```swift
typealias Joint = SkeletonResource.Joint
let skeleton = try SkeletonResource(
    named: "Character",
    rootJoint: try Joint("Root") {
        try Joint("Spine")
    },
    animationEvaluation: .init(
        ikResources: [ikResource1, ikResource2],
        blendMasks: blendMasks
    )
)
```

#### Related Types

- [`SkeletonResource.Joint`](skeletonresource/joint.md) - Represents a single joint in the skeleton hierarchy
- [`SkeletonResource.AnimationEvaluation`](skeletonresource/animationevaluation-swift.struct.md) - Bundle of additional animation-related skeletal data
- [`SkeletonResource.BlendMask`](skeletonresource/blendmask.md) - Defines selective weighting for joint animation control

## Topics

### Creating a skeleton resource
- [convenience init(named: String, rootJoint: SkeletonResource.Joint, animationEvaluation: SkeletonResource.AnimationEvaluation) throws](skeletonresource/init(named:rootjoint:animationevaluation:).md)
  Creates a skeleton resource with the specified name, joint hierarchy, and animation-evaluation data.
### Defining the joint hierarchy
- [var rootJoint: SkeletonResource.Joint](skeletonresource/rootjoint.md)
  The root joint of the skeleton hierarchy.
- [SkeletonResource.Joint](skeletonresource/joint.md)
  Describes a single joint of a `Skeleton`
- [SkeletonResource.JointBuilder](skeletonresource/jointbuilder.md)
  A result builder for declaratively constructing the children of a joint.
### Configuring animation evaluation
- [let animationEvaluation: SkeletonResource.AnimationEvaluation](skeletonresource/animationevaluation-swift.property.md)
  Animation-evaluation data baked into this resource at construction time.
- [SkeletonResource.AnimationEvaluation](skeletonresource/animationevaluation-swift.struct.md)
  A bundle of additional animation-related skeletal data the runtime consumes when evaluating animations against this skeleton.
- [SkeletonResource.BlendMask](skeletonresource/blendmask.md)
  Describes a single blend mask for selective animation control.
### Initializers
- [convenience init(from: MeshResource.Skeleton) throws](skeletonresource/init(from:).md)
  Creates a skeleton resource from a mesh resource skeleton.
### Instance Properties
- [let name: String](skeletonresource/name.md)
  Fast access to the name of the skeleton.

## Relationships

### Conforms To
- [Resource](resource.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class RetargetingConfiguration](retargetingconfiguration.md)
  A configuration for retargeting skeletal animations between different skeletons.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/skeletonresource)*