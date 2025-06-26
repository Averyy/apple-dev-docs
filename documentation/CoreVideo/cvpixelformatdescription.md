# CVPixelFormatDescription

**Framework**: Core Video  
**Kind**: struct

Defines a pixel format which can be used to create custom pixel buffer types.

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
struct CVPixelFormatDescription
```

## Topics

### Classes
- [CVPixelFormatDescription.Registry](cvpixelformatdescription/registry.md)
  Registry of all pixel formats.
### Structures
- [CVPixelFormatDescription.Compatibility](cvpixelformatdescription/compatibility.md)
  A set of options that control compatibility between different pixel formats.
- [CVPixelFormatDescription.Components](cvpixelformatdescription/components-swift.struct.md)
  Defines the color components represented by pixels in the buffer.
- [CVPixelFormatDescription.Dimensions](cvpixelformatdescription/dimensions.md)
  Holds integer horizontal and vertical dimension quantities
- [CVPixelFormatDescription.PixelLayout](cvpixelformatdescription/pixellayout.md)
  Defines pixel layout of a buffer plane or the entire buffer if the format is non-planar.
### Initializers
- [init(pixelFormatType: CVPixelFormatType, name: String, components: CVPixelFormatDescription.Components, componentRange: CVPixelFormatDescription.ComponentRange?, planeConfiguration: CVPixelFormatDescription.PlaneConfiguration)](cvpixelformatdescription/init(pixelformattype:name:components:componentrange:planeconfiguration:).md)
### Instance Properties
- [var componentRange: CVPixelFormatDescription.ComponentRange?](cvpixelformatdescription/componentrange-swift.property.md)
  Color gamut of format
- [var components: CVPixelFormatDescription.Components](cvpixelformatdescription/components-swift.property.md)
  Color components carried by the pixel buffer
- [var name: String](cvpixelformatdescription/name.md)
  The canonical name for the format. This should be the same as the codec name you’d use in QT.
- [var pixelFormatType: CVPixelFormatType](cvpixelformatdescription/pixelformattype.md)
  Pixel format to be use for associating pixel buffers with this format.
- [var planeConfiguration: CVPixelFormatDescription.PlaneConfiguration](cvpixelformatdescription/planeconfiguration-swift.property.md)
  Defines planar or non-planar configuration
### Enumerations
- [CVPixelFormatDescription.ComponentRange](cvpixelformatdescription/componentrange-swift.enum.md)
  Range of colors supported by pixel components.
- [CVPixelFormatDescription.PlaneConfiguration](cvpixelformatdescription/planeconfiguration-swift.enum.md)
  Defines how color components in the buffer are arranged.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvpixelformatdescription)*