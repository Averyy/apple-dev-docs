# MDLMeshBufferMap

**Framework**: Model I/O  
**Kind**: class

An object that manages access to a memory buffer used for the data storage of a Model I/O mesh.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
class MDLMeshBufferMap
```

#### Overview

Typically, you do not create [`MDLMeshBufferMap`](mdlmeshbuffermap.md) objects directly. Instead, you use classes supporting the [`MDLMeshBuffer`](mdlmeshbuffer.md) protocol to manage mesh buffer memory shared with a rendering technology—for example, the [`MTKMeshBuffer`](https://developer.apple.com/documentation/MetalKit/MTKMeshBuffer) class for rendering with Metal. A mesh buffer object vends a [`MDLMeshBufferMap`](mdlmeshbuffermap.md) objects when you use the [`map()`](mdlmeshbuffer/map().md) method to gain temporary access to the shared memory.

> ❗ **Important**:  When you use a mesh buffer’s [`map()`](mdlmeshbuffer/map().md) method, the buffer remains mapped for as long as that [`MDLMeshBufferMap`](mdlmeshbuffermap.md) object exists. Mapping a buffer may impose restrictions on a system. For example, a buffer in shared GPU memory may be unavailable for rendering while mapped, causing draw calls that use the buffer to fail until the corresponding [`MDLMeshBufferMap`](mdlmeshbuffermap.md) object is deallocated.

 When you use a mesh buffer’s [`map()`](mdlmeshbuffer/map().md) method, the buffer remains mapped for as long as that [`MDLMeshBufferMap`](mdlmeshbuffermap.md) object exists. Mapping a buffer may impose restrictions on a system. For example, a buffer in shared GPU memory may be unavailable for rendering while mapped, causing draw calls that use the buffer to fail until the corresponding [`MDLMeshBufferMap`](mdlmeshbuffermap.md) object is deallocated.

## Topics

### Creating a Buffer Map
- [init(bytes: UnsafeMutableRawPointer, deallocator: (() -> Void)?)](mdlmeshbuffermap/init(bytes:deallocator:).md)
  Initializes a buffer map object to manage access to the specified memory.
### Accessing Buffer Data
- [var bytes: UnsafeMutableRawPointer](mdlmeshbuffermap/bytes.md)
  A pointer to the mutable memory managed by the buffer map.

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

- [protocol MDLMeshBuffer](mdlmeshbuffer.md)
  The general interface for managing storage of vertex and index data used in loading, processing, and rendering meshes.
- [protocol MDLMeshBufferAllocator](mdlmeshbufferallocator.md)
  The general interface for managing allocation of data buffers to be used in loading, processing, and rendering meshes.
- [class MDLMeshBufferData](mdlmeshbufferdata.md)
  A memory buffer that stores vertex or index data for a Model I/O mesh.
- [class MDLMeshBufferDataAllocator](mdlmeshbufferdataallocator.md)
  A basic allocator implementation that allocates from main memory using data objects.
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

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlmeshbuffermap)*