# MeshPartCollection

**Framework**: RealityKit  
**Kind**: struct  
**Role**: Structure

An object that holds a collection of mesh parts.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 26.0+
- visionOS

## Declaration

```swift
struct MeshPartCollection
```

## Topics

### Creating a collection
- [init()](./meshpartcollection/init%28%29.md)
- [init([MeshResource.Part])](./meshpartcollection/init%28_%29.md)
### Using the collection
- [func insert(MeshResource.Part) -> Bool](./meshpartcollection/insert%28_%29.md)
  Add a new part to the container. Returns true if added. Returns false if it already exists.
- [func remove(id: String) -> MeshResource.Part?](./meshpartcollection/remove%28id%29.md)
  Remove a part by id.
- [func removeAll()](./meshpartcollection/removeall%28%29.md)
  Remove all the parts.
- [func update(MeshResource.Part) -> MeshResource.Part?](./meshpartcollection/update%28_%29.md)
  Update an existing part. The old part is returned.
### Instance Properties
- [var count: Int](./meshpartcollection/count.md)
  Number of parts.
- [var isEmpty: Bool](./meshpartcollection/isempty.md)
  True if there are no parts.
### Subscripts
- [subscript(String) -> MeshResource.Part?](./meshpartcollection/subscript%28_%29.md)
  Read a part given its id.

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
- [struct MeshModelCollection](./meshmodelcollection.md)
  An object that holds a collection of mesh models.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/meshpartcollection)*