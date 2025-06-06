# vertexBufferOffset

**Framework**: Metal  
**Kind**: property

The offset, in bytes, for the first vertex in the vertex buffer.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
var vertexBufferOffset: Int { get set }
```

#### Discussion

The vertex must be a multiple of the vertex stride and must be a multiple of 4 bytes. The default value is 0.

## See Also

- [var vertexBuffer: (any MTLBuffer)?](mtlaccelerationstructuretrianglegeometrydescriptor/vertexbuffer.md)
  A buffer  that contains vertex data.
- [var vertexStride: Int](mtlaccelerationstructuretrianglegeometrydescriptor/vertexstride.md)
  The stride, in bytes, between vertices in the vertex buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlaccelerationstructuretrianglegeometrydescriptor/vertexbufferoffset)*