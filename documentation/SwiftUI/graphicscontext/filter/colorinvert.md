# colorInvert(_:)

**Framework**: SwiftUI  
**Kind**: method

Returns a filter that inverts the color of their results.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
static func colorInvert(_ amount: Double = 1) -> GraphicsContext.Filter
```

#### Return Value

A filter that applies a color inversion.

#### Discussion

This filter is equivalent to the `invert` filter primitive defined by the Scalable Vector Graphics (SVG) specification.

## Parameters

- `amount`: The inversion amount. A value of one results in total   inversion, while a value of zero leaves the result unchanged.   Other values apply a linear multiplier effect.

## See Also

- [static func saturation(Double) -> GraphicsContext.Filter](graphicscontext/filter/saturation(_:).md)
  Returns a filter that applies a saturation adjustment.
- [static func colorMultiply(Color) -> GraphicsContext.Filter](graphicscontext/filter/colormultiply(_:).md)
  Returns a filter that multiplies each color component by the matching component of a given color.
- [static func hueRotation(Angle) -> GraphicsContext.Filter](graphicscontext/filter/huerotation(_:).md)
  Returns a filter that applies a hue rotation adjustment.
- [static func grayscale(Double) -> GraphicsContext.Filter](graphicscontext/filter/grayscale(_:).md)
  Returns a filter that applies a grayscale adjustment.
- [static func colorMatrix(ColorMatrix) -> GraphicsContext.Filter](graphicscontext/filter/colormatrix(_:).md)
  Returns a filter that multiplies by a given color matrix.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/graphicscontext/filter/colorinvert(_:))*