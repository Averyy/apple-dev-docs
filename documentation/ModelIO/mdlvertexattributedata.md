# MDLVertexAttributeData

**Framework**: Model I/O  
**Kind**: class

An object that provides convenience access to vertex data for a specific vertex attribute of a mesh.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
class MDLVertexAttributeData
```

#### Overview

You retrieve a vertex attribute data object by calling the [`vertexAttributeData(forAttributeNamed:)`](mdlmesh/vertexattributedata(forattributenamed:).md) method of a [`MDLMesh`](mdlmesh.md) object, which is shorthand for looking up the the [`MDLMeshBuffer`](mdlmeshbuffer.md) object corresponding to the named attribute and using the [`map()`](mdlmeshbuffer/map().md) method to gain read-only access to its contents.

## Topics

### Accessing Data for a Vertex Attribute
- [var dataStart: UnsafeMutableRawPointer](mdlvertexattributedata/datastart.md)
  The offset, in bytes, from the start of the data to where vertex attribute information begins.
- [var stride: Int](mdlvertexattributedata/stride.md)
  The stride, in bytes, between vertex information for consecutive vertices in the data.
- [var format: MDLVertexFormat](mdlvertexattributedata/format.md)
  The format of per-vertex data for the attribute.
### Instance Properties
- [var bufferSize: Int](mdlvertexattributedata/buffersize.md)
- [var map: MDLMeshBufferMap](mdlvertexattributedata/map.md)

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
- [class MDLMeshBufferMap](mdlmeshbuffermap.md)
  An object that manages access to a memory buffer used for the data storage of a Model I/O mesh.
- [protocol MDLMeshBufferZone](mdlmeshbufferzone.md)
  The general interface for logical pools of memory used in allocation of related mesh data buffers.
- [class MDLMeshBufferZoneDefault](mdlmeshbufferzonedefault.md)
  A standard implementation of the [`MDLMeshBufferZone`](mdlmeshbufferzone.md) protocol.
- [class MDLVertexAttribute](mdlvertexattribute.md)
  A description of the format of per-vertex data for a single vertex attribute in a mesh object.
- [class MDLVertexBufferLayout](mdlvertexbufferlayout.md)
  A [`MDLVertexBufferLayout`](mdlvertexbufferlayout.md) object describes layout information for a vertex buffer in a [`MDLMesh`](mdlmesh.md) object. A collection of vertex layer objects, vertex attribute objects, and additional information forms a [`MDLVertexDescriptor`](mdlvertexdescriptor.md) object, which completely describes the layout of vertex buffers for a mesh.
- [class MDLVertexDescriptor](mdlvertexdescriptor.md)
  A description of the structure, format, and layout for vertex data buffers associated with a mesh.


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlvertexattributedata)*