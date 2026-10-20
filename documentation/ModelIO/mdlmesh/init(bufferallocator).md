# init(bufferAllocator:)

**Framework**: Model I/O  
**Kind**: init  
**Role**: Initializer

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
init(bufferAllocator: (any MDLMeshBufferAllocator)?)
```

```objc
- (instancetype) initWithBufferAllocator:(id<MDLMeshBufferAllocator>) bufferAllocator;
```

## See Also

### Creating a Custom Mesh
- [init(vertexBuffer: any MDLMeshBuffer, vertexCount: Int, descriptor: MDLVertexDescriptor, submeshes: [MDLSubmesh])](./init%28vertexbuffer,vertexcount,descriptor,submeshes%29.md)
  Creates a mesh from a single vertex buffer with the specified parameters.
- [init(vertexBuffers: [any MDLMeshBuffer], vertexCount: Int, descriptor: MDLVertexDescriptor, submeshes: [MDLSubmesh])](./init%28vertexbuffers,vertexcount,descriptor,submeshes%29.md)
  Creates a mesh by unifying vertex data from multiple sources with the specified parameters.
- [class func newSubdividedMesh(MDLMesh, submeshIndex: Int, subdivisionLevels: Int) -> Self?](./newsubdividedmesh%28_,submeshindex,subdivisionlevels%29.md)
  Creates a new mesh by subdividing the specified mesh.
- [init(meshBySubdividingMesh: MDLMesh, submeshIndex: Int32, subdivisionLevels: UInt32, allocator: (any MDLMeshBufferAllocator)?)](./init%28meshbysubdividingmesh,submeshindex,subdivisionlevels,allocator%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlmesh/init(bufferallocator:))*