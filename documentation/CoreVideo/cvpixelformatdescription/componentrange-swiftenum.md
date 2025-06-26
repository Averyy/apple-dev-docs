# CVPixelFormatDescription.ComponentRange

**Framework**: Core Video  
**Kind**: enum

Range of colors supported by pixel components.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

## Declaration

```swift
enum ComponentRange
```

## Topics

### Enumeration Cases
- [CVPixelFormatDescription.ComponentRange.full](cvpixelformatdescription/componentrange-swift.enum/full.md)
  Indicates that this component represents the nominal range of values in a color component using the full range of (usually integer) values. For example, in 8 bit YCbCr formats, full range indicates that the -1.0 to 1.0 range for chroma components is represented by the values 0 to 255.
- [CVPixelFormatDescription.ComponentRange.video](cvpixelformatdescription/componentrange-swift.enum/video.md)
  Indicates that this component represents the nominal range of values in a color component using a reduced range of (usually integer) values. For example, in 8-bit YCbCr formats, video range indicates that a -1.0 to 1.0 range for chroma components is represented by the values 16 to 240, while the range of luma components is typically 16 to 235.  Values outside this range are still used for certain signaling purposes.
- [CVPixelFormatDescription.ComponentRange.wide](cvpixelformatdescription/componentrange-swift.enum/wide.md)
  Indicates that this component represents the nominal range of values in a color component using a dramatically reduced range of integer values, in order to allow expression of values broadly outside the normal -1.0 to 1.0 and/or 0.0 to 1.0 ranges.  For example, formats supporting Extended sRGB allow component values that are less than 0.0 or greater than 1.0 in order to depict colors outside the sRGB colorimetry.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvpixelformatdescription/componentrange-swift.enum)*