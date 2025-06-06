# Color.RGBColorSpace

**Framework**: SwiftUI  
**Kind**: enum

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
- [Color.RGBColorSpace.sRGB](color/rgbcolorspace/srgb.md)
  The extended red, green, blue (sRGB) color space.
- [Color.RGBColorSpace.sRGBLinear](color/rgbcolorspace/srgblinear.md)
  The extended sRGB color space with a linear transfer function.
- [Color.RGBColorSpace.displayP3](color/rgbcolorspace/displayp3.md)
  The Display P3 color space.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [init(hue: Double, saturation: Double, brightness: Double, opacity: Double)](color/init(hue:saturation:brightness:opacity:).md)
  Creates a constant color from hue, saturation, and brightness values.
- [init(Color.RGBColorSpace, white: Double, opacity: Double)](color/init(_:white:opacity:).md)
  Creates a constant grayscale color.
- [init(Color.RGBColorSpace, red: Double, green: Double, blue: Double, opacity: Double)](color/init(_:red:green:blue:opacity:).md)
  Creates a constant color from red, green, and blue component values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/color/rgbcolorspace)*