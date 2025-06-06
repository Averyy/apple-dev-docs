# MTKMesh

**Framework**: MetalKit  
**Kind**: class

A container for the vertex data of a Model I/O mesh, suitable for use in a Metal app.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
class MTKMesh
```

## Topics

### Initialization
- [init(mesh: MDLMesh, device: any MTLDevice) throws](mtkmesh/init(mesh:device:).md)
  Initializes a MetalKit mesh and its submeshes from a Model I/O mesh.
### Loading Meshes from an Asset
- [class func newMeshes(asset: MDLAsset, device: any MTLDevice) throws -> (modelIOMeshes: [MDLMesh], metalKitMeshes: [MTKMesh])](mtkmesh/newmeshes(asset:device:).md)
### Submeshes
- [var submeshes: [MTKSubmesh]](mtkmesh/submeshes.md)
  An array of submeshes containing index buffers referencing the mesh vertices.
### Vertex Properties
- [var vertexBuffers: [MTKMeshBuffer]](mtkmesh/vertexbuffers.md)
  An array of buffers in which mesh vertex data resides.
- [var vertexCount: Int](mtkmesh/vertexcount.md)
  The number of vertices in the vertex buffers.
- [var vertexDescriptor: MDLVertexDescriptor](mtkmesh/vertexdescriptor.md)
  A Model I/O vertex descriptor specifying the data layout in the vertex buffers.
### Identifying Properties
- [var name: String](mtkmesh/name.md)
  The name of the mesh.
### Constants
- [Mesh Error Handling](mesh-error-handling.md)
  Strings used when handling [`NSError`](https://developer.apple.com/documentation/Foundation/NSError) messages returned from a mesh initialization method.

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

- [class MTKMeshBuffer](mtkmeshbuffer.md)
  A buffer that backs the vertex data of a Model I/O mesh, suitable for use in a Metal app.
- [class MTKMeshBufferAllocator](mtkmeshbufferallocator.md)
  An interface for allocating a MetalKit buffer that backs the vertex data of a Model I/O mesh, suitable for use in a Metal app.
- [class MTKSubmesh](mtksubmesh.md)
  A container for the index data of a Model I/O submesh, suitable for use in a Metal app.
- [Conversion Functions](conversion-functions.md)
  Convert between Metal and Model I/O vertex representations.
- [Model Errors](model-errors.md)
  Learn about errors thrown by model handling methods.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalkit/mtkmesh)*