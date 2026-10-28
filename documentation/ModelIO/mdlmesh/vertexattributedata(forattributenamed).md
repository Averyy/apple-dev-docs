# vertexAttributeData(forAttributeNamed:)

**Framework**: Model I/O  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (MDLVertexAttributeData *) vertexAttributeDataForAttributeNamed:(NSString *) name;
```

## Return Value

The vertex data for the specified attribute, or `nil` if the mesh does not contain vertex data for the specified attribute.

## Discussion

Calling this data is equivalent to using the mesh’s [`vertexDescriptor`](./vertexdescriptor.md) object to find the index of the [`MDLMeshBuffer`](../mdlmeshbuffer.md) object corresponding to the specified vertex attribute in the mesh’s [`vertexBuffers`](./vertexbuffers.md) array, then using the vertex buffer’s [`map()`](../mdlmeshbuffer/map%28%29.md) method to gain read-only access to the vertex buffer’s data.

> ❗ **Important**:  The buffer’s storage remains mapped for as long as the returned [`MDLVertexAttributeData`](../mdlvertexattributedata.md) object exists, potentially restricting other uses of that storage. For example, if a buffer’s storage is shared with GPU memory, that buffer may be unavailable for use in rendering until the data object is deallocated.

## Parameters

- `name`: The attribute name for which to retrieve data. See Vertex Attributes for standard attribute names.

## See Also

### Working with Vertex Data
- [var boundingBox: MDLAxisAlignedBoundingBox](./boundingbox.md)
  The minimum region entirely enclosing the mesh’s vertex positions, expressed in the model coordinate system of the mesh.
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
- [func vertexAttributeData(forAttributeNamed: String, as: MDLVertexFormat) -> MDLVertexAttributeData?](./vertexattributedata%28forattributenamed,as%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlmesh/vertexattributedata(forattributenamed:))*