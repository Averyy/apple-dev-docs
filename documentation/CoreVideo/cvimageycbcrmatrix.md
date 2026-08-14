# CVImageYCbCrMatrix

**Framework**: Core Video  
**Kind**: enum

Indicates color matrix used for converting image buffer from YCbCr to RGB.

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
enum CVImageYCbCrMatrix
```

## Topics

### Enumeration Cases
- [CVImageYCbCrMatrix.itu_R_2020](cvimageycbcrmatrix/itu_r_2020.md)
  The conversion matrix for UHDTV digital television images, that follows the ITU Rec 2020 standard.
- [CVImageYCbCrMatrix.itu_R_601_4](cvimageycbcrmatrix/itu_r_601_4.md)
  The conversion matrix for standard definition television images, that follows the ITU R 601 standard.
- [CVImageYCbCrMatrix.itu_R_709_2](cvimageycbcrmatrix/itu_r_709_2.md)
  The conversion matrix for HDTV digital television images, that follows the ITU R 709 standard.
- [CVImageYCbCrMatrix.smpte_240M_1995](cvimageycbcrmatrix/smpte_240m_1995.md)
  The conversion matrix for 1920 x 1135 HDTV images, that follows the SMPTE 240M 1995 standard.

## Relationships

### Conforms To
- [CVAttachmentValueRepresentable](cvattachmentvaluerepresentable.md)
- [Copyable](../swift/copyable.md)
- [Equatable](../swift/equatable.md)
- [Escapable](../swift/escapable.md)
- [Hashable](../swift/hashable.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [enum CVImageColorPrimaries](cvimagecolorprimaries.md)
  Color primaries describe the gamut used for the rendering intent of an image.
- [enum CVImageTransferFunction](cvimagetransferfunction.md)
  The transfer function describes the tonality of an image for use in color matching operations. This value is used along with a color primaries gamut [`CVImageColorPrimaries`](cvimagecolorprimaries.md). Most apps should use the [`CVImageTransferFunction.itu_R_709_2`](cvimagetransferfunction/itu_r_709_2.md) transfer function.
- [enum CVImageLogTransferFunction](cvimagelogtransferfunction.md)
  Identifies the specific log curve transfer function or gamma of the content.
- [enum CVImageAlphaChannelMode](cvimagealphachannelmode.md)
- [enum CVImageFieldDetail](cvimagefielddetail.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvimageycbcrmatrix)*