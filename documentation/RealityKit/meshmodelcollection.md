# MeshModelCollection

**Framework**: RealityKit  
**Kind**: struct

An object that holds a collection of mesh models.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- visionOS ?+

## Declaration

```swift
struct MeshModelCollection
```

## Topics

### Creating a collection
- [init()](meshmodelcollection/init.md)
- [init([MeshResource.Model])](meshmodelcollection/init(_:).md)
### Using the collection
- [var count: Int](meshmodelcollection/count.md)
  Number of models.
- [var isEmpty: Bool](meshmodelcollection/isempty.md)
  True if there are no models.
- [func insert(MeshResource.Model) -> Bool](meshmodelcollection/insert(_:).md)
  Add a new model to the container. Returns true if added.
- [func remove(id: String) -> MeshResource.Model?](meshmodelcollection/remove(id:).md)
  Remove a model by id.
- [func removeAll()](meshmodelcollection/removeall.md)
  Remove all the models.
- [func update(MeshResource.Model) -> MeshResource.Model?](meshmodelcollection/update(_:).md)
  Update an existing model. The old model is returned.
- [subscript(String) -> MeshResource.Model?](meshmodelcollection/subscript(_:)-5xuaf.md)
  Read a model given its id.
### Default Implementations
- [Collection Implementations](meshmodelcollection/collection-implementations.md)
- [ExpressibleByArrayLiteral Implementations](meshmodelcollection/expressiblebyarrayliteral-implementations.md)
- [Sequence Implementations](meshmodelcollection/sequence-implementations.md)

## Relationships

### Conforms To
- [Collection](../Swift/Collection.md)
- [Copyable](../Swift/Copyable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [Sequence](../Swift/Sequence.md)

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
- [struct MeshInstanceCollection](meshinstancecollection.md)
  An object that holds a collection of mesh resource instances.
- [struct MeshPartCollection](meshpartcollection.md)
  An object that holds a collection of mesh parts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/meshmodelcollection)*