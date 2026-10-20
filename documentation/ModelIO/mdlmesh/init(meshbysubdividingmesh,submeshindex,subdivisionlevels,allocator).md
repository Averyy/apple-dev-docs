# init(meshBySubdividingMesh:submeshIndex:subdivisionLevels:allocator:)

**Framework**: Model I/O  
**Kind**: init

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.0+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
init(meshBySubdividingMesh mesh: MDLMesh, submeshIndex: Int32, subdivisionLevels: UInt32, allocator: (any MDLMeshBufferAllocator)?)
```

## See Also

- [init(vertexBuffer: any MDLMeshBuffer, vertexCount: Int, descriptor: MDLVertexDescriptor, submeshes: [MDLSubmesh])](mdlmesh/init(vertexbuffer:vertexcount:descriptor:submeshes:).md)
  Creates a mesh from a single vertex buffer with the specified parameters.
- [init(vertexBuffers: [any MDLMeshBuffer], vertexCount: Int, descriptor: MDLVertexDescriptor, submeshes: [MDLSubmesh])](mdlmesh/init(vertexbuffers:vertexcount:descriptor:submeshes:).md)
  Creates a mesh by unifying vertex data from multiple sources with the specified parameters.
- [init(bufferAllocator: (any MDLMeshBufferAllocator)?)](mdlmesh/init(bufferallocator:).md)
- [class func newSubdividedMesh(MDLMesh, submeshIndex: Int, subdivisionLevels: Int) -> Self?](mdlmesh/newsubdividedmesh(_:submeshindex:subdivisionlevels:).md)
  Creates a new mesh by subdividing the specified mesh.


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlmesh/init(meshbysubdividingmesh:submeshindex:subdivisionlevels:allocator:))*