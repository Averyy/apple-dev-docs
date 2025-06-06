# indexBufferOffset

**Framework**: Metal  
**Kind**: property

The offset, in bytes, to the first index in the buffer.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
var indexBufferOffset: Int { get set }
```

#### Discussion

Specify an offset that is a multiple of the index data type size and a multiple of the platform’s buffer offset alignment.

## See Also

- [var indexBuffer: (any MTLBuffer)?](mtlaccelerationstructuremotiontrianglegeometrydescriptor/indexbuffer.md)
  A buffer that contains indices for the vertices that compose the triangle list.
- [var indexType: MTLIndexType](mtlaccelerationstructuremotiontrianglegeometrydescriptor/indextype.md)
  The data type of indices in the index buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlaccelerationstructuremotiontrianglegeometrydescriptor/indexbufferoffset)*