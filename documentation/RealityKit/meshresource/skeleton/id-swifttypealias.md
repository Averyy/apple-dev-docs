# MeshResource.Skeleton.ID

**Framework**: RealityKit  
**Kind**: typealias

A type representing the stable identity of the entity associated with an instance.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 1.0+

## Declaration

```swift
typealias ID = String
```

## See Also

- [MeshResource.Skeleton](meshresource/skeleton.md)
  A skeleton consists of a hierarchy of joints. Each joint defines a coordinate space. Portions of a model may be thought of as having a position in a joint’s local space.
- [MeshResource.Skeleton.Joint](meshresource/skeleton/joint.md)
  A named joint in a [`MeshResource.Skeleton`](meshresource/skeleton.md).
- [struct MeshSkeletonCollection](meshskeletoncollection.md)
  An object that holds a collection of skeletons used by a mesh resource.
- [struct MeshJointInfluence](meshjointinfluence.md)
  A binding to a joint, which consists of the joint’s index and the weight of that joint’s influence on a vertex.
- [MeshResource.JointInfluences](meshresource/jointinfluences.md)
  A buffer of vertex-joint influences which bind the mesh part’s vertices to a skeleton via a skinning deformation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/meshresource/skeleton/id-swift.typealias)*