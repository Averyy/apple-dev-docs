# vertexBuffer

**Framework**: Metal  
**Kind**: property

A buffer that contains vertex data.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
var vertexBuffer: (any MTLBuffer)? { get set }
```

#### Discussion

The [`vertexFormat`](mtlaccelerationstructuretrianglegeometrydescriptor/vertexformat.md) property defines the format of each vertex position in the buffer. You need to set a vertex buffer before creating the acceleration structure.

## See Also

- [var vertexFormat: MTLAttributeFormat](mtlaccelerationstructuretrianglegeometrydescriptor/vertexformat.md)
  The format of each vertex position in the vertex buffer property.
- [var vertexBufferOffset: Int](mtlaccelerationstructuretrianglegeometrydescriptor/vertexbufferoffset.md)
  The offset, in bytes, for the first vertex in the vertex buffer.
- [var vertexStride: Int](mtlaccelerationstructuretrianglegeometrydescriptor/vertexstride.md)
  The stride, in bytes, between vertices in the vertex buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlaccelerationstructuretrianglegeometrydescriptor/vertexbuffer)*