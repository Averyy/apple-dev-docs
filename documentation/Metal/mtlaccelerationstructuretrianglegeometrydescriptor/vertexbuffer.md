# vertexBuffer

**Framework**: Metal  
**Kind**: property

A buffer  that contains vertex data.

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

You must set a vertex buffer before creating the acceleration structure. Each vertex must have at least 12 bytes of position data, stored as a [`MTLPackedFloat3`](mtlpackedfloat3.md) containing the X, Y, and Z position.

## See Also

- [var vertexBufferOffset: Int](mtlaccelerationstructuretrianglegeometrydescriptor/vertexbufferoffset.md)
  The offset, in bytes, for the first vertex in the vertex buffer.
- [var vertexStride: Int](mtlaccelerationstructuretrianglegeometrydescriptor/vertexstride.md)
  The stride, in bytes, between vertices in the vertex buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlaccelerationstructuretrianglegeometrydescriptor/vertexbuffer)*