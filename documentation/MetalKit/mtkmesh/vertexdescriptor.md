# vertexDescriptor

**Framework**: MetalKit  
**Kind**: property

A Model I/O vertex descriptor specifying the data layout in the vertex buffers.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var vertexDescriptor: MDLVertexDescriptor { get }
```

#### Discussion

This is a convenience property. The [`MTKMesh`](mtkmesh.md) class does not use this descriptor, but your application may use this object to determine rendering state or create a [`MTLVertexDescriptor`](https://developer.apple.com/documentation/Metal/MTLVertexDescriptor) object to build a [`MTLRenderPipelineState`](https://developer.apple.com/documentation/Metal/MTLRenderPipelineState) object capable of interpreting the data in [`vertexBuffers`](mtkmesh/vertexbuffers.md).

## See Also

- [var vertexBuffers: [MTKMeshBuffer]](mtkmesh/vertexbuffers.md)
  An array of buffers in which mesh vertex data resides.
- [var vertexCount: Int](mtkmesh/vertexcount.md)
  The number of vertices in the vertex buffers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalkit/mtkmesh/vertexdescriptor)*