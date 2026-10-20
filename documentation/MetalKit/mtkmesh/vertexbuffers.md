# vertexBuffers

**Framework**: MetalKit  
**Kind**: property  
**Role**: Instance Property

An array of buffers in which mesh vertex data resides.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var vertexBuffers: [MTKMeshBuffer] { get }
```

```objc
@property (nonatomic, readonly, nonnull) NSArray<MTKMeshBuffer *> * vertexBuffers;
```

## See Also

### Vertex Properties
- [var vertexCount: Int](./vertexcount.md)
  The number of vertices in the vertex buffers.
- [var vertexDescriptor: MDLVertexDescriptor](./vertexdescriptor.md)
  A Model I/O vertex descriptor specifying the data layout in the vertex buffers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalkit/mtkmesh/vertexbuffers)*