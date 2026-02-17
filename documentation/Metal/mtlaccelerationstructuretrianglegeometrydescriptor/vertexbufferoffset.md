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

The offset needs to be a multiple of the vertex stride. Check the [`Metal feature set tables (PDF)`](https://developer.apple.comhttps://developer.apple.com/metal/Metal-Feature-Set-Tables.pdf) for potential alignment restrictions. The default value is `0`.

## See Also

- [var vertexFormat: MTLAttributeFormat](mtlaccelerationstructuretrianglegeometrydescriptor/vertexformat.md)
  The format of each vertex position in the vertex buffer property.
- [var vertexBuffer: (any MTLBuffer)?](mtlaccelerationstructuretrianglegeometrydescriptor/vertexbuffer.md)
  A buffer that contains vertex data.
- [var vertexStride: Int](mtlaccelerationstructuretrianglegeometrydescriptor/vertexstride.md)
  The stride, in bytes, between vertices in the vertex buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlaccelerationstructuretrianglegeometrydescriptor/vertexbufferoffset)*