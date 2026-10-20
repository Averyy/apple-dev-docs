# addAttribute(withName:format:)

**Framework**: Model I/O  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (void) addAttributeWithName:(NSString *) name format:(MDLVertexFormat) format;
```

#### Discussion

Calling this method updates the mesh’s [`vertexDescriptor`](./vertexdescriptor.md) object to reflect the new attribute, and then uses the same [`MDLMeshBufferAllocator`](../mdlmeshbufferallocator.md) object shared by the mesh’s existing vertex buffers to allocate new, empty storage for the new attribute’s vertex data. This method has no effect if the mesh already contains an attribute with the specified name; to overwrite or rearrange existing attribute data, use the [`vertexDescriptor`](./vertexdescriptor.md) property.

## Parameters

- `name`: A name for the new attribute. See Vertex Attributes for standard attribute names.
- `format`: The data format for the new attribute.

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

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlmesh/addattribute(withname:format:))*