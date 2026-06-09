# MeshDeformParameter.VertexBuffers

**Framework**: RealityKit  
**Kind**: struct

The vertices requested by the developer when they defined their custom deformations. These will be passed into their custom deformation functions.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct VertexBuffers<Buffer>
```

## Topics

### Accessing geometry buffers
- [let positions: MeshDeformParameter<InputBuffer, OutputBuffer>.VertexBuffers<Buffer>.Data?](meshdeformparameter/vertexbuffers/positions.md)
  The positions buffer, if the custom deformer author specified it.
- [let normals: MeshDeformParameter<InputBuffer, OutputBuffer>.VertexBuffers<Buffer>.Data?](meshdeformparameter/vertexbuffers/normals.md)
  The normals buffer, if the custom deformer author specified it.
- [let tangents: MeshDeformParameter<InputBuffer, OutputBuffer>.VertexBuffers<Buffer>.Data?](meshdeformparameter/vertexbuffers/tangents.md)
  The tangents buffer, if the custom deformer author specified it.
- [let bitangents: MeshDeformParameter<InputBuffer, OutputBuffer>.VertexBuffers<Buffer>.Data?](meshdeformparameter/vertexbuffers/bitangents.md)
  The bitangents buffer, if the custom deformer author specified it.
### Accessing texture coordinates
- [let uvs: MeshDeformParameter<InputBuffer, OutputBuffer>.VertexBuffers<Buffer>.Data?](meshdeformparameter/vertexbuffers/uvs.md)
  The uvs buffer, if the custom deformer author specified it
- [let uv1s: MeshDeformParameter<InputBuffer, OutputBuffer>.VertexBuffers<Buffer>.Data?](meshdeformparameter/vertexbuffers/uv1s.md)
  The uv1s buffer, if the custom deformer author specified it
- [let uv2s: MeshDeformParameter<InputBuffer, OutputBuffer>.VertexBuffers<Buffer>.Data?](meshdeformparameter/vertexbuffers/uv2s.md)
  The uv2s buffer, if the custom deformer author specified it
- [let uv3s: MeshDeformParameter<InputBuffer, OutputBuffer>.VertexBuffers<Buffer>.Data?](meshdeformparameter/vertexbuffers/uv3s.md)
  The uv3s buffer, if the custom deformer author specified it
- [let uv4s: MeshDeformParameter<InputBuffer, OutputBuffer>.VertexBuffers<Buffer>.Data?](meshdeformparameter/vertexbuffers/uv4s.md)
  The uv4s buffer, if the custom deformer author specified it
- [let uv5s: MeshDeformParameter<InputBuffer, OutputBuffer>.VertexBuffers<Buffer>.Data?](meshdeformparameter/vertexbuffers/uv5s.md)
  The uv5s buffer, if the custom deformer author specified it
- [let uv6s: MeshDeformParameter<InputBuffer, OutputBuffer>.VertexBuffers<Buffer>.Data?](meshdeformparameter/vertexbuffers/uv6s.md)
  The uv6s buffer, if the custom deformer author specified it
- [let uv7s: MeshDeformParameter<InputBuffer, OutputBuffer>.VertexBuffers<Buffer>.Data?](meshdeformparameter/vertexbuffers/uv7s.md)
  The uv7s buffer, if the custom deformer author specified it
### Inspecting buffer storage
- [let count: Int](meshdeformparameter/vertexbuffers/count.md)
  The number of elements in each of the specified buffers.
- [MeshDeformParameter.VertexBuffers.Data](meshdeformparameter/vertexbuffers/data.md)
  Provides low-level information about the memory allocation of the buffers.

## See Also

- [var inputBuffers: MeshDeformParameter<InputBuffer, OutputBuffer>.VertexBuffers<InputBuffer>](meshdeformparameter/inputbuffers.md)
  The specified input vertex data for the deformer function.
- [var outputBuffers: MeshDeformParameter<InputBuffer, OutputBuffer>.VertexBuffers<OutputBuffer>](meshdeformparameter/outputbuffers.md)
  The specified output vertex data for the deformer function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/meshdeformparameter/vertexbuffers)*