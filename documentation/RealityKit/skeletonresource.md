# SkeletonResource

**Framework**: RealityKit  
**Kind**: class

A self-contained skeleton asset for animating characters and articulated objects.

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

A `SkeletonResource` encapsulates a skeleton’s joint hierarchy together with optional inverse-kinematics resources and blend masks in a single value. Use a skeleton resource to define the joint structure of a character, then share it with animation-related APIs such as retargeting configurations, IK rigs, and animation graphs.

You create a skeleton resource by providing a name and the root of a joint hierarchy. A skeleton resource is immutable once created — the same instance is safe to reuse anywhere in your app, including from background threads, without copying.

##### Build a Skeleton From a Joint Hierarchy

Build a skeleton’s joint hierarchy using the [`SkeletonResource.Joint`](skeletonresource/joint.md) type and the [`SkeletonResource.JointBuilder`](skeletonresource/jointbuilder.md) result builder. Each joint has a name and a rest-pose transform relative to its parent; nesting joints inside the trailing closure declares parent-child relationships. Joint names must be unique among siblings — the initializer throws an error if any children of the same parent share a name.

```swift
typealias Joint = SkeletonResource.Joint
let skeleton = try SkeletonResource(
    named: "Character",
    rootJoint: try Joint("root") {
        try Joint("spine", restPoseTransform: Transform(translation: [0, 0.1, 0])) {
            try Joint("shoulder", restPoseTransform: Transform(translation: [0, 0.15, 0])) {
                try Joint("upperArm", restPoseTransform: Transform(translation: [0, -0.3, 0])) {
                    try Joint("forearm", restPoseTransform: Transform(translation: [0, -0.3, 0])) {
                        try Joint("hand", restPoseTransform: Transform(translation: [0, -0.2, 0]))
                    }
                }
            }
        }
    }
)
```

##### Add Blend Masks and Inverse Kinematics Resources

Blend masks let you control which joints an animation affects. Inverse-kinematics (IK) resources let the runtime solve joint poses that meet positional or orientational targets — for example, making a hand reach a point in space rather than following only pre-baked motion. Bundle either or both into an [`SkeletonResource.AnimationEvaluation`](skeletonresource/animationevaluation-swift.struct.md) value and supply it when you create the skeleton; that data then stays fixed for the lifetime of the resource. Both lists default to empty if you don’t need them.

Build a blend mask by listing per-joint weights between `0.0` (no animation) and `1.0` (full animation). Joints you don’t list keep the default `1.0`, so one entry is often enough to silence a whole body region:

```swift
let blendMasks: [SkeletonResource.BlendMask] = [
    .init(name: "armOnly", jointWeights: ["shoulder": 0.0]),
    .init(name: "handOnly", jointWeights: ["shoulder": 0.0, "upperArm": 0.0, "forearm": 0.0])
]
```

Build an IK rig from the same joint hierarchy with [`init(named:rootJoint:)`](ikrig/init(named:rootjoint:).md), configure the constraints you need, then wrap the rig in an [`IKResource`](ikresource.md). A skeleton can carry more than one IK resource — for example, one configured for look-at constraints and another for positional constraints — by passing each in the `ikResources` array:

```swift
var rig = try IKRig(named: "armRig", rootJoint: rootJoint)
rig.constraints = [
    .parent(named: "Hand_Task", on: "hand",
            positionWeight: [50, 50, 50],
            orientationWeight: [60, 60, 60])
]
let ikResource = try IKResource(rig: rig)
```

Finally, pass both into the skeleton when you create it:

```swift
let skeleton = try SkeletonResource(
    named: "armSkeleton",
    rootJoint: rootJoint,
    animationEvaluation: .init(ikResources: [ikResource], blendMasks: blendMasks)
)
```

##### Extract a Skeleton From a Loaded Model

To pull a skeleton out of a USD-loaded model for use with the animation APIs, convert the model’s [`MeshResource.Skeleton`](meshresource/skeleton.md) with [`init(from:)`](skeletonresource/init(from:).md).

```swift
let entity = try await Entity.load(named: "Character")
let modelEntity = entity as! ModelEntity
if let meshSkeleton = modelEntity.model?.mesh.contents.skeletons.first {
    let skeleton = try SkeletonResource(from: meshSkeleton)
}
```

##### Use with Retargeting

Pair a source and target `SkeletonResource` to build a retargeting configuration that remaps animations across characters with different joint names or proportions, then process source animations through it. See [`RetargetingConfiguration`](retargetingconfiguration.md) for the full flow and the available matching strategies.

```swift
let config = try RetargetingConfiguration.automatchBiped(sourceSkeleton, to: targetSkeleton)
let retargeted = try sourceAnimation.processAndCreateAnimation(retargeting: config)
```

#### Related Types

- [`SkeletonResource.Joint`](skeletonresource/joint.md) — a single joint in the skeleton hierarchy.
- [`SkeletonResource.AnimationEvaluation`](skeletonresource/animationevaluation-swift.struct.md) — bundle of IK resources and blend masks baked into the resource.
- [`SkeletonResource.BlendMask`](skeletonresource/blendmask.md) — selective per-joint weighting for layered animation control.

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
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [class RetargetingConfiguration](retargetingconfiguration.md)
  A configuration for retargeting skeletal animations between different skeletons.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/skeletonresource)*