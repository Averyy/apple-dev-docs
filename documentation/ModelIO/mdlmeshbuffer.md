# MDLMeshBuffer

**Framework**: Model I/O  
**Kind**: protocol

The general interface for managing storage of vertex and index data used in loading, processing, and rendering meshes.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
protocol MDLMeshBuffer : NSCopying, NSObjectProtocol
```

#### Overview

Model I/O creates buffers using an allocator that you specify when loading mesh data from a file with the [`MDLAsset`](mdlasset.md) class or generating meshes with the [`MDLMesh`](mdlmesh.md) class. You can also create buffers using an allocator method such as [`newBuffer(with:type:)`](mdlmeshbufferallocator/newbuffer(with:type:).md). The allocator you choose determines the concrete class of a mesh buffer and thus its storage mechanism—for example, the MetalKit [`MTKMeshBufferAllocator`](https://developer.apple.com/documentation/MetalKit/MTKMeshBufferAllocator) class allocates [`MTKMeshBuffer`](https://developer.apple.com/documentation/MetalKit/MTKMeshBuffer) objects, which share storage with Metal buffers for use in rendering.

## Topics

### Working with Data in a Buffer
- [func fill(Data, offset: Int)](mdlmeshbuffer/fill(_:offset:).md)
  Writes the specified data into the buffer.
- [func map() -> MDLMeshBufferMap](mdlmeshbuffer/map.md)
  Provides direct, read-only access to the buffer’s contents.
- [var length: Int](mdlmeshbuffer/length.md)
  The data size of the buffer, in bytes.
### Inspecting a Buffer
- [var allocator: any MDLMeshBufferAllocator](mdlmeshbuffer/allocator.md)
  The allocator object that created the buffer.
- [var zone: any MDLMeshBufferZone](mdlmeshbuffer/zone.md)
  The memory pool from which the buffer was created.
- [var type: MDLMeshBufferType](mdlmeshbuffer/type.md)
  The type of data contained in a buffer.
### Constants
- [enum MDLMeshBufferType](mdlmeshbuffertype.md)
  Options for the content of a mesh buffer, used by the [`type`](mdlmeshbuffer/type.md) property and by [`MDLMeshBufferAllocator`](mdlmeshbufferallocator.md) methods for creating buffers.

## Relationships

### Inherits From
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
### Conforming Types
- [MDLMeshBufferData](mdlmeshbufferdata.md)

## See Also

- [protocol MDLMeshBufferAllocator](mdlmeshbufferallocator.md)
  The general interface for managing allocation of data buffers to be used in loading, processing, and rendering meshes.
- [class MDLMeshBufferData](mdlmeshbufferdata.md)
  A memory buffer that stores vertex or index data for a Model I/O mesh.
- [class MDLMeshBufferDataAllocator](mdlmeshbufferdataallocator.md)
  A basic allocator implementation that allocates from main memory using data objects.
- [class MDLMeshBufferMap](mdlmeshbuffermap.md)
  An object that manages access to a memory buffer used for the data storage of a Model I/O mesh.
- [protocol MDLMeshBufferZone](mdlmeshbufferzone.md)
  The general interface for logical pools of memory used in allocation of related mesh data buffers.
- [class MDLMeshBufferZoneDefault](mdlmeshbufferzonedefault.md)
  A standard implementation of the [`MDLMeshBufferZone`](mdlmeshbufferzone.md) protocol.
- [class MDLVertexAttribute](mdlvertexattribute.md)
  A description of the format of per-vertex data for a single vertex attribute in a mesh object.
- [class MDLVertexAttributeData](mdlvertexattributedata.md)
  An object that provides convenience access to vertex data for a specific vertex attribute of a mesh.
- [class MDLVertexBufferLayout](mdlvertexbufferlayout.md)
  A [`MDLVertexBufferLayout`](mdlvertexbufferlayout.md) object describes layout information for a vertex buffer in a [`MDLMesh`](mdlmesh.md) object. A collection of vertex layer objects, vertex attribute objects, and additional information forms a [`MDLVertexDescriptor`](mdlvertexdescriptor.md) object, which completely describes the layout of vertex buffers for a mesh.
- [class MDLVertexDescriptor](mdlvertexdescriptor.md)
  A description of the structure, format, and layout for vertex data buffers associated with a mesh.


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlmeshbuffer)*