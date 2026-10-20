# Color.RGBColorSpace

**Framework**: SwiftUI  
**Kind**: enum  
**Role**: Enumeration

A profile that specifies how to interpret a color value for display.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
enum RGBColorSpace
```

## Topics

### Getting color spaces
- [Color.RGBColorSpace.sRGB](./rgbcolorspace/srgb.md)
  The extended red, green, blue (sRGB) color space.
- [Color.RGBColorSpace.sRGBLinear](./rgbcolorspace/srgblinear.md)
  The extended sRGB color space with a linear transfer function.
- [Color.RGBColorSpace.displayP3](./rgbcolorspace/displayp3.md)
  The Display P3 color space.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Creating a color from component values
- [init(hue: Double, saturation: Double, brightness: Double, opacity: Double)](./init%28hue,saturation,brightness,opacity%29.md)
  Creates a constant color from hue, saturation, and brightness values.
- [init(Color.RGBColorSpace, white: Double, opacity: Double)](./init%28_,white,opacity%29.md)
  Creates a constant grayscale color.
- [init(Color.RGBColorSpace, red: Double, green: Double, blue: Double, opacity: Double)](./init%28_,red,green,blue,opacity%29.md)
  Creates a constant color from red, green, and blue component values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/color/rgbcolorspace)*