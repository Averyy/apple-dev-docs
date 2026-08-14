# CVPixelFormatDescription.Compatibility

**Framework**: Core Video  
**Kind**: struct

A set of options that control compatibility between different pixel formats.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
struct Compatibility
```

## Topics

### Type Properties
- [static let cgBitmapContext: CVPixelFormatDescription.Compatibility](cvpixelformatdescription/compatibility/cgbitmapcontext.md)
  The pixel format is compatible with a Core Graphics bitmap context.
- [static let cgImage: CVPixelFormatDescription.Compatibility](cvpixelformatdescription/compatibility/cgimage.md)
  The pixel format is compatible with a Core Graphics image.
- [static let ioSurfaceCoreAnimation: CVPixelFormatDescription.Compatibility](cvpixelformatdescription/compatibility/iosurfacecoreanimation.md)
  The CVPixelBuffer’s IOSurface is compatible with CoreAnimation CALayer.
- [static let metalTexture: CVPixelFormatDescription.Compatibility](cvpixelformatdescription/compatibility/metaltexture.md)
  The pixel format is compatible with a Metal texture.

## Relationships

### Conforms To
- [Equatable](../swift/equatable.md)
- [ExpressibleByArrayLiteral](../swift/expressiblebyarrayliteral.md)
- [Hashable](../swift/hashable.md)
- [OptionSet](../swift/optionset.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)
- [SetAlgebra](../swift/setalgebra.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvpixelformatdescription/compatibility)*