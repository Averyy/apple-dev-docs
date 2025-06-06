# MDLVertexBufferLayout

**Framework**: Model I/O  
**Kind**: class

A [`MDLVertexBufferLayout`](mdlvertexbufferlayout.md) object describes layout information for a vertex buffer in a [`MDLMesh`](mdlmesh.md) object. A collection of vertex layer objects, vertex attribute objects, and additional information forms a [`MDLVertexDescriptor`](mdlvertexdescriptor.md) object, which completely describes the layout of vertex buffers for a mesh.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
class MDLVertexBufferLayout
```

#### Overview

A collection of vertex layout objects, vertex attribute objects, and additional information forms a [`MDLVertexDescriptor`](mdlvertexdescriptor.md) object, which completely describes the layout of vertex buffers for a [`MDLMesh`](mdlmesh.md) object.

A mesh may store vertex data in either a structure of arrays model, where data for each vertex attribute (such as vertex position or surface normal) lies in a separate vertex buffer, or in an array of structures model, where multiple vertex attributes share the same buffer.

- In a structure of arrays, the mesh’s [`vertexBuffers`](mdlmesh/vertexbuffers.md) array contains several [`MDLMeshBuffer`](mdlmeshbuffer.md) objects, and the mesh’s [`vertexDescriptor`](mdlmesh/vertexdescriptor.md) object contains a separate [`MDLVertexBufferLayout`](mdlvertexbufferlayout.md) object for each buffer.
- In an array of structures, the mesh contains a single vertex buffer, and its descriptor contains a single vertex buffer layout object. To identify which bytes in the buffer refer to which vertices and vertex attributes, use the layout’s [`stride`](mdlvertexbufferlayout/stride.md) together with the [`format`](mdlvertexattribute/format.md) and [`offset`](mdlvertexattribute/offset.md) properties of the descriptor’s vertex attributes.

Because there is only one stride per buffer:

- If a buffer uses interleaved layout, it can contain attributes of different sizes, and the stride is the sum of their sizes (plus padding).
- If a buffer uses non-interleaved layout (that is, it stores all the data for one attribute, then all the data for another, and so on), each attribute in the buffer must have the same size as the others.

## Topics

### Working with Layout Information
- [var stride: Int](mdlvertexbufferlayout/stride.md)
  The stride, in bytes, between data for separate vertices in a vertex buffer.
### Initializers
- [init(stride: Int)](mdlvertexbufferlayout/init(stride:).md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
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
- [class MDLVertexDescriptor](mdlvertexdescriptor.md)
  A description of the structure, format, and layout for vertex data buffers associated with a mesh.


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlvertexbufferlayout)*