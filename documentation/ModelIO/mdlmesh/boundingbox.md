# boundingBox

**Framework**: Model I/O  
**Kind**: property  
**Role**: Instance Property

The minimum region entirely enclosing the mesh’s vertex positions, expressed in the model coordinate system of the mesh.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var boundingBox: MDLAxisAlignedBoundingBox { get }
```

```objc
@property (nonatomic, readonly) MDLAxisAlignedBoundingBox boundingBox;
```

## Discussion

This property’s value is valid only if the mesh contains vertex data for the [`MDLVertexAttributePosition`](../mdlvertexattributeposition.md) attribute. If the mesh does not contain position information, this property’s value is a bounding box whose `maxBounds` coordinate is greater than its `minBounds` coordinate.

Reading this property for the first time processes the mesh’s vertex data to calculate and cache a bounding box. Reading this property thereafter returns the cached value.

## See Also

### Working with Vertex Data
- [var submeshes: NSMutableArray?](./submeshes.md)
  The array of submeshes to be used in rendering the mesh.
- [var vertexBuffers: [any MDLMeshBuffer]](./vertexbuffers.md)
  The array of buffers that provide vertex data for the mesh.
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

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlmesh/boundingbox)*