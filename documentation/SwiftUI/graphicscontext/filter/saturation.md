# saturation(_:)

**Framework**: SwiftUI  
**Kind**: method

Returns a filter that applies a saturation adjustment.

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
static func saturation(_ amount: Double) -> GraphicsContext.Filter
```

#### Return Value

A filter that applies a saturation adjustment.

#### Discussion

This filter is equivalent to the `saturate` filter primitive defined by the Scalable Vector Graphics (SVG) specification.

## Parameters

- `amount`: The amount of the saturation adjustment. A value   of zero to completely desaturates each pixel, while a value of   one makes no change. You can use values greater than one.

## See Also

- [static func colorInvert(Double) -> GraphicsContext.Filter](graphicscontext/filter/colorinvert(_:).md)
  Returns a filter that inverts the color of their results.
- [static func colorMultiply(Color) -> GraphicsContext.Filter](graphicscontext/filter/colormultiply(_:).md)
  Returns a filter that multiplies each color component by the matching component of a given color.
- [static func hueRotation(Angle) -> GraphicsContext.Filter](graphicscontext/filter/huerotation(_:).md)
  Returns a filter that applies a hue rotation adjustment.
- [static func grayscale(Double) -> GraphicsContext.Filter](graphicscontext/filter/grayscale(_:).md)
  Returns a filter that applies a grayscale adjustment.
- [static func colorMatrix(ColorMatrix) -> GraphicsContext.Filter](graphicscontext/filter/colormatrix(_:).md)
  Returns a filter that multiplies by a given color matrix.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/graphicscontext/filter/saturation(_:))*