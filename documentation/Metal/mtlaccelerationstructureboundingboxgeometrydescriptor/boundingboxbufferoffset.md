# boundingBoxBufferOffset

**Framework**: Metal  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic) NSUInteger boundingBoxBufferOffset;
```

## Discussion

The offset needs to be a multiple of [`boundingBoxStride`](./boundingboxstride.md). Check the [Metal feature set tables (PDF)](https://developer.apple.com/metal/Metal-Feature-Set-Tables.pdf) for potential alignment restrictions.

## See Also

### Specifying bounding boxes data
- [var boundingBoxBuffer: (any MTLBuffer)?](./boundingboxbuffer.md)
  A buffer that contains an array of bounding box structures.
- [var boundingBoxStride: Int](./boundingboxstride.md)
  The stride, in bytes, between bounding boxes in the buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlaccelerationstructureboundingboxgeometrydescriptor/boundingboxbufferoffset)*