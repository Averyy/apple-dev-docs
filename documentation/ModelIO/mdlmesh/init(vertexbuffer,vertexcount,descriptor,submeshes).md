# init(vertexBuffer:vertexCount:descriptor:submeshes:)

**Framework**: Model I/O  
**Kind**: init  
**Role**: Initializer

Creates a mesh from a single vertex buffer with the specified parameters.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
init(vertexBuffer: any MDLMeshBuffer, vertexCount: Int, descriptor: MDLVertexDescriptor, submeshes: [MDLSubmesh])
```

```objc
- (instancetype) initWithVertexBuffer:(id<MDLMeshBuffer>) vertexBuffer vertexCount:(NSUInteger) vertexCount descriptor:(MDLVertexDescriptor *) descriptor submeshes:(NSArray<MDLSubmesh *> *) submeshes;
```

## Return Value

A new mesh object.

## Discussion

Use this initializer to create a mesh from vertex data that describes multiple vertex attributes in the same array (that is, in an array of structures).

## Parameters

- `vertexBuffer`: The source of vertex information for the mesh.
- `vertexCount`: The number of vertices in the mesh.
- `descriptor`: An object describing the type and layout of vertex attribute data in the vertex buffer.
- `submeshes`: An array of submesh objects, each of which provides index buffer and material information describing how some or all of the mesh’s vertex data is to be rendered.

## See Also

### Creating a Custom Mesh
- [init(vertexBuffers: [any MDLMeshBuffer], vertexCount: Int, descriptor: MDLVertexDescriptor, submeshes: [MDLSubmesh])](./init%28vertexbuffers,vertexcount,descriptor,submeshes%29.md)
  Creates a mesh by unifying vertex data from multiple sources with the specified parameters.
- [init(bufferAllocator: (any MDLMeshBufferAllocator)?)](./init%28bufferallocator%29.md)
- [class func newSubdividedMesh(MDLMesh, submeshIndex: Int, subdivisionLevels: Int) -> Self?](./newsubdividedmesh%28_,submeshindex,subdivisionlevels%29.md)
  Creates a new mesh by subdividing the specified mesh.
- [init(meshBySubdividingMesh: MDLMesh, submeshIndex: Int32, subdivisionLevels: UInt32, allocator: (any MDLMeshBufferAllocator)?)](./init%28meshbysubdividingmesh,submeshindex,subdivisionlevels,allocator%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlmesh/init(vertexbuffer:vertexcount:descriptor:submeshes:))*