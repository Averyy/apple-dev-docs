# MDLVertexDescriptor

**Framework**: Model I/O  
**Kind**: class

A description of the structure, format, and layout for vertex data buffers associated with a mesh.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
class MDLVertexDescriptor
```

#### Overview

A [`MDLMesh`](mdlmesh.md) object contains arrays of data for separate attributes of each vertex, such as position, color, surface normal vector, or texture coordinates. The vertex data for various attributes can be contained in one or more buffers and may be laid out in various contiguous or interleaved formats. You use a mesh’s [`vertexDescriptor`](mdlmesh/vertexdescriptor.md) property to determine the structure of vertex data for a mesh loaded from an asset file for use in rendering or processing a mesh. You also use vertex descriptors to describe the structure of existing vertex data when creating a new mesh.

## Topics

### Working with Vertex Attributes
- [var attributes: NSMutableArray](mdlvertexdescriptor/attributes.md)
  The list of vertex attributes described by the vertex descriptor.
- [func attributeNamed(String) -> MDLVertexAttribute?](mdlvertexdescriptor/attributenamed(_:).md)
  Returns the vertex attribute with the specified name in the vertex descriptor.
- [func addOrReplaceAttribute(MDLVertexAttribute)](mdlvertexdescriptor/addorreplaceattribute(_:).md)
  Adds the specified vertex attribute to the vertex descriptor, replacing any existing attribute with the same name.
- [func setPackedOffsets()](mdlvertexdescriptor/setpackedoffsets.md)
  Sets the offset for each vertex attribute to the minimum value to pack vertex data together in a single buffer.
### Working with Vertex Buffer Layouts
- [var layouts: NSMutableArray](mdlvertexdescriptor/layouts.md)
  The list of vertex buffer layouts described by the vertex descriptor.
- [func setPackedStrides()](mdlvertexdescriptor/setpackedstrides.md)
  Sets the stride for each vertex layout to the minimum value to pack vertex data together in a single buffer.
### Resetting a Vertex Descriptor
- [func reset()](mdlvertexdescriptor/reset.md)
  Resets a vertex descriptor to its default state.
### Copying a Vertex Descriptor
- [init(vertexDescriptor: MDLVertexDescriptor)](mdlvertexdescriptor/init(vertexdescriptor:).md)
  Creates a new vertex descriptor by performing a deep copy of the specified vertex descriptor.
### Instance Methods
- [func removeAttributeNamed(String)](mdlvertexdescriptor/removeattributenamed(_:).md)

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
- [class MDLVertexBufferLayout](mdlvertexbufferlayout.md)
  A [`MDLVertexBufferLayout`](mdlvertexbufferlayout.md) object describes layout information for a vertex buffer in a [`MDLMesh`](mdlmesh.md) object. A collection of vertex layer objects, vertex attribute objects, and additional information forms a [`MDLVertexDescriptor`](mdlvertexdescriptor.md) object, which completely describes the layout of vertex buffers for a mesh.


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlvertexdescriptor)*