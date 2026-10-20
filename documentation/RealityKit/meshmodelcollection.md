# MeshModelCollection

**Framework**: RealityKit  
**Kind**: struct  
**Role**: Structure

An object that holds a collection of mesh models.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 26.0+
- visionOS

## Declaration

```swift
struct MeshModelCollection
```

## Topics

### Creating a collection
- [init()](./meshmodelcollection/init%28%29.md)
- [init([MeshResource.Model])](./meshmodelcollection/init%28_%29.md)
### Using the collection
- [func insert(MeshResource.Model) -> Bool](./meshmodelcollection/insert%28_%29.md)
  Add a new model to the container. Returns true if added. Returns false if it already exists.
- [func remove(id: String) -> MeshResource.Model?](./meshmodelcollection/remove%28id%29.md)
  Remove a model by id.
- [func removeAll()](./meshmodelcollection/removeall%28%29.md)
  Remove all the models.
- [func update(MeshResource.Model) -> MeshResource.Model?](./meshmodelcollection/update%28_%29.md)
  Update an existing model. The old model is returned.
- [subscript(String) -> MeshResource.Model?](./meshmodelcollection/subscript%28_%29.md)
  Read a model given its id.
### Instance Properties
- [var count: Int](./meshmodelcollection/count.md)
  Number of models.
- [var isEmpty: Bool](./meshmodelcollection/isempty.md)
  True if there are no models.

## Relationships

### Conforms To
- [Collection](../Swift/collection.md)
- [Copyable](../Swift/copyable.md)
- [Escapable](../Swift/escapable.md)
- [ExpressibleByArrayLiteral](../Swift/expressiblebyarrayliteral.md)
- [Sequence](../Swift/sequence.md)

## See Also

### Mesh description
- [struct MeshBuffer](./meshbuffer.md)
  Mesh buffer containing elements of any type.
- [protocol MeshBufferContainer](./meshbuffercontainer.md)
  Conforming objects contain a table of mesh buffers.
- [protocol MeshBufferSemantic](./meshbuffersemantic.md)
  A protocol that holds an identifier value for mesh buffers.
- [enum MeshBuffers](./meshbuffers.md)
  An object that holds the data for an model entity’s mesh.
- [struct AnyMeshBuffer](./anymeshbuffer.md)
  Mesh buffer stored in the container.
- [struct MeshInstanceCollection](./meshinstancecollection.md)
  An object that holds a collection of mesh resource instances.
- [struct MeshPartCollection](./meshpartcollection.md)
  An object that holds a collection of mesh parts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/meshmodelcollection)*