# MeshResource.Skeleton.Joint

**Framework**: RealityKit  
**Kind**: struct

A named joint in a [`MeshResource.Skeleton`](meshresource/skeleton.md).

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+
- visionOS 1.0+

## Declaration

```swift
struct Joint
```

## Topics

### Initializers
- [init(name: String, parentIndex: Int?, inverseBindPoseMatrix: simd_float4x4, restPoseTransform: Transform)](meshresource/skeleton/joint/init(name:parentindex:inversebindposematrix:restposetransform:).md)
  Creates a single joint in a skeleton.
### Instance Properties
- [var inverseBindPoseMatrix: simd_float4x4](meshresource/skeleton/joint/inversebindposematrix.md)
  A matrix which transforms from the authored pose (the “bind pose”) of the bound model to the local space of this joint.
- [var name: String](meshresource/skeleton/joint/name.md)
  The name of this joint.
- [var parentIndex: Int?](meshresource/skeleton/joint/parentindex.md)
  The index of this joint’s parent, or nil if this joint has no parent.
- [var restPoseTransform: Transform](meshresource/skeleton/joint/restposetransform.md)
  The local transform of this joint in skeleton’s rest pose, specified relative to this joint’s parent (or relative to model space, if this joint has no parent).

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)

## See Also

- [MeshResource.Skeleton](meshresource/skeleton.md)
  A skeleton consists of a hierarchy of joints. Each joint defines a coordinate space. Portions of a model may be thought of as having a position in a joint’s local space.
- [struct MeshSkeletonCollection](meshskeletoncollection.md)
  An object that holds a collection of skeletons used by a mesh resource.
- [struct MeshJointInfluence](meshjointinfluence.md)
  A binding to a joint, which consists of the joint’s index and the weight of that joint’s influence on a vertex.
- [MeshResource.JointInfluences](meshresource/jointinfluences.md)
  A buffer of vertex-joint influences which bind the mesh part’s vertices to a skeleton via a skinning deformation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/meshresource/skeleton/joint)*