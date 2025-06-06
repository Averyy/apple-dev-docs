# addAttribute(withName:format:)

**Framework**: Model I/O  
**Kind**: method

Adds a vertex attribute to the mesh and creates a new, empty corresponding vertex buffer.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.0+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func addAttribute(withName name: String, format: MDLVertexFormat)
```

#### Discussion

Calling this method updates the mesh’s [`vertexDescriptor`](mdlmesh/vertexdescriptor.md) object to reflect the new attribute, and then uses the same [`MDLMeshBufferAllocator`](mdlmeshbufferallocator.md) object shared by the mesh’s existing vertex buffers to allocate new, empty storage for the new attribute’s vertex data. This method has no effect if the mesh already contains an attribute with the specified name; to overwrite or rearrange existing attribute data, use the [`vertexDescriptor`](mdlmesh/vertexdescriptor.md) property.

## Parameters

- `name`: A name for the new attribute. See Vertex Attributes for standard attribute names.
- `format`: The data format for the new attribute.

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
- [func addAttribute(withName: String, format: MDLVertexFormat, type: String, data: Data, stride: Int)](mdlmesh/addattribute(withname:format:type:data:stride:).md)
- [func addAttribute(withName: String, format: MDLVertexFormat, type: String, data: Data, stride: Int, time: TimeInterval)](mdlmesh/addattribute(withname:format:type:data:stride:time:).md)
- [func removeAttributeNamed(String)](mdlmesh/removeattributenamed(_:).md)
- [func replaceAttributeNamed(String, with: MDLVertexAttributeData)](mdlmesh/replaceattributenamed(_:with:).md)
- [func updateAttributeNamed(String, with: MDLVertexAttributeData)](mdlmesh/updateattributenamed(_:with:).md)
- [func addUnwrappedTextureCoordinates(forAttributeNamed: String)](mdlmesh/addunwrappedtexturecoordinates(forattributenamed:).md)
- [func vertexAttributeData(forAttributeNamed: String) -> MDLVertexAttributeData?](mdlmesh/vertexattributedata(forattributenamed:).md)
  Returns the vertex data for the specified attribute.
- [func vertexAttributeData(forAttributeNamed: String, as: MDLVertexFormat) -> MDLVertexAttributeData?](mdlmesh/vertexattributedata(forattributenamed:as:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlmesh/addattribute(withname:format:))*