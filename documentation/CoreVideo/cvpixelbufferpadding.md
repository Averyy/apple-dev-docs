# CVPixelBufferPadding

**Framework**: Core Video  
**Kind**: struct

Padding pixels around the CVPixelBuffer

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
struct CVPixelBufferPadding
```

## Topics

### Initializers
- [init(left: Int, right: Int, top: Int, bottom: Int)](cvpixelbufferpadding/init(left:right:top:bottom:).md)
### Instance Properties
- [var bottom: Int](cvpixelbufferpadding/bottom.md)
  Pixel row padding at the bottom
- [var left: Int](cvpixelbufferpadding/left.md)
  Pixel column padding to the left
- [var right: Int](cvpixelbufferpadding/right.md)
  Pixel column padding to the right
- [var top: Int](cvpixelbufferpadding/top.md)
  Pixel row padding at the top
### Type Properties
- [static let zero: CVPixelBufferPadding](cvpixelbufferpadding/zero.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../swift/bitwisecopyable.md)
- [Copyable](../swift/copyable.md)
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
- [struct CVPixelBufferPlaneProperties](cvpixelbufferplaneproperties.md)
  Properties of a plane of pixels in pixel buffer
- [struct CVProResRawMetadata](cvproresrawmetadata.md)
  Metadata associated with ProRes RAW images.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvpixelbufferpadding)*