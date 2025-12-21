# SkeletalPose

**Framework**: RealityKit  
**Kind**: struct

A container that holds the position and orientation of each joint in a single animation skeleton.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+
- visionOS 2.0+

## Declaration

```swift
struct SkeletalPose
```

#### Overview

Each index in [`jointNames`](skeletalpose/jointnames.md) directly corresponds to the same index in [`jointTransforms`](skeletalpose/jointtransforms.md), linking each joint name to its respective transform.

## Topics

### Initializers
- [init(id: SkeletalPose.ID, from: MeshResource.Skeleton)](skeletalpose/init(id:from:).md)
  Creates a skeletal pose from the rest pose of the model skeleton.
- [init(id: SkeletalPose.ID, joints: [(String, JointTransforms.Element)])](skeletalpose/init(id:joints:).md)
  Creates a pose for the joint name and transformation pairs.
### Instance Properties
- [var id: SkeletalPose.ID](skeletalpose/id.md)
  The unique identifier of the pose.
- [var jointNames: [String]](skeletalpose/jointnames.md)
  The names of the joints in the pose in specific order.
- [var jointTransforms: JointTransforms](skeletalpose/jointtransforms.md)
  The transformations of the joints in the pose.
### Subscripts
- [subscript(String) -> Transform?](skeletalpose/subscript(_:).md)
  Accesses a pose transformation using the index of the joint name.

## Relationships

### Conforms To
- [Identifiable](../Swift/Identifiable.md)

## See Also

- [struct SkeletalPosesComponent](skeletalposescomponent.md)
  A component that exposes the collection of named animation skeletal poses.
- [struct SkeletalPoseSet](skeletalposeset.md)
  A collection of named skeletal poses.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/skeletalpose)*