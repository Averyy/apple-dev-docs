# vertexBuffers

**Framework**: Model I/O  
**Kind**: property

The array of buffers that provide vertex data for the mesh.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var vertexBuffers: [any MDLMeshBuffer] { get set }
```

#### Discussion

A mesh contains vertex data organized in one of two designs: as a  or as an . In a structure of arrays, the mesh contains multiple vertex buffers, each of which provides data for a different vertex attribute, and a single vertex is the union of data from the same index in each of the separate buffers. In an array of structures, the mesh contains a single vertex buffer, and each index in the vertex buffer contains data for all vertex attributes. Use the [`vertexDescriptor`](mdlmesh/vertexdescriptor.md) property to determine the structure of the mesh’s vertex data.

## See Also

- [var boundingBox: MDLAxisAlignedBoundingBox](mdlmesh/boundingbox.md)
  The minimum region entirely enclosing the mesh’s vertex positions, expressed in the model coordinate system of the mesh.
- [var submeshes: NSMutableArray?](mdlmesh/submeshes.md)
  The array of submeshes to be used in rendering the mesh.
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
- [func vertexAttributeData(forAttributeNamed: String) -> MDLVertexAttributeData?](mdlmesh/vertexattributedata(forattributenamed:).md)
  Returns the vertex data for the specified attribute.
- [func vertexAttributeData(forAttributeNamed: String, as: MDLVertexFormat) -> MDLVertexAttributeData?](mdlmesh/vertexattributedata(forattributenamed:as:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlmesh/vertexbuffers)*