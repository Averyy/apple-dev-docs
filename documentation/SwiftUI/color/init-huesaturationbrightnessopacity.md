# init(hue:saturation:brightness:opacity:)

**Framework**: SwiftUI  
**Kind**: init

Creates a constant color from hue, saturation, and brightness values.

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
init(hue: Double, saturation: Double, brightness: Double, opacity: Double = 1)
```

#### Discussion

This initializer creates a constant color that doesn’t change based on context. For example, it doesn’t have distinct light and dark appearances, unlike various system-defined colors, or a color that you load from an Asset Catalog with [`init(_:bundle:)`](color/init(_:bundle:).md).

## Parameters

- `hue`: A value in the range   to   that maps to an angle   from 0° to 360° to represent a shade on the color wheel.
- `saturation`: A value in the range   to   that indicates   how strongly the hue affects the color. A value of   removes the   effect of the hue, resulting in gray. As the value increases,   the hue becomes more prominent.
- `brightness`: A value in the range   to   that indicates   how bright a color is. A value of   results in black, regardless   of the other components. The color lightens as you increase this   component.
- `opacity`: An optional degree of opacity, given in the range   to   . A value of   means 100% transparency, while a value of    means 100% opacity. The default is  .

## See Also

- [init(Color.RGBColorSpace, white: Double, opacity: Double)](color/init(_:white:opacity:).md)
  Creates a constant grayscale color.
- [init(Color.RGBColorSpace, red: Double, green: Double, blue: Double, opacity: Double)](color/init(_:red:green:blue:opacity:).md)
  Creates a constant color from red, green, and blue component values.
- [Color.RGBColorSpace](color/rgbcolorspace.md)
  A profile that specifies how to interpret a color value for display.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/color/init(hue:saturation:brightness:opacity:))*