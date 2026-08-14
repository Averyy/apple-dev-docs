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
  Number of bytes in each row of the plane. Note that this may be greater than the number of bytes required for all pixels in the row.
- [var size: CVImageSize](cvpixelbufferplaneproperties/size.md)
  Size of the plane in pixels

## Relationships

### Conforms To
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [class CVReadOnlyPixelBuffer](cvreadonlypixelbuffer.md)
  CVReadOnlyPixelBuffer provides an immutable view of the pixel data held by the pixel buffer.
- [struct CVMutablePixelBuffer](cvmutablepixelbuffer.md)
  CVMutablePixelBuffer provides read-write access to the pixel data and attachments.
- [struct CVPixelBufferAttributes](cvpixelbufferattributes.md)
  A partial set of pixel buffer creation attributes. This struct is useful for conveying partial requirements for pixel buffers to clients. This struct makes all properties of `CVPixelBuffer/CreationAttributes` optional.
- [struct CVPixelBufferCreationAttributes](cvpixelbuffercreationattributes.md)
  Attributes needed for creating a pixel buffer.
- [struct CVPixelBufferPadding](cvpixelbufferpadding.md)
  Padding pixels around the CVPixelBuffer
- [struct CVProResRawMetadata](cvproresrawmetadata.md)
  Metadata associated with ProRes RAW images.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvpixelbufferplaneproperties)*