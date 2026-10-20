# MeshDeformParameter.VertexBuffers.Data

**Framework**: RealityKit  
**Kind**: struct  
**Role**: Structure

Provides low-level information about the memory allocation of the buffers.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
struct Data
```

## Topics

### Accessing buffer data
- [let buffer: Buffer](./data/buffer.md)
  The allocation containing the vertex data.
- [let stride: Int](./data/stride.md)
  The stride of the vertex data.
### Instance Properties
- [let format: MTLVertexFormat](./data/format.md)
  The format of the vertices.
- [let offset: Int](./data/offset.md)
  The offset of the vertex data.

## See Also

### Inspecting buffer storage
- [let count: Int](./count.md)
  The number of elements in each of the specified buffers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/meshdeformparameter/vertexbuffers/data)*