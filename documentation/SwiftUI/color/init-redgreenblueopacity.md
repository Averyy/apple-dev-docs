# init(_:red:green:blue:opacity:)

**Framework**: SwiftUI  
**Kind**: init

Creates a constant color from red, green, and blue component values.

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
init(_ colorSpace: Color.RGBColorSpace = .sRGB, red: Double, green: Double, blue: Double, opacity: Double = 1)
```

#### Discussion

This initializer creates a constant color that doesn’t change based on context. For example, it doesn’t have distinct light and dark appearances, unlike various system-defined colors, or a color that you load from an Asset Catalog with [`init(_:bundle:)`](color/init(_:bundle:).md).

A standard sRGB color space clamps each color component — `red`, `green`, and `blue` — to a range of `0` to `1`, but SwiftUI colors use an extended sRGB color space, so you can use component values outside that range. This makes it possible to create colors using the [`Color.RGBColorSpace.sRGB`](color/rgbcolorspace/srgb.md) or [`Color.RGBColorSpace.sRGBLinear`](color/rgbcolorspace/srgblinear.md) color space that make full use of the wider gamut of a diplay that supports [`Color.RGBColorSpace.displayP3`](color/rgbcolorspace/displayp3.md).

## Parameters

- `colorSpace`: The profile that specifies how to interpret the color   for display. The default is  .
- `red`: The amount of red in the color.
- `green`: The amount of green in the color.
- `blue`: The amount of blue in the color.
- `opacity`: An optional degree of opacity, given in the range   to   . A value of   means 100% transparency, while a value of    means 100% opacity. The default is  .

## See Also

- [init(hue: Double, saturation: Double, brightness: Double, opacity: Double)](color/init(hue:saturation:brightness:opacity:).md)
  Creates a constant color from hue, saturation, and brightness values.
- [init(Color.RGBColorSpace, white: Double, opacity: Double)](color/init(_:white:opacity:).md)
  Creates a constant grayscale color.
- [Color.RGBColorSpace](color/rgbcolorspace.md)
  A profile that specifies how to interpret a color value for display.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/color/init(_:red:green:blue:opacity:))*