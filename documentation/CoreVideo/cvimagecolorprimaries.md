# CVImageColorPrimaries

**Framework**: Core Video  
**Kind**: enum

Color primaries describe the gamut used for the rendering intent of an image.

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
enum CVImageColorPrimaries
```

#### Overview

This value is primarily used in color matching operations, along with a transfer function specified as [`CVImageTransferFunction`](cvimagetransferfunction.md).

## Topics

### Enumeration Cases
- [CVImageColorPrimaries.dci_P3](cvimagecolorprimaries/dci_p3.md)
  Color primaries gamut for DCI P3 theatrical distribution video.
- [CVImageColorPrimaries.ebu_3213](cvimagecolorprimaries/ebu_3213.md)
  Color primaries gamut for PAL video.
- [CVImageColorPrimaries.itu_R_2020](cvimagecolorprimaries/itu_r_2020.md)
  Color primaries gamut for ITU-R BT2020 HDR video.
- [CVImageColorPrimaries.itu_R_709_2](cvimagecolorprimaries/itu_r_709_2.md)
  Color primaries gamut for HD video.
- [CVImageColorPrimaries.p22](cvimagecolorprimaries/p22.md)
  Color primaries gamut for sRGB video.
- [CVImageColorPrimaries.p3_D65](cvimagecolorprimaries/p3_d65.md)
  Color primaries gamut for DCI P3 video with D65 white point.
- [CVImageColorPrimaries.smpte_C](cvimagecolorprimaries/smpte_c.md)
  Color primaries gamut for standard-definition video.

## Relationships

### Conforms To
- [CVAttachmentValueRepresentable](cvattachmentvaluerepresentable.md)
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Escapable](../Swift/Escapable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [enum CVImageTransferFunction](cvimagetransferfunction.md)
  The transfer function describes the tonality of an image for use in color matching operations. This value is used along with a color primaries gamut [`CVImageColorPrimaries`](cvimagecolorprimaries.md). Most apps should use the [`CVImageTransferFunction.itu_R_709_2`](cvimagetransferfunction/itu_r_709_2.md) transfer function.
- [enum CVImageLogTransferFunction](cvimagelogtransferfunction.md)
  Identifies the specific log curve transfer function or gamma of the content.
- [enum CVImageYCbCrMatrix](cvimageycbcrmatrix.md)
  Indicates color matrix used for converting image buffer from YCbCr to RGB.
- [enum CVImageAlphaChannelMode](cvimagealphachannelmode.md)
- [enum CVImageFieldDetail](cvimagefielddetail.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvimagecolorprimaries)*