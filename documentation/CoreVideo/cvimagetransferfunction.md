# CVImageTransferFunction

**Framework**: Core Video  
**Kind**: enum

The transfer function describes the tonality of an image for use in color matching operations. This value is used along with a color primaries gamut [`CVImageColorPrimaries`](cvimagecolorprimaries.md). Most apps should use the [`CVImageTransferFunction.itu_R_709_2`](cvimagetransferfunction/itu_r_709_2.md) transfer function.

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
enum CVImageTransferFunction
```

## Topics

### Enumeration Cases
- [CVImageTransferFunction.itu_R_2020](cvimagetransferfunction/itu_r_2020.md)
  The transfer function for HDR video specified in ITU-R BT2020 standard.
- [CVImageTransferFunction.itu_R_2100_HLG](cvimagetransferfunction/itu_r_2100_hlg.md)
  The transfer function for HDR video specified in ITU-R BT2020 HLG standard.
- [CVImageTransferFunction.itu_R_709_2](cvimagetransferfunction/itu_r_709_2.md)
  The default transfer function for high-definition and standard-definition video.
- [CVImageTransferFunction.linear](cvimagetransferfunction/linear.md)
- [CVImageTransferFunction.sRGB](cvimagetransferfunction/srgb.md)
  The standard transfer function for web and desktop publishing.
- [CVImageTransferFunction.smpte_240M_1995](cvimagetransferfunction/smpte_240m_1995.md)
  The transfer function for HDTV interim video.
- [CVImageTransferFunction.smpte_ST_2084_PQ](cvimagetransferfunction/smpte_st_2084_pq.md)
  The transfer function for mapping HDR gamma to absolute light levels.
- [CVImageTransferFunction.smpte_ST_428_1](cvimagetransferfunction/smpte_st_428_1.md)
  The transfer function for digital cinema distribution master.
- [CVImageTransferFunction.useGamma](cvimagetransferfunction/usegamma.md)
  The transfer function that’s defined by the gamma level value of the image buffer.

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
- [enum CVImageLogTransferFunction](cvimagelogtransferfunction.md)
  Identifies the specific log curve transfer function or gamma of the content.
- [enum CVImageYCbCrMatrix](cvimageycbcrmatrix.md)
  Indicates color matrix used for converting image buffer from YCbCr to RGB.
- [enum CVImageAlphaChannelMode](cvimagealphachannelmode.md)
- [enum CVImageFieldDetail](cvimagefielddetail.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvimagetransferfunction)*