# MDLVertexAttribute

**Framework**: Model I/O  
**Kind**: class

A description of the format of per-vertex data for a single vertex attribute in a mesh object.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
class MDLVertexAttribute
```

#### Overview

The vertex buffers of a [`MDLMesh`](mdlmesh.md) object store vertex attributes—such as vertex position, surface normal vector, or texture coordinates—that define its 3D shape and other data for use in rendering. Attribute information describes the structure and layout of that data. A collection of vertex attribute objects and additional information forms a [`MDLVertexDescriptor`](mdlvertexdescriptor.md) object, which completely describes the layout of vertex buffers for a mesh.

## Topics

### Creating a Vertex Attribute
- [init(name: String, format: MDLVertexFormat, offset: Int, bufferIndex: Int)](mdlvertexattribute/init(name:format:offset:bufferindex:).md)
  Initializes a vertex attribute object with the specified property values.
### Inspecting a Vertex Attribute
- [var name: String](mdlvertexattribute/name.md)
  An identifier for the semantic use of the vertex attribute.
- [var format: MDLVertexFormat](mdlvertexattribute/format.md)
  The format of per-vertex data for the attribute.
- [var offset: Int](mdlvertexattribute/offset.md)
  The offset, in bytes, of vertex data for the attribute in a vertex buffer, relative to the start of data for each vertex.
- [var bufferIndex: Int](mdlvertexattribute/bufferindex.md)
  The index of the vertex buffer containing data for this attribute in a mesh’s [`vertexBuffers`](mdlmesh/vertexbuffers.md) array.
- [var initializationValue: vector_float4](mdlvertexattribute/initializationvalue.md)
  The default value for vertex data for this attribute.
### Constants
- [Vertex Attributes](vertex-attributes.md)
  Names that identify semantic uses for vertex attribute data, used by the [`name`](mdlvertexattribute/name.md) property.
- [enum MDLVertexFormat](mdlvertexformat.md)
  Descriptions of the data size and layout for a vertex attribute, used by the [`format`](mdlvertexattribute/format.md) property.
### Instance Properties
- [var time: TimeInterval](mdlvertexattribute/time.md)

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
- [class MDLVertexAttributeData](mdlvertexattributedata.md)
  An object that provides convenience access to vertex data for a specific vertex attribute of a mesh.
- [class MDLVertexBufferLayout](mdlvertexbufferlayout.md)
  A [`MDLVertexBufferLayout`](mdlvertexbufferlayout.md) object describes layout information for a vertex buffer in a [`MDLMesh`](mdlmesh.md) object. A collection of vertex layer objects, vertex attribute objects, and additional information forms a [`MDLVertexDescriptor`](mdlvertexdescriptor.md) object, which completely describes the layout of vertex buffers for a mesh.
- [class MDLVertexDescriptor](mdlvertexdescriptor.md)
  A description of the structure, format, and layout for vertex data buffers associated with a mesh.


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlvertexattribute)*