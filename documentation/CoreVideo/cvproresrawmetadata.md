# CVProResRawMetadata

**Framework**: Core Video  
**Kind**: struct

Metadata associated with ProRes RAW images.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
struct CVProResRawMetadata
```

## Topics

### Structures
- [CVProResRawMetadata.RecommendedCrop](cvproresrawmetadata/recommendedcrop-swift.struct.md)
  Recommended pixels to discard in the image after raw conversion.
### Initializers
- [init(senselSitingOffsets: CVSenselSitingOffsets, blackLevel: Int32, whiteLevel: Int32, whiteBalanceCCT: Float32?, whiteBalanceRedFactor: Float32, whiteBalanceBlueFactor: Float32, colorMatrix: InlineArray<9, Float32>, gainFactor: Float32, recommendedCrop: CVProResRawMetadata.RecommendedCrop, extensions: Data?)](cvproresrawmetadata/init(senselsitingoffsets:blacklevel:whitelevel:whitebalancecct:whitebalanceredfactor:whitebalancebluefactor:colormatrix:gainfactor:recommendedcrop:extensions:).md)
### Instance Properties
- [var blackLevel: Int32](cvproresrawmetadata/blacklevel.md)
  The sensel level corresponding to no light exposure.
- [var colorMatrix: InlineArray<9, Float32>](cvproresrawmetadata/colormatrix.md)
  This is a 3x3 matrix which transforms linear RGB pixel values in the camera native color space to CIE 1931 XYZ values relative to the D65 illuminant, where the matrix entries are stored in row-major order.
- [var extensions: Data?](cvproresrawmetadata/extensions.md)
  ProRes RAW metadata extensions. This Data contains a big-endian UInt32 representing the size of the item in bytes followed by a 4-character code (‘psim’) followed by a variable-length pascal string identifying the metadata (like a key string) followed by the metadata payload.
- [var gainFactor: Float32](cvproresrawmetadata/gainfactor.md)
  The overall gain factor for raw conversion.
- [var recommendedCrop: CVProResRawMetadata.RecommendedCrop](cvproresrawmetadata/recommendedcrop-swift.property.md)
  The recommended number of: pixels to discard from the start (left) of each row of the image; pixels to discard from the end (right) of each row of the image; rows of pixels to discard from the top of the image; and rows of pixels to discard from the bottom of the image. Pixels/rows are discarded after raw conversion.
- [var senselSitingOffsets: CVSenselSitingOffsets](cvproresrawmetadata/senselsitingoffsets.md)
  Siting offsets, relative to pixel center, of individual sensels/components constituting each pixel.
- [var whiteBalanceBlueFactor: Float32](cvproresrawmetadata/whitebalancebluefactor.md)
  The white balance multiplication factor for blue-filtered sensels.
- [var whiteBalanceCCT: Float32?](cvproresrawmetadata/whitebalancecct.md)
  The illuminant correlated color temperature (CCT), in kelvins, selected at the time of capture. If not present, the CCT is considered unknown or unspecified.
- [var whiteBalanceRedFactor: Float32](cvproresrawmetadata/whitebalanceredfactor.md)
  The white balance multiplication factor for red-filtered sensels.
- [var whiteLevel: Int32](cvproresrawmetadata/whitelevel.md)
  The sensel level corresponding to sensor (or camera A-to-D converter) saturation.

## Relationships

### Conforms To
- [CVAttachmentValueRepresentable](cvattachmentvaluerepresentable.md)
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
- [struct CVPixelBufferPlaneProperties](cvpixelbufferplaneproperties.md)
  Properties of a plane of pixels in pixel buffer


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvproresrawmetadata)*