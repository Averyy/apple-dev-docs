# CVPixelBufferPlaneProperties

**Framework**: Core Video  
**Kind**: struct

Properties of a plane of pixels in pixel buffer

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
@frozen
struct CVPixelBufferPlaneProperties
```

## Topics

### Initializers
- [init(size: CVImageSize, bytesPerRow: Int)](cvpixelbufferplaneproperties/init(size:bytesperrow:).md)
### Instance Properties
- [var bytesPerRow: Int](cvpixelbufferplaneproperties/bytesperrow.md)
  Number of bytes in each row of the plane. Note that this may be greater than the bytes required for all pixels in the row.
- [var size: CVImageSize](cvpixelbufferplaneproperties/size.md)
  Size of the plane in pixels

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvpixelbufferplaneproperties)*