# CVPixelFormatDescription.Compatibility

**Framework**: Core Video  
**Kind**: struct

A set of options that control compatibility between different pixel formats.

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
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [Hashable](../Swift/Hashable.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [SetAlgebra](../Swift/SetAlgebra.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvpixelformatdescription/compatibility)*