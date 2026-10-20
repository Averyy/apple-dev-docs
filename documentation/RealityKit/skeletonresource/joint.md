# SkeletonResource.Joint

**Framework**: RealityKit  
**Kind**: struct  
**Role**: Structure

Describes a single joint of a `Skeleton`

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

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
- [init(String, restPoseTransform: Transform, children: () throws -> [SkeletonResource.Joint]) throws](./joint/init%28_,restposetransform,children%29.md)
  Creates a joint with the provided name, rest pose transform, and optional children.
### Inspecting a joint
- [var id: String](./joint/id.md)
  The identifier of the joint, automatically derived from the joint name.
- [var restPoseTransform: Transform](./joint/restposetransform.md)
  The rest pose transform of the joint. Defines position, rotation, and scale relative to the parent joint in local space. Used as the reference pose for all animations and deformations.
- [let children: [SkeletonResource.Joint]](./joint/children.md)
  The child joints of this joint. All children must have unique names within the same parent. `JointBuilder` preserves the order children are declared in the closure body, so iteration over `children` is deterministic.
### Instance Properties
- [let name: String](./joint/name.md)
  The unique name of the joint. Names should be unique within a skeleton.

## Relationships

### Conforms To
- [Identifiable](../../Swift/identifiable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Defining the joint hierarchy
- [var rootJoint: SkeletonResource.Joint](./rootjoint.md)
  The root joint of the skeleton hierarchy.
- [SkeletonResource.JointBuilder](./jointbuilder.md)
  A result builder for declaratively constructing the children of a joint.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/skeletonresource/joint)*