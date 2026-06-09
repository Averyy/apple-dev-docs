# CVImageFieldDetail

**Framework**: Core Video  
**Kind**: enum

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
enum CVImageFieldDetail
```

## Topics

### Enumeration Cases
- [CVImageFieldDetail.spatialFirstLineEarly](cvimagefielddetail/spatialfirstlineearly.md)
  The image buffer contains interleaved fields. The first line of image data corresponds to the first top, odd-numbered, field.
- [CVImageFieldDetail.spatialFirstLineLate](cvimagefielddetail/spatialfirstlinelate.md)
  The image buffer contains interleaved fields. The first line of image data corresponds to the first bottom, even-numbered, field.
- [CVImageFieldDetail.temporalBottomFirst](cvimagefielddetail/temporalbottomfirst.md)
  The image buffer contains complete fields in alternating order. The bottom, even-numbered, fields contain image data captured at an earlier time than top, odd-numbered, fields.
- [CVImageFieldDetail.temporalTopFirst](cvimagefielddetail/temporaltopfirst.md)
  The image buffer contains complete fields in alternating order. The top, odd-numbered, fields contain image data captured at an earlier time than bottom, even-numbered, fields.

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

- [enum CVImageColorPrimaries](cvimagecolorprimaries.md)
  Color primaries describe the gamut used for the rendering intent of an image.
- [enum CVImageTransferFunction](cvimagetransferfunction.md)
  The transfer function describes the tonality of an image for use in color matching operations. This value is used along with a color primaries gamut [`CVImageColorPrimaries`](cvimagecolorprimaries.md). Most apps should use the [`CVImageTransferFunction.itu_R_709_2`](cvimagetransferfunction/itu_r_709_2.md) transfer function.
- [enum CVImageLogTransferFunction](cvimagelogtransferfunction.md)
  Identifies the specific log curve transfer function or gamma of the content.
- [enum CVImageYCbCrMatrix](cvimageycbcrmatrix.md)
  Indicates color matrix used for converting image buffer from YCbCr to RGB.
- [enum CVImageAlphaChannelMode](cvimagealphachannelmode.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvimagefielddetail)*