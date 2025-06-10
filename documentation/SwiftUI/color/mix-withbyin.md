# mix(with:by:in:)

**Framework**: SwiftUI  
**Kind**: method

Returns a version of self mixed with `rhs` by the amount specified by `fraction`.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
func mix(with rhs: Color, by fraction: Double, in colorSpace: Gradient.ColorSpace = .perceptual) -> Color
```

#### Return Value

A new `Color` based on `self` and `rhs`.

## Parameters

- `rhs`: The color to mix   with.
- `fraction`: The amount of blending,   means   is mixed in   equal parts with  .
- `colorSpace`: The color space used to mix the colors.

## See Also

- [func opacity(Double) -> Color](color/opacity(_:).md)
  Multiplies the opacity of the color by the given amount.
- [var gradient: AnyGradient](color/gradient.md)
  Returns the standard gradient for the color `self`.
- [func exposureAdjust(Double) -> Color](color/exposureadjust(_:).md)
  Returns a new color with an exposure adjustment applied.
- [func headroom(Double?) -> Color](color/headroom(_:).md)
  Creates a new color with specified HDR content headroom.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/color/mix(with:by:in:))*