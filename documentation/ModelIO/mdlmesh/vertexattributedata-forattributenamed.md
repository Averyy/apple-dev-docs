# vertexAttributeData(forAttributeNamed:)

**Framework**: Model I/O  
**Kind**: method

Returns the vertex data for the specified attribute.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func vertexAttributeData(forAttributeNamed name: String) -> MDLVertexAttributeData?
```

#### Return Value

The vertex data for the specified attribute, or `nil` if the mesh does not contain vertex data for the specified attribute.

#### Discussion

Calling this data is equivalent to using the mesh’s [`vertexDescriptor`](mdlmesh/vertexdescriptor.md) object to find the index of the [`MDLMeshBuffer`](mdlmeshbuffer.md) object corresponding to the specified vertex attribute in the mesh’s [`vertexBuffers`](mdlmesh/vertexbuffers.md) array, then using the vertex buffer’s [`map()`](mdlmeshbuffer/map().md) method to gain read-only access to the vertex buffer’s data.

> ❗ **Important**:  The buffer’s storage remains mapped for as long as the returned [`MDLVertexAttributeData`](mdlvertexattributedata.md) object exists, potentially restricting other uses of that storage. For example, if a buffer’s storage is shared with GPU memory, that buffer may be unavailable for use in rendering until the data object is deallocated.

 The buffer’s storage remains mapped for as long as the returned [`MDLVertexAttributeData`](mdlvertexattributedata.md) object exists, potentially restricting other uses of that storage. For example, if a buffer’s storage is shared with GPU memory, that buffer may be unavailable for use in rendering until the data object is deallocated.

## Parameters

- `name`: The attribute name for which to retrieve data. See Vertex Attributes for standard attribute names.

## See Also

- [var boundingBox: MDLAxisAlignedBoundingBox](mdlmesh/boundingbox.md)
  The minimum region entirely enclosing the mesh’s vertex positions, expressed in the model coordinate system of the mesh.
- [var submeshes: NSMutableArray?](mdlmesh/submeshes.md)
  The array of submeshes to be used in rendering the mesh.
- [var vertexBuffers: [any MDLMeshBuffer]](mdlmesh/vertexbuffers.md)
  The array of buffers that provide vertex data for the mesh.
- [var vertexCount: Int](mdlmesh/vertexcount.md)
  The number of vertices in the mesh.
- [var vertexDescriptor: MDLVertexDescriptor](mdlmesh/vertexdescriptor.md)
  A description of the format and layout of the mesh’s vertex buffers.
- [var allocator: any MDLMeshBufferAllocator](mdlmesh/allocator.md)
- [func addAttribute(withName: String, format: MDLVertexFormat)](mdlmesh/addattribute(withname:format:).md)
  Adds a vertex attribute to the mesh and creates a new, empty corresponding vertex buffer.
- [func addAttribute(withName: String, format: MDLVertexFormat, type: String, data: Data, stride: Int)](mdlmesh/addattribute(withname:format:type:data:stride:).md)
- [func addAttribute(withName: String, format: MDLVertexFormat, type: String, data: Data, stride: Int, time: TimeInterval)](mdlmesh/addattribute(withname:format:type:data:stride:time:).md)
- [func removeAttributeNamed(String)](mdlmesh/removeattributenamed(_:).md)
- [func replaceAttributeNamed(String, with: MDLVertexAttributeData)](mdlmesh/replaceattributenamed(_:with:).md)
- [func updateAttributeNamed(String, with: MDLVertexAttributeData)](mdlmesh/updateattributenamed(_:with:).md)
- [func addUnwrappedTextureCoordinates(forAttributeNamed: String)](mdlmesh/addunwrappedtexturecoordinates(forattributenamed:).md)
- [func vertexAttributeData(forAttributeNamed: String, as: MDLVertexFormat) -> MDLVertexAttributeData?](mdlmesh/vertexattributedata(forattributenamed:as:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlmesh/vertexattributedata(forattributenamed:))*