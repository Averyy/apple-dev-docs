# boundingBoxStride

**Framework**: Metal  
**Kind**: property

The stride, in bytes, between bounding boxes in the buffer.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
var boundingBoxStride: Int { get set }
```

#### Discussion

The stride needs be at least 24 bytes, and be a multiple of 4 bytes. The default value is 24 bytes.

## See Also

- [var boundingBoxBuffer: (any MTLBuffer)?](mtlaccelerationstructureboundingboxgeometrydescriptor/boundingboxbuffer.md)
  A buffer that contains an array of bounding box structures.
- [var boundingBoxBufferOffset: Int](mtlaccelerationstructureboundingboxgeometrydescriptor/boundingboxbufferoffset.md)
  The offset, in bytes, to the first bounding box in the buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlaccelerationstructureboundingboxgeometrydescriptor/boundingboxstride)*