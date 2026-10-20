# MDLMeshBufferAllocator

**Framework**: Model I/O  
**Kind**: protocol  
**Role**: Protocol

The general interface for managing allocation of data buffers to be used in loading, processing, and rendering meshes.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
protocol MDLMeshBufferAllocator : NSObjectProtocol
```

```objc
@protocol MDLMeshBufferAllocator <NSObject>
```

#### Overview

Classes adopting this protocol provide different ways of handling mesh buffer data. For example, the [`MTKMeshBufferAllocator`](../MetalKit/mtkmeshbufferallocator.md) class can share mesh data with Metal buffers for use in rendering.

When you load meshes from a file with the [`MDLAsset`](./mdlasset.md) class or generate meshes with the [`MDLMesh`](./mdlmesh.md) class, you must specify an allocator. By choosing an allocator specific to how you use a mesh, you can ensure that vertex and index data for the mesh is copied and transformed a minimal number of times between loading and use.

## Topics

### Allocating Mesh Buffers
- [func newZone(Int) -> any MDLMeshBufferZone](./mdlmeshbufferallocator/newzone%28_%29.md)
  Creates a zone for related memory allocations.
- [func newZoneForBuffers(withSize: [NSNumber], andType: [NSNumber]) -> any MDLMeshBufferZone](./mdlmeshbufferallocator/newzoneforbuffers%28withsize,andtype%29.md)
  Creates a zone large enough to fit the specified group of allocation sizes.
- [func newBuffer(Int, type: MDLMeshBufferType) -> any MDLMeshBuffer](./mdlmeshbufferallocator/newbuffer%28_,type%29.md)
  Creates a new buffer of the specified length.
- [func newBuffer(from: (any MDLMeshBufferZone)?, length: Int, type: MDLMeshBufferType) -> (any MDLMeshBuffer)?](./mdlmeshbufferallocator/newbuffer%28from,length,type%29.md)
  Creates a new buffer of the specified length in the specified zone.
- [func newBuffer(with: Data, type: MDLMeshBufferType) -> any MDLMeshBuffer](./mdlmeshbufferallocator/newbuffer%28with,type%29.md)
  Creates a new buffer containing the specified data.
- [func newBuffer(from: (any MDLMeshBufferZone)?, data: Data, type: MDLMeshBufferType) -> (any MDLMeshBuffer)?](./mdlmeshbufferallocator/newbuffer%28from,data,type%29.md)
  Creates a new buffer containing the specified data in the specified zone.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
### Conforming Types
- [MDLMeshBufferDataAllocator](./mdlmeshbufferdataallocator.md)

## See Also

### Managing Mesh Data
- [protocol MDLMeshBuffer](./mdlmeshbuffer.md)
  The general interface for managing storage of vertex and index data used in loading, processing, and rendering meshes.
- [class MDLMeshBufferData](./mdlmeshbufferdata.md)
  A memory buffer that stores vertex or index data for a Model I/O mesh.
- [class MDLMeshBufferDataAllocator](./mdlmeshbufferdataallocator.md)
  A basic allocator implementation that allocates from main memory using data objects.
- [class MDLMeshBufferMap](./mdlmeshbuffermap.md)
  An object that manages access to a memory buffer used for the data storage of a Model I/O mesh.
- [protocol MDLMeshBufferZone](./mdlmeshbufferzone.md)
  The general interface for logical pools of memory used in allocation of related mesh data buffers.
- [class MDLMeshBufferZoneDefault](./mdlmeshbufferzonedefault.md)
  A standard implementation of the [`MDLMeshBufferZone`](./mdlmeshbufferzone.md) protocol.
- [class MDLVertexAttribute](./mdlvertexattribute.md)
  A description of the format of per-vertex data for a single vertex attribute in a mesh object.
- [class MDLVertexAttributeData](./mdlvertexattributedata.md)
  An object that provides convenience access to vertex data for a specific vertex attribute of a mesh.
- [class MDLVertexBufferLayout](./mdlvertexbufferlayout.md)
  A [`MDLVertexBufferLayout`](./mdlvertexbufferlayout.md) object describes layout information for a vertex buffer in a [`MDLMesh`](./mdlmesh.md) object. A collection of vertex layer objects, vertex attribute objects, and additional information forms a [`MDLVertexDescriptor`](./mdlvertexdescriptor.md) object, which completely describes the layout of vertex buffers for a mesh.
- [class MDLVertexDescriptor](./mdlvertexdescriptor.md)
  A description of the structure, format, and layout for vertex data buffers associated with a mesh.


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlmeshbufferallocator)*