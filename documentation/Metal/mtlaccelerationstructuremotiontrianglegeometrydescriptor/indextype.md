# indexType

**Framework**: Metal  
**Kind**: property

The data type of indices in the index buffer.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
var indexType: MTLIndexType { get set }
```

#### Discussion

The data type must be [`MTLDataType.ushort`](mtldatatype/ushort.md) or [`MTLDataType.uint`](mtldatatype/uint.md). The default is [`MTLDataType.uint`](mtldatatype/uint.md).

## See Also

- [var indexBuffer: (any MTLBuffer)?](mtlaccelerationstructuremotiontrianglegeometrydescriptor/indexbuffer.md)
  A buffer that contains indices for the vertices that compose the triangle list.
- [var indexBufferOffset: Int](mtlaccelerationstructuremotiontrianglegeometrydescriptor/indexbufferoffset.md)
  The offset, in bytes, to the first index in the buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlaccelerationstructuremotiontrianglegeometrydescriptor/indextype)*