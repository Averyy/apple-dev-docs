# boundingBoxBufferOffset

**Framework**: Metal  
**Kind**: property

The offset, in bytes, to the first bounding box in the buffer.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
var boundingBoxBufferOffset: Int { get set }
```

#### Discussion

The offset needs be a multiple of [`boundingBoxStride`](mtlaccelerationstructureboundingboxgeometrydescriptor/boundingboxstride.md), and you need to align it to the platform’s buffer offset alignment.

## See Also

- [var boundingBoxBuffer: (any MTLBuffer)?](mtlaccelerationstructureboundingboxgeometrydescriptor/boundingboxbuffer.md)
  A buffer that contains an array of bounding box structures.
- [var boundingBoxStride: Int](mtlaccelerationstructureboundingboxgeometrydescriptor/boundingboxstride.md)
  The stride, in bytes, between bounding boxes in the buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlaccelerationstructureboundingboxgeometrydescriptor/boundingboxbufferoffset)*