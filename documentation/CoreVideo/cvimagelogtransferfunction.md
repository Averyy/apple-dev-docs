# CVImageLogTransferFunction

**Framework**: Core Video  
**Kind**: enum

Identifies the specific log curve transfer function or gamma of the content.

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
enum CVImageLogTransferFunction
```

#### Overview

Log is a specific video format usually processed in a camera’s ISP. A Log video format usually defines:

- Scene-referred color primaries designed to preserve the chromaticity range captured by a camera sensor. In cinematography, “scene-referred” color primaries refers to a color space designed to accurately preserve the chromaticity and dynamic range directly captured by a camera sensor.
- A specific gamma curve (or transfer characteristic) tailored to capturing the full dynamic range from the sensor. This gamma curve is usually shaped like a log curve (hence the name Log).
- A set of matrix transforms to go from RGB to Y’CbCr (Y’CbCr being the most common format used to store the bits compressed into a file).

As described above, a Log video format defines a whole color space (even though the “log” part of the name comes only from the “transfer characteristic” or gamma curve).

## Topics

### Enumeration Cases
- [CVImageLogTransferFunction.appleLog](cvimagelogtransferfunction/applelog.md)
  Apple log profile.
- [CVImageLogTransferFunction.appleLog2](cvimagelogtransferfunction/applelog2.md)
  Apple log 2 profile.

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
- [enum CVImageYCbCrMatrix](cvimageycbcrmatrix.md)
  Indicates color matrix used for converting image buffer from YCbCr to RGB.
- [enum CVImageAlphaChannelMode](cvimagealphachannelmode.md)
- [enum CVImageFieldDetail](cvimagefielddetail.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvimagelogtransferfunction)*