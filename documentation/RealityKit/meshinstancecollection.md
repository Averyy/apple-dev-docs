# MeshInstanceCollection

**Framework**: RealityKit  
**Kind**: struct

An object that holds a collection of mesh resource instances.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 26.0+
- visionOS ?+

## Declaration

```swift
struct MeshInstanceCollection
```

## Topics

### Creating a collection
- [init()](meshinstancecollection/init.md)
- [init([MeshResource.Instance])](meshinstancecollection/init(_:).md)
### Using the collection
- [func insert(MeshResource.Instance) -> Bool](meshinstancecollection/insert(_:).md)
  Add a new instance to the container. Returns true if added. Returns false if it already exists.
- [func remove(id: String) -> MeshResource.Instance?](meshinstancecollection/remove(id:).md)
  Remove an instance by name.
- [func removeAll()](meshinstancecollection/removeall.md)
  Remove all the instances.
- [func update(MeshResource.Instance) -> MeshResource.Instance?](meshinstancecollection/update(_:).md)
  Update an existing instance. The old instance is returned.
- [subscript(String) -> MeshResource.Instance?](meshinstancecollection/subscript(_:).md)
  Read an instance given its name.
### Instance Properties
- [var count: Int](meshinstancecollection/count.md)
  Number of instances.
- [var isEmpty: Bool](meshinstancecollection/isempty.md)
  True if there are no instances.

## Relationships

### Conforms To
- [Collection](../swift/collection.md)
- [Copyable](../swift/copyable.md)
- [Escapable](../swift/escapable.md)
- [ExpressibleByArrayLiteral](../swift/expressiblebyarrayliteral.md)
- [Sequence](../swift/sequence.md)

## See Also

- [struct MeshBuffer](meshbuffer.md)
  Mesh buffer containing elements of any type.
- [protocol MeshBufferContainer](meshbuffercontainer.md)
  Conforming objects contain a table of mesh buffers.
- [protocol MeshBufferSemantic](meshbuffersemantic.md)
  A protocol that holds an identifier value for mesh buffers.
- [enum MeshBuffers](meshbuffers.md)
  An object that holds the data for an model entity’s mesh.
- [struct AnyMeshBuffer](anymeshbuffer.md)
  Mesh buffer stored in the container.
- [struct MeshModelCollection](meshmodelcollection.md)
  An object that holds a collection of mesh models.
- [struct MeshPartCollection](meshpartcollection.md)
  An object that holds a collection of mesh parts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/meshinstancecollection)*