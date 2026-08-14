# CVPixelBufferCreationAttributes

**Framework**: Core Video  
**Kind**: struct

Attributes needed for creating a pixel buffer.

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
struct CVPixelBufferCreationAttributes
```

## Topics

### Initializers
- [init?(CVPixelBufferAttributes)](cvpixelbuffercreationattributes/init(_:).md)
  Convert Attributes to CreationAttributes. This init will fail if [`pixelFormatType`](cvpixelbuffercreationattributes/pixelformattype.md) or [`size`](cvpixelbuffercreationattributes/size.md) properties are absent.
- [init(pixelFormatType: CVPixelFormatType, size: CVImageSize, compatibility: CVPixelFormatDescription.Compatibility, bytesPerRowAlignment: Int?, planeAlignment: Int?, extendedPixels: CVPixelBufferPadding?)](cvpixelbuffercreationattributes/init(pixelformattype:size:compatibility:bytesperrowalignment:planealignment:extendedpixels:).md)
- [init(pixelFormatType: CVPixelFormatType, size: CVImageSize, compatibility: CVPixelFormatDescription.Compatibility, bytesPerRowAlignment: Int?, planeAlignment: Int?, extendedPixels: CVPixelBufferPadding?, attachments: CVAttachmentContainer<CVPixelBufferAttachmentKeyDefinitions>?)](cvpixelbuffercreationattributes/init(pixelformattype:size:compatibility:bytesperrowalignment:planealignment:extendedpixels:attachments:).md)
### Instance Properties
- [var attachments: CVAttachmentContainer<CVPixelBufferAttachmentKeyDefinitions>?](cvpixelbuffercreationattributes/attachments.md)
  Attachments to set on the pixel buffer.
- [var backing: CVPixelBufferCreationAttributes.Backing](cvpixelbuffercreationattributes/backing-swift.property.md)
  Defines how the memory for the pixel buffer backing is allocated. IOSurface backed pixel buffers can be shared between CPU and GPU also across process boundaries. Defaults to `Backing.ioSurface`.
- [var bytesPerRowAlignment: Int?](cvpixelbuffercreationattributes/bytesperrowalignment.md)
  The number of bytes per row in the pixel buffer must be a multiple of this number.
- [var compatibility: CVPixelFormatDescription.Compatibility](cvpixelbuffercreationattributes/compatibility.md)
  Defines interoperability of pixel buffers with other frameworks
- [var extendedPixels: CVPixelBufferPadding?](cvpixelbuffercreationattributes/extendedpixels.md)
  Sets the amount of extended pixel padding in the pixel buffer.
- [var pixelFormatType: CVPixelFormatType](cvpixelbuffercreationattributes/pixelformattype.md)
  Format of the pixel buffer bytes
- [var planeAlignment: Int?](cvpixelbuffercreationattributes/planealignment.md)
  Planes start on a byte number that’s a multiple of this value.
- [var size: CVImageSize](cvpixelbuffercreationattributes/size.md)
  Size of the buffer in pixels
### Enumerations
- [CVPixelBufferCreationAttributes.Backing](cvpixelbuffercreationattributes/backing-swift.enum.md)
  Type of backing storage used by the pixel buffer

## Relationships

### Conforms To
- [Equatable](../swift/equatable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [class CVReadOnlyPixelBuffer](cvreadonlypixelbuffer.md)
  CVReadOnlyPixelBuffer provides an immutable view of the pixel data held by the pixel buffer.
- [struct CVMutablePixelBuffer](cvmutablepixelbuffer.md)
  CVMutablePixelBuffer provides read-write access to the pixel data and attachments.
- [struct CVPixelBufferAttributes](cvpixelbufferattributes.md)
  A partial set of pixel buffer creation attributes. This struct is useful for conveying partial requirements for pixel buffers to clients. This struct makes all properties of `CVPixelBuffer/CreationAttributes` optional.
- [struct CVPixelBufferPadding](cvpixelbufferpadding.md)
  Padding pixels around the CVPixelBuffer
- [struct CVPixelBufferPlaneProperties](cvpixelbufferplaneproperties.md)
  Properties of a plane of pixels in pixel buffer
- [struct CVProResRawMetadata](cvproresrawmetadata.md)
  Metadata associated with ProRes RAW images.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvpixelbuffercreationattributes)*