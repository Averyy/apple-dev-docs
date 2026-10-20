# MeshDeformParameter.VertexBuffers

**Framework**: RealityKit  
**Kind**: struct  
**Role**: Structure

The vertices requested by the developer when they defined their custom deformations. These will be passed into their custom deformation functions.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
struct VertexBuffers<Buffer>
```

## Topics

### Accessing geometry buffers
- [let positions: MeshDeformParameter<InputBuffer, OutputBuffer>.VertexBuffers<Buffer>.Data?](./vertexbuffers/positions.md)
  The positions buffer, if the custom deformer author specified it.
- [let normals: MeshDeformParameter<InputBuffer, OutputBuffer>.VertexBuffers<Buffer>.Data?](./vertexbuffers/normals.md)
  The normals buffer, if the custom deformer author specified it.
- [let tangents: MeshDeformParameter<InputBuffer, OutputBuffer>.VertexBuffers<Buffer>.Data?](./vertexbuffers/tangents.md)
  The tangents buffer, if the custom deformer author specified it.
- [let bitangents: MeshDeformParameter<InputBuffer, OutputBuffer>.VertexBuffers<Buffer>.Data?](./vertexbuffers/bitangents.md)
  The bitangents buffer, if the custom deformer author specified it.
### Accessing texture coordinates
- [let uvs: MeshDeformParameter<InputBuffer, OutputBuffer>.VertexBuffers<Buffer>.Data?](./vertexbuffers/uvs.md)
  The uvs buffer, if the custom deformer author specified it
- [let uv1s: MeshDeformParameter<InputBuffer, OutputBuffer>.VertexBuffers<Buffer>.Data?](./vertexbuffers/uv1s.md)
  The uv1s buffer, if the custom deformer author specified it
- [let uv2s: MeshDeformParameter<InputBuffer, OutputBuffer>.VertexBuffers<Buffer>.Data?](./vertexbuffers/uv2s.md)
  The uv2s buffer, if the custom deformer author specified it
- [let uv3s: MeshDeformParameter<InputBuffer, OutputBuffer>.VertexBuffers<Buffer>.Data?](./vertexbuffers/uv3s.md)
  The uv3s buffer, if the custom deformer author specified it
- [let uv4s: MeshDeformParameter<InputBuffer, OutputBuffer>.VertexBuffers<Buffer>.Data?](./vertexbuffers/uv4s.md)
  The uv4s buffer, if the custom deformer author specified it
- [let uv5s: MeshDeformParameter<InputBuffer, OutputBuffer>.VertexBuffers<Buffer>.Data?](./vertexbuffers/uv5s.md)
  The uv5s buffer, if the custom deformer author specified it
- [let uv6s: MeshDeformParameter<InputBuffer, OutputBuffer>.VertexBuffers<Buffer>.Data?](./vertexbuffers/uv6s.md)
  The uv6s buffer, if the custom deformer author specified it
- [let uv7s: MeshDeformParameter<InputBuffer, OutputBuffer>.VertexBuffers<Buffer>.Data?](./vertexbuffers/uv7s.md)
  The uv7s buffer, if the custom deformer author specified it
### Inspecting buffer storage
- [let count: Int](./vertexbuffers/count.md)
  The number of elements in each of the specified buffers.
- [MeshDeformParameter.VertexBuffers.Data](./vertexbuffers/data.md)
  Provides low-level information about the memory allocation of the buffers.

## See Also

### Accessing deformation buffers
- [var inputBuffers: MeshDeformParameter<InputBuffer, OutputBuffer>.VertexBuffers<InputBuffer>](./inputbuffers.md)
  The specified input vertex data for the deformer function.
- [var outputBuffers: MeshDeformParameter<InputBuffer, OutputBuffer>.VertexBuffers<OutputBuffer>](./outputbuffers.md)
  The specified output vertex data for the deformer function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/meshdeformparameter/vertexbuffers)*