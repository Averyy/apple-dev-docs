# colorMatrix(_:isPremultiplied:)

**Framework**: SwiftUI  
**Kind**: method

Returns a filter that multiplies by a given color matrix.

**Availability**:
- iOS 18.2+
- iPadOS 18.2+
- Mac Catalyst 18.2+
- macOS 15.2+
- tvOS 18.2+
- visionOS 2.2+
- watchOS 11.2+

## Declaration

```swift
static func colorMatrix(_ matrix: ColorMatrix, isPremultiplied: Bool) -> GraphicsContext.Filter
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

- `matrix`: A [`ColorMatrix`](colormatrix.md) instance used by the filter.
- `isPremultiplied`: Whether the matrix is intended to be applied to color components that have been multiplied by their opacity value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/graphicscontext/filter/colormatrix(_:ispremultiplied:))*