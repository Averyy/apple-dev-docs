# init(colorSpace:red:green:blue:opacity:)

**Framework**: SwiftUI  
**Kind**: init

Creates a resolved color from red, green, and blue component values.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
init(colorSpace: Color.RGBColorSpace = .sRGB, red: Float, green: Float, blue: Float, opacity: Float = 1)
```

#### Discussion

A standard sRGB color space clamps each color component — `red`, `green`, and `blue` — to a range of `0` to `1`, but SwiftUI colors use an extended sRGB color space, so you can use component values outside that range. This makes it possible to create colors using the [`Color.RGBColorSpace.sRGB`](color/rgbcolorspace/srgb.md) or [`Color.RGBColorSpace.sRGBLinear`](color/rgbcolorspace/srgblinear.md) color space that make full use of the wider gamut of a diplay that supports [`Color.RGBColorSpace.displayP3`](color/rgbcolorspace/displayp3.md).

## Parameters

- `colorSpace`: The profile that specifies how to interpret the   color for display. The default is  .
- `red`: The amount of red in the color.
- `green`: The amount of green in the color.
- `blue`: The amount of blue in the color.
- `opacity`: An optional degree of opacity, given in the range    to  . A value of   means 100% transparency, while a value of    means 100% opacity. The default is  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/color/resolved/init(colorspace:red:green:blue:opacity:))*