# CVImageAlphaChannelMode

**Framework**: Core Video  
**Kind**: enum  
**Role**: Enumeration

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
enum CVImageAlphaChannelMode
```

## Topics

### Enumeration Cases
- [CVImageAlphaChannelMode.premultipliedAlpha](./cvimagealphachannelmode/premultipliedalpha.md)
- [CVImageAlphaChannelMode.straightAlpha](./cvimagealphachannelmode/straightalpha.md)

## Relationships

### Conforms To
- [CVAttachmentValueRepresentable](./cvattachmentvaluerepresentable.md)
- [Copyable](../Swift/copyable.md)
- [Equatable](../Swift/equatable.md)
- [Escapable](../Swift/escapable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Color and signal characteristics
- [enum CVImageColorPrimaries](./cvimagecolorprimaries.md)
  Color primaries describe the gamut used for the rendering intent of an image.
- [enum CVImageTransferFunction](./cvimagetransferfunction.md)
  The transfer function describes the tonality of an image for use in color matching operations. This value is used along with a color primaries gamut [`CVImageColorPrimaries`](./cvimagecolorprimaries.md). Most apps should use the [`CVImageTransferFunction.itu_R_709_2`](./cvimagetransferfunction/itu_r_709_2.md) transfer function.
- [enum CVImageLogTransferFunction](./cvimagelogtransferfunction.md)
  Identifies the specific log curve transfer function or gamma of the content.
- [enum CVImageYCbCrMatrix](./cvimageycbcrmatrix.md)
  Indicates color matrix used for converting image buffer from YCbCr to RGB.
- [enum CVImageFieldDetail](./cvimagefielddetail.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvimagealphachannelmode)*