# allocator

**Framework**: Model I/O  
**Kind**: property  
**Required**: Yes

The allocator object that created the buffer.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var allocator: any MDLMeshBufferAllocator { get }
```

#### Discussion

Certain operations on the MDLMesh object that owns this buffer—for example, generating new vertex attributes with methods such as [`addNormals(withAttributeNamed:creaseThreshold:)`](mdlmesh/addnormals(withattributenamed:creasethreshold:).md), or changing the format and layout of vertex data by assigning a new value to the [`vertexDescriptor`](mdlmesh/vertexdescriptor.md) property—may require reallocation of buffer memory. When you perform such operations, Model I/O  uses the same allocator that was used to create the buffer.

## See Also

- [var zone: any MDLMeshBufferZone](mdlmeshbuffer/zone.md)
  The memory pool from which the buffer was created.
- [var type: MDLMeshBufferType](mdlmeshbuffer/type.md)
  The type of data contained in a buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlmeshbuffer/allocator)*