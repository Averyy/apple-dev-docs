# CVPixelBufferPlaneProperties

**Framework**: Core Video  
**Kind**: struct

Properties of a plane of pixels in pixel buffer

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

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