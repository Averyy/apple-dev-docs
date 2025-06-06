# newSubdividedMesh(_:submeshIndex:subdivisionLevels:)

**Framework**: Model I/O  
**Kind**: method

Creates a new mesh by subdividing the specified mesh.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.0+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
class func newSubdividedMesh(_ mesh: MDLMesh, submeshIndex: Int, subdivisionLevels: Int) -> Self?
```

#### Return Value

A new mesh object, or `nil` if subdivision fails.

#### Discussion

Surface subdivision creates a smooth mesh from a coarse mesh by splitting each primitive (triangle or quad) in the original mesh into multiple smaller primitives and projecting the newly created vertices along surface normal vectors. The `subdivisionLevels` parameter controls the level of detail (and resulting performance cost) of the subdivision process. For example, in a triangle mesh, a subdivision level of 1 replaces each triangle with a set of four smaller triangles; a subdivision level of 2 replaces each of those four triangles with four even smaller triangles (for a total of 16 created from the triangle in the original mesh.

> **Note**:  The computational cost of subdivision increases exponentially with subdivision level. Depending on the arrangement of the original mesh and the device on which a mesh is to be rendered, using a subdivision level greater than 4 may result in more detail than would be visible when rendering.

 The computational cost of subdivision increases exponentially with subdivision level. Depending on the arrangement of the original mesh and the device on which a mesh is to be rendered, using a subdivision level greater than 4 may result in more detail than would be visible when rendering.

Meshes intended for use with surface subdivision contain topology information to ensure that the results of subdivision match the artist’s intent. To make use of this information, use the [`init(url:vertexDescriptor:bufferAllocator:preserveTopology:error:)`](mdlasset/init(url:vertexdescriptor:bufferallocator:preservetopology:error:).md) initializer when creating an [`MDLAsset`](mdlasset.md) object to load meshes from.

## Parameters

- `mesh`: The mesh from which to generate a new subdivided mesh.
- `submeshIndex`: The index of the submesh in the original mesh from which to generate the new mesh.
- `subdivisionLevels`: The number of times to iteratively perform the subdivision process.

## See Also

- [init(vertexBuffer: any MDLMeshBuffer, vertexCount: Int, descriptor: MDLVertexDescriptor, submeshes: [MDLSubmesh])](mdlmesh/init(vertexbuffer:vertexcount:descriptor:submeshes:).md)
  Creates a mesh from a single vertex buffer with the specified parameters.
- [init(vertexBuffers: [any MDLMeshBuffer], vertexCount: Int, descriptor: MDLVertexDescriptor, submeshes: [MDLSubmesh])](mdlmesh/init(vertexbuffers:vertexcount:descriptor:submeshes:).md)
  Creates a mesh by unifying vertex data from multiple sources with the specified parameters.
- [init(bufferAllocator: (any MDLMeshBufferAllocator)?)](mdlmesh/init(bufferallocator:).md)
- [init(meshBySubdividingMesh: MDLMesh, submeshIndex: Int32, subdivisionLevels: UInt32, allocator: (any MDLMeshBufferAllocator)?)](mdlmesh/init(meshbysubdividingmesh:submeshindex:subdivisionlevels:allocator:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlmesh/newsubdividedmesh(_:submeshindex:subdivisionlevels:))*