# CVSenselArrayPattern

**Framework**: Core Video  
**Kind**: enum

Pattern indicating sensel arrangement.

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
enum CVSenselArrayPattern
```

## Topics

### Enumeration Cases
- [CVSenselArrayPattern.bayerBGGR](cvsenselarraypattern/bayerbggr.md)
  Top-left sensel of the frame is blue-filtered.
- [CVSenselArrayPattern.bayerGBRG](cvsenselarraypattern/bayergbrg.md)
  Top-left sensel of the frame is green-filtered, with the top row alternating between green and blue-filtered sensels.
- [CVSenselArrayPattern.bayerGRBG](cvsenselarraypattern/bayergrbg.md)
  Top-left sensel of the frame is green-filtered, with the top row alternating between green and red-filtered sensels.
- [CVSenselArrayPattern.bayerRGGB](cvsenselarraypattern/bayerrggb.md)
  Top-left sensel of the frame is red-filtered.

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

- [struct CVPixelFormatDescription](cvpixelformatdescription.md)
  Defines a pixel format which can be used to create custom pixel buffer types.
- [struct CVFillExtendedPixelsCallBackData](cvfillextendedpixelscallbackdata.md)
  A structure for holding information that describes a custom extended pixel fill algorithm.
- [struct CVPixelFormatType](cvpixelformattype.md)
  Identifier for a pixel format type
- [struct CVSenselSitingOffsets](cvsenselsitingoffsets.md)
  Siting offsets, relative to pixel center, of individual sensels/components constituting each pixel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvsenselarraypattern)*