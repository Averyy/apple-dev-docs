# MDLMeshBufferData

**Framework**: Model I/O  
**Kind**: class

A memory buffer that stores vertex or index data for a Model I/O mesh.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
class MDLMeshBufferData
```

#### Overview

This class is the simplest concrete implementation of the [`MDLMeshBuffer`](mdlmeshbuffer.md) protocol—use this class when you need only a single data store for loading or processing mesh data. To share mesh data for other uses, use another concrete implementation of the [`MDLMeshBuffer`](mdlmeshbuffer.md) protocol—for example, the [`MTKMeshBuffer`](https://developer.apple.com/documentation/MetalKit/MTKMeshBuffer) class shares mesh data with Metal buffers, ensuring that data is copied a minimal number of times between loading, processing, and rendering.If you do not specify a [`MDLMeshBufferAllocator`](mdlmeshbufferallocator.md) object for loading meshes from a file with the [`MDLAsset`](mdlasset.md) class or generating meshes with the [`MDLMesh`](mdlmesh.md) class, Model I/O uses [`MDLMeshBufferData`](mdlmeshbufferdata.md) objects to store mesh data.

## Topics

### Creating a Buffer
- [init(type: MDLMeshBufferType, data: Data?)](mdlmeshbufferdata/init(type:data:).md)
  Initializes a buffer containing the specified data.
- [init(type: MDLMeshBufferType, length: Int)](mdlmeshbufferdata/init(type:length:).md)
  Initializes a buffer of the specified length.
### Accessing a Buffer’s Data
- [var data: Data](mdlmeshbufferdata/data.md)
  The underlying data storage for the mesh buffer.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [MDLMeshBuffer](mdlmeshbuffer.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [protocol MDLMeshBuffer](mdlmeshbuffer.md)
  The general interface for managing storage of vertex and index data used in loading, processing, and rendering meshes.
- [protocol MDLMeshBufferAllocator](mdlmeshbufferallocator.md)
  The general interface for managing allocation of data buffers to be used in loading, processing, and rendering meshes.
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

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlmeshbufferdata)*