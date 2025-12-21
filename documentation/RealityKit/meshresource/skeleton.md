# MeshResource.Skeleton

**Framework**: RealityKit  
**Kind**: struct

A skeleton consists of a hierarchy of joints. Each joint defines a coordinate space. Portions of a model may be thought of as having a position in a joint’s local space.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+
- visionOS 1.0+

## Declaration

```swift
struct Skeleton
```

#### Overview

Each joint in a skeleton has a name, which usually determines the joint’s parent. For example, the legs of a human body might include these joints:

- `root`
- `root/hips_joint`
- `root/hips_joint/left_upLeg_joint`
- `root/hips_joint/left_upLeg_joint/left_leg_joint`
- `root/hips_joint/right_upLeg_joint`
- `root/hips_joint/right_upLeg_joint/right_leg_joint`
- etc.

Models with skinned animation are authored in a fixed pose (the “bind pose”). The position of a vertex in a particular joint’s local space is a function of the vertex’s position in the bind pose and an “inverse bind pose” matrix which transforms from the bind pose (model space) to the joint’s local space.

When unanimated, the pose of a skinned model is defined by the rest pose of each joint. This transform is relative to the joint’s parent. Usually, the rest pose of a model is the same as its bind pose.

## Topics

### Structures
- [MeshResource.Skeleton.Joint](meshresource/skeleton/joint.md)
  A named joint in a [`MeshResource.Skeleton`](meshresource/skeleton.md).
### Initializers
- [init?(id: String, jointNames: [String], inverseBindPoseMatrices: [simd_float4x4], restPoseTransforms: [Transform]?, parentIndices: [Int?]?)](meshresource/skeleton/init(id:jointnames:inversebindposematrices:restposetransforms:parentindices:).md)
  Creates a skeleton from arrays which define its joints. Returns `nil` if there was an issue converting the parameters to a valid skeleton.
- [init(id: String, joints: [MeshResource.Skeleton.Joint])](meshresource/skeleton/init(id:joints:).md)
  Creates a skeleton from an array of joints.
### Instance Properties
- [var id: String](meshresource/skeleton/id.md)
  The unique identifier of this skeleton. This acts as a stable identity for this object.
- [var joints: [MeshResource.Skeleton.Joint]](meshresource/skeleton/joints.md)
  The joints which define this skeleton’s hierarchy.

## Relationships

### Conforms To
- [Identifiable](../Swift/Identifiable.md)

## See Also

- [MeshResource.Skeleton.Joint](meshresource/skeleton/joint.md)
  A named joint in a [`MeshResource.Skeleton`](meshresource/skeleton.md).
- [struct MeshSkeletonCollection](meshskeletoncollection.md)
  An object that holds a collection of skeletons used by a mesh resource.
- [struct MeshJointInfluence](meshjointinfluence.md)
  A binding to a joint, which consists of the joint’s index and the weight of that joint’s influence on a vertex.
- [MeshResource.JointInfluences](meshresource/jointinfluences.md)
  A buffer of vertex-joint influences which bind the mesh part’s vertices to a skeleton via a skinning deformation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/meshresource/skeleton)*