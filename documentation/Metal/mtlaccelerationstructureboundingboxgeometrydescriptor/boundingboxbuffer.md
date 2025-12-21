# boundingBoxBuffer

**Framework**: Metal  
**Kind**: property

A buffer that contains an array of bounding box structures.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
var boundingBoxBuffer: (any MTLBuffer)? { get set }
```

#### Discussion

The buffer contains an array of [`MTLAxisAlignedBoundingBox`](mtlaxisalignedboundingbox-c.struct.md) structures, one for each bounding box in the geometry.

## See Also

- [var boundingBoxBufferOffset: Int](mtlaccelerationstructureboundingboxgeometrydescriptor/boundingboxbufferoffset.md)
  The offset, in bytes, to the first bounding box in the buffer.
- [var boundingBoxStride: Int](mtlaccelerationstructureboundingboxgeometrydescriptor/boundingboxstride.md)
  The stride, in bytes, between bounding boxes in the buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlaccelerationstructureboundingboxgeometrydescriptor/boundingboxbuffer)*