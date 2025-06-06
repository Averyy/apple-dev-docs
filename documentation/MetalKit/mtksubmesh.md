# MTKSubmesh

**Framework**: MetalKit  
**Kind**: class

A container for the index data of a Model I/O submesh, suitable for use in a Metal app.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
class MTKSubmesh
```

#### Overview

The [`MTKSubmesh`](mtksubmesh.md) class provides a container for a segment of mesh data that can be rendered in a single draw call. A submesh can only be initialized as part of a [`MTKMesh`](mtkmesh.md) object. Each submesh contains an index buffer with which the parent’s mesh data can be rendered. Actual submesh vertex data resides in the submesh’s parent mesh. For more information on Model I/O submeshes, see [`MDLSubmesh`](https://developer.apple.com/documentation/ModelIO/MDLSubmesh).

## Topics

### Parent Mesh
- [var mesh: MTKMesh?](mtksubmesh/mesh.md)
  The parent mesh containing the vertex data of this submesh.
### Properties used to Draw Indexed Primitives
- [var indexBuffer: MTKMeshBuffer](mtksubmesh/indexbuffer.md)
  The index buffer used to render the submesh object.
- [var indexCount: Int](mtksubmesh/indexcount.md)
  The number of indices in the index buffer.
- [var indexType: MTLIndexType](mtksubmesh/indextype.md)
  The type of index data in the index buffer.
- [var primitiveType: MTLPrimitiveType](mtksubmesh/primitivetype.md)
  The primitive type with which to draw the submesh object.
### Identifying Properties
- [var name: String](mtksubmesh/name.md)
  The name of the submesh.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class MTKMesh](mtkmesh.md)
  A container for the vertex data of a Model I/O mesh, suitable for use in a Metal app.
- [class MTKMeshBuffer](mtkmeshbuffer.md)
  A buffer that backs the vertex data of a Model I/O mesh, suitable for use in a Metal app.
- [class MTKMeshBufferAllocator](mtkmeshbufferallocator.md)
  An interface for allocating a MetalKit buffer that backs the vertex data of a Model I/O mesh, suitable for use in a Metal app.
- [Conversion Functions](conversion-functions.md)
  Convert between Metal and Model I/O vertex representations.
- [Model Errors](model-errors.md)
  Learn about errors thrown by model handling methods.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalkit/mtksubmesh)*