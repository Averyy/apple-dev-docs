# vertexBuffers

**Framework**: Model I/O  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic, retain, readwrite) NSArray<id<MDLMeshBuffer>> * vertexBuffers;
```

#### Discussion

A mesh contains vertex data organized in one of two designs: as a *structure of arrays* or as an *array of structures*. In a structure of arrays, the mesh contains multiple vertex buffers, each of which provides data for a different vertex attribute, and a single vertex is the union of data from the same index in each of the separate buffers. In an array of structures, the mesh contains a single vertex buffer, and each index in the vertex buffer contains data for all vertex attributes. Use the [`vertexDescriptor`](./vertexdescriptor.md) property to determine the structure of the mesh’s vertex data.

## See Also

### Working with Vertex Data
- [var boundingBox: MDLAxisAlignedBoundingBox](./boundingbox.md)
  The minimum region entirely enclosing the mesh’s vertex positions, expressed in the model coordinate system of the mesh.
- [var submeshes: NSMutableArray?](./submeshes.md)
  The array of submeshes to be used in rendering the mesh.
- [var vertexCount: Int](./vertexcount.md)
  The number of vertices in the mesh.
- [var vertexDescriptor: MDLVertexDescriptor](./vertexdescriptor.md)
  A description of the format and layout of the mesh’s vertex buffers.
- [var allocator: any MDLMeshBufferAllocator](./allocator.md)
- [func addAttribute(withName: String, format: MDLVertexFormat)](./addattribute%28withname,format%29.md)
  Adds a vertex attribute to the mesh and creates a new, empty corresponding vertex buffer.
- [func addAttribute(withName: String, format: MDLVertexFormat, type: String, data: Data, stride: Int)](./addattribute%28withname,format,type,data,stride%29.md)
- [func addAttribute(withName: String, format: MDLVertexFormat, type: String, data: Data, stride: Int, time: TimeInterval)](./addattribute%28withname,format,type,data,stride,time%29.md)
- [func removeAttributeNamed(String)](./removeattributenamed%28_%29.md)
- [func replaceAttributeNamed(String, with: MDLVertexAttributeData)](./replaceattributenamed%28_,with%29.md)
- [func updateAttributeNamed(String, with: MDLVertexAttributeData)](./updateattributenamed%28_,with%29.md)
- [func addUnwrappedTextureCoordinates(forAttributeNamed: String)](./addunwrappedtexturecoordinates%28forattributenamed%29.md)
- [func vertexAttributeData(forAttributeNamed: String) -> MDLVertexAttributeData?](./vertexattributedata%28forattributenamed%29.md)
  Returns the vertex data for the specified attribute.
- [func vertexAttributeData(forAttributeNamed: String, as: MDLVertexFormat) -> MDLVertexAttributeData?](./vertexattributedata%28forattributenamed,as%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlmesh/vertexbuffers)*