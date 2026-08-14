# SkeletonResource.Joint

**Framework**: RealityKit  
**Kind**: struct

Describes a single joint of a `Skeleton`

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct Joint
```

#### Overview

Joints form the hierarchical structure of a skeleton. Each joint has a unique name, a rest pose transform relative to its parent, and an optional list of child joints. The hierarchy is expressed through nesting using the `JointBuilder` result builder.

```swift
typealias Joint = SkeletonResource.Joint
// Create a simple arm hierarchy
let arm = try Joint("shoulder") {
    try Joint("upperArm", restPoseTransform: Transform(translation: [0, -0.3, 0])) {
        try Joint("forearm", restPoseTransform: Transform(translation: [0, -0.3, 0]))
    }
}
```

## Topics

### Creating a joint
- [init(String, restPoseTransform: Transform, children: () throws -> [SkeletonResource.Joint]) throws](skeletonresource/joint/init(_:restposetransform:children:).md)
  Creates a joint with the provided name, rest pose transform, and optional children.
### Inspecting a joint
- [var id: String](skeletonresource/joint/id.md)
  The identifier of the joint, automatically derived from the joint name.
- [var restPoseTransform: Transform](skeletonresource/joint/restposetransform.md)
  The rest pose transform of the joint. Defines position, rotation, and scale relative to the parent joint in local space. Used as the reference pose for all animations and deformations.
- [let children: [SkeletonResource.Joint]](skeletonresource/joint/children.md)
  The child joints of this joint. All children must have unique names within the same parent. `JointBuilder` preserves the order children are declared in the closure body, so iteration over `children` is deterministic.
### Instance Properties
- [let name: String](skeletonresource/joint/name.md)
  The unique name of the joint. Names should be unique within a skeleton.

## Relationships

### Conforms To
- [Identifiable](../swift/identifiable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [var rootJoint: SkeletonResource.Joint](skeletonresource/rootjoint.md)
  The root joint of the skeleton hierarchy.
- [SkeletonResource.JointBuilder](skeletonresource/jointbuilder.md)
  A result builder for declaratively constructing the children of a joint.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/skeletonresource/joint)*