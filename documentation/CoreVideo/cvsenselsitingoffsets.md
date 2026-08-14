# CVSenselSitingOffsets

**Framework**: Core Video  
**Kind**: struct

Siting offsets, relative to pixel center, of individual sensels/components constituting each pixel.

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
struct CVSenselSitingOffsets
```

## Topics

### Structures
- [CVSenselSitingOffsets.Offset](cvsenselsitingoffsets/offset.md)
  Siting offset of a component, relative to pixel center.
### Initializers
- [init(red: CVSenselSitingOffsets.Offset, green: CVSenselSitingOffsets.Offset, blue: CVSenselSitingOffsets.Offset, alpha: CVSenselSitingOffsets.Offset)](cvsenselsitingoffsets/init(red:green:blue:alpha:).md)
### Instance Properties
- [var alpha: CVSenselSitingOffsets.Offset](cvsenselsitingoffsets/alpha.md)
- [var blue: CVSenselSitingOffsets.Offset](cvsenselsitingoffsets/blue.md)
- [var green: CVSenselSitingOffsets.Offset](cvsenselsitingoffsets/green.md)
- [var red: CVSenselSitingOffsets.Offset](cvsenselsitingoffsets/red.md)
### Type Properties
- [static let zero: CVSenselSitingOffsets](cvsenselsitingoffsets/zero.md)

## Relationships

### Conforms To
- [CVAttachmentValueRepresentable](cvattachmentvaluerepresentable.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [struct CVPixelFormatDescription](cvpixelformatdescription.md)
  Defines a pixel format which can be used to create custom pixel buffer types.
- [struct CVFillExtendedPixelsCallBackData](cvfillextendedpixelscallbackdata.md)
  A structure for holding information that describes a custom extended pixel fill algorithm.
- [struct CVPixelFormatType](cvpixelformattype.md)
  Identifier for a pixel format type
- [enum CVSenselArrayPattern](cvsenselarraypattern.md)
  Pattern indicating sensel arrangement.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvsenselsitingoffsets)*