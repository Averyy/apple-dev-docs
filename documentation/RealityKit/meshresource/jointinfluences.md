# MeshResource.JointInfluences

**Framework**: RealityKit  
**Kind**: struct

A buffer of vertex-joint influences which bind the mesh part’s vertices to a skeleton via a skinning deformation.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 1.0+

## Declaration

```swift
struct JointInfluences
```

#### Overview

Each vertex is associated with a fixed number of influences. If `influencesPerVertex` is 4, then there should be four elements in the buffer of joint influences for each vertex in the mesh part.

> **Note**: If a particular vertex needs fewer influences than the `influencesPerVertex` value, the influences for that vertex can be padded with zero-weight influences.

If a particular vertex needs fewer influences than the `influencesPerVertex` value, the influences for that vertex can be padded with zero-weight influences.

## Topics

### Initializers
- [init(influences: MeshBuffers.JointInfluences, influencesPerVertex: Int)](meshresource/jointinfluences/init(influences:influencespervertex:).md)
  Associates every vertex in the mesh with a fixed number of influences per vertex.
### Instance Properties
- [var influences: MeshBuffers.JointInfluences](meshresource/jointinfluences/influences.md)
  Buffer of joint influences.

## See Also

- [MeshResource.Skeleton](meshresource/skeleton.md)
  A skeleton consists of a hierarchy of joints. Each joint defines a coordinate space. Portions of a model may be thought of as having a position in a joint’s local space.
- [MeshResource.Skeleton.Joint](meshresource/skeleton/joint.md)
  A named joint in a [`MeshResource.Skeleton`](meshresource/skeleton.md).
- [MeshResource.Skeleton.ID](meshresource/skeleton/id-swift.typealias.md)
  A type representing the stable identity of the entity associated with an instance.
- [struct MeshSkeletonCollection](meshskeletoncollection.md)
  An object that holds a collection of skeletons used by a mesh resource.
- [struct MeshJointInfluence](meshjointinfluence.md)
  A binding to a joint, which consists of the joint’s index and the weight of that joint’s influence on a vertex.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/meshresource/jointinfluences)*