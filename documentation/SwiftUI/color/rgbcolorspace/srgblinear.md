# Color.RGBColorSpace.sRGBLinear

**Framework**: SwiftUI  
**Kind**: case

The extended sRGB color space with a linear transfer function.

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
case sRGBLinear
```

#### Discussion

This color space has the same colorimetry as [`Color.RGBColorSpace.sRGB`](color/rgbcolorspace/srgb.md), but uses a linear transfer function.

Standard sRGB color spaces clamp the red, green, and blue components of a color to a range of `0` to `1`, but SwiftUI colors use an extended sRGB color space, so you can use component values outside that range.

## See Also

- [Color.RGBColorSpace.sRGB](color/rgbcolorspace/srgb.md)
  The extended red, green, blue (sRGB) color space.
- [Color.RGBColorSpace.displayP3](color/rgbcolorspace/displayp3.md)
  The Display P3 color space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/color/rgbcolorspace/srgblinear)*