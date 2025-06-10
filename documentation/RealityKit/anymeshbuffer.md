# AnyMeshBuffer

**Framework**: RealityKit  
**Kind**: struct

Mesh buffer stored in the container.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 26.0+ (Beta)
- visionOS ?+

## Declaration

```swift
struct AnyMeshBuffer
```

## Topics

### Inspecting a mesh buffer
- [var count: Int](anymeshbuffer/count.md)
- [var elementType: MeshBuffers.ElementType](anymeshbuffer/elementtype.md)
- [var id: MeshBuffers.Identifier](anymeshbuffer/id.md)
- [var rate: MeshBuffers.Rate](anymeshbuffer/rate.md)
- [func get<Value>(Value.Type) -> MeshBuffer<Value>?](anymeshbuffer/get(_:).md)

## See Also

- [struct MeshBuffer](meshbuffer.md)
  Mesh buffer containing elements of any type.
- [protocol MeshBufferContainer](meshbuffercontainer.md)
  Conforming objects contain a table of mesh buffers.
- [protocol MeshBufferSemantic](meshbuffersemantic.md)
  A protocol that holds an identifier value for mesh buffers.
- [enum MeshBuffers](meshbuffers.md)
  An object that holds the data for an model entity’s mesh.
- [struct MeshInstanceCollection](meshinstancecollection.md)
  An object that holds a collection of mesh resource instances.
- [struct MeshModelCollection](meshmodelcollection.md)
  An object that holds a collection of mesh models.
- [struct MeshPartCollection](meshpartcollection.md)
  An object that holds a collection of mesh parts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/anymeshbuffer)*