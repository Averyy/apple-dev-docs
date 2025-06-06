# colorMatrix(_:)

**Framework**: SwiftUI  
**Kind**: method

Returns a filter that multiplies by a given color matrix.

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
static func colorMatrix(_ matrix: ColorMatrix) -> GraphicsContext.Filter
```

#### Return Value

A filter that transforms color using the given matrix.

#### Discussion

This filter is equivalent to the `feColorMatrix` filter primitive defined by the Scalable Vector Graphics (SVG) specification.

The filter creates the output color `[R', G', B', A']` at each pixel from an input color `[R, G, B, A]` by multiplying the input color by the square matrix formed by the first four columns of the [`ColorMatrix`](colormatrix.md), then adding the fifth column to the result:

```swift
R' = r1 ✕ R + r2 ✕ G + r3 ✕ B + r4 ✕ A + r5
G' = g1 ✕ R + g2 ✕ G + g3 ✕ B + g4 ✕ A + g5
B' = b1 ✕ R + b2 ✕ G + b3 ✕ B + b4 ✕ A + b5
A' = a1 ✕ R + a2 ✕ G + a3 ✕ B + a4 ✕ A + a5
```

## Parameters

- `matrix`: A   instance used by the filter.

## See Also

- [static func saturation(Double) -> GraphicsContext.Filter](graphicscontext/filter/saturation(_:).md)
  Returns a filter that applies a saturation adjustment.
- [static func colorInvert(Double) -> GraphicsContext.Filter](graphicscontext/filter/colorinvert(_:).md)
  Returns a filter that inverts the color of their results.
- [static func colorMultiply(Color) -> GraphicsContext.Filter](graphicscontext/filter/colormultiply(_:).md)
  Returns a filter that multiplies each color component by the matching component of a given color.
- [static func hueRotation(Angle) -> GraphicsContext.Filter](graphicscontext/filter/huerotation(_:).md)
  Returns a filter that applies a hue rotation adjustment.
- [static func grayscale(Double) -> GraphicsContext.Filter](graphicscontext/filter/grayscale(_:).md)
  Returns a filter that applies a grayscale adjustment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/graphicscontext/filter/colormatrix(_:))*