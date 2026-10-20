# MeshSkeletonCollection

**Framework**: RealityKit  
**Kind**: struct  
**Role**: Structure

An object that holds a collection of skeletons used by a mesh resource.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+
- visionOS 1.0+

## Declaration

```swift
struct MeshSkeletonCollection
```

## Topics

### Initializers
- [init()](./meshskeletoncollection/init%28%29.md)
- [init([MeshResource.Skeleton])](./meshskeletoncollection/init%28_%29.md)
### Instance Properties
- [var count: Int](./meshskeletoncollection/count.md)
  Number of skeletons.
- [var isEmpty: Bool](./meshskeletoncollection/isempty.md)
  True if there are no skeletons.
### Instance Methods
- [func insert(MeshResource.Skeleton) -> Bool](./meshskeletoncollection/insert%28_%29.md)
  Add a new skeleton to the container. Returns true if added. Returns false if it already exists.
- [func remove(id: String) -> MeshResource.Skeleton?](./meshskeletoncollection/remove%28id%29.md)
  Remove a skeleton by id.
- [func removeAll()](./meshskeletoncollection/removeall%28%29.md)
  Remove all the skeletons.
- [func update(MeshResource.Skeleton) -> MeshResource.Skeleton?](./meshskeletoncollection/update%28_%29.md)
  Update an existing skeleton. The old instance is returned.
### Subscripts
- [subscript(String) -> MeshResource.Skeleton?](./meshskeletoncollection/subscript%28_%29.md)
  Read a skeleton given its id.

## Relationships

### Conforms To
- [Collection](../Swift/collection.md)
- [Copyable](../Swift/copyable.md)
- [Escapable](../Swift/escapable.md)
- [ExpressibleByArrayLiteral](../Swift/expressiblebyarrayliteral.md)
- [Sequence](../Swift/sequence.md)

## See Also

### Mesh skeletons
- [MeshResource.Skeleton](./meshresource/skeleton.md)
  A skeleton consists of a hierarchy of joints. Each joint defines a coordinate space. Portions of a model may be thought of as having a position in a joint’s local space.
- [MeshResource.Skeleton.Joint](./meshresource/skeleton/joint.md)
  A named joint in a [`MeshResource.Skeleton`](./meshresource/skeleton.md).
- [struct MeshJointInfluence](./meshjointinfluence.md)
  A binding to a joint, which consists of the joint’s index and the weight of that joint’s influence on a vertex.
- [MeshResource.JointInfluences](./meshresource/jointinfluences.md)
  A buffer of vertex-joint influences which bind the mesh part’s vertices to a skeleton via a skinning deformation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/meshskeletoncollection)*