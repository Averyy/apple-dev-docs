# SkeletalPosesComponent

**Framework**: RealityKit  
**Kind**: struct

A component that exposes the collection of named animation skeletal poses.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+
- visionOS 2.0+

## Declaration

```swift
struct SkeletalPosesComponent
```

#### Overview

Use the entity’s skeletal poses to either read the pose evaluated from animations bound to [`BindTarget.jointTransforms`](bindtarget/jointtransforms.md) and [`BindTarget.skeletalPose(_:)`](bindtarget/skeletalpose(_:).md), or write your own pose to animate the skeletal model.

##### Setting Updated Value on an Entity

When an updated [`SkeletalPose`](skeletalpose.md) is set on an entity as part of this component, these rules are followed:

- If [`jointNames`](skeletalpose/jointnames.md) is reordered, following animation updated will match the new order.
- If [`jointTransforms`](skeletalpose/jointtransforms.md) contains more elements than [`jointNames`](skeletalpose/jointnames.md), the extra transformations are ignored.
- If [`jointTransforms`](skeletalpose/jointtransforms.md) contains less elements than [`jointNames`](skeletalpose/jointnames.md), the extra joint transformations are not updated.

You can use [`poses`](skeletalposescomponent/poses.md)’s [`default`](skeletalposeset/default.md) accessor for the same skeletal pose as exposed by [`jointNames`](hasmodel/jointnames.md) and [`jointTransforms`](hasmodel/jointtransforms.md). The access trough the component allows the reordering, addition and removal of joints from the default pose.

## Topics

### Initializers
- [init(poses: [SkeletalPose])](skeletalposescomponent/init(poses:).md)
  Creates a component value with the provided poses.
### Instance Properties
- [var poses: SkeletalPoseSet](skeletalposescomponent/poses.md)
  The collection of the skeletal poses for a single entity.

## Relationships

### Conforms To
- [Component](component.md)

## See Also

- [struct SkeletalPose](skeletalpose.md)
  A container that holds the position and orientation of each joint in a single animation skeleton.
- [struct SkeletalPoseSet](skeletalposeset.md)
  A collection of named skeletal poses.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/skeletalposescomponent)*