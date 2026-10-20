# CVPixelFormatDescription.Compatibility

**Framework**: Core Video  
**Kind**: struct  
**Role**: Structure

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
- [static let cgBitmapContext: CVPixelFormatDescription.Compatibility](./compatibility/cgbitmapcontext.md)
  The pixel format is compatible with a Core Graphics bitmap context.
- [static let cgImage: CVPixelFormatDescription.Compatibility](./compatibility/cgimage.md)
  The pixel format is compatible with a Core Graphics image.
- [static let ioSurfaceCoreAnimation: CVPixelFormatDescription.Compatibility](./compatibility/iosurfacecoreanimation.md)
  The CVPixelBuffer’s IOSurface is compatible with CoreAnimation CALayer.
- [static let metalTexture: CVPixelFormatDescription.Compatibility](./compatibility/metaltexture.md)
  The pixel format is compatible with a Metal texture.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../../Swift/expressiblebyarrayliteral.md)
- [Hashable](../../Swift/hashable.md)
- [OptionSet](../../Swift/optionset.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)
- [SetAlgebra](../../Swift/setalgebra.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvpixelformatdescription/compatibility)*