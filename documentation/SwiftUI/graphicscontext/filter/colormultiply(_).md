# colorMultiply(_:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Type Method

Returns a filter that multiplies each color component by the matching component of a given color.

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
static func colorMultiply(_ color: Color) -> GraphicsContext.Filter
```

## Return Value

A filter that multiplies color components.

## Parameters

- `color`: The color that the filter uses for the multiplication operation.

## See Also

### Manipulating color
- [static func saturation(Double) -> GraphicsContext.Filter](./saturation%28_%29.md)
  Returns a filter that applies a saturation adjustment.
- [static func colorInvert(Double) -> GraphicsContext.Filter](./colorinvert%28_%29.md)
  Returns a filter that inverts the color of their results.
- [static func hueRotation(Angle) -> GraphicsContext.Filter](./huerotation%28_%29.md)
  Returns a filter that applies a hue rotation adjustment.
- [static func grayscale(Double) -> GraphicsContext.Filter](./grayscale%28_%29.md)
  Returns a filter that applies a grayscale adjustment.
- [static func colorMatrix(ColorMatrix) -> GraphicsContext.Filter](./colormatrix%28_%29.md)
  Returns a filter that multiplies by a given color matrix.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/graphicscontext/filter/colormultiply(_:))*