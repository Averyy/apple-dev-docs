# opacity(_:)

**Framework**: SwiftUI  
**Kind**: method

Multiplies the opacity of the color by the given amount.

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
func opacity(_ opacity: Double) -> Color
```

#### Return Value

A view with modified opacity.

## Parameters

- `opacity`: The amount by which to multiply the opacity of the   color.

## See Also

- [var gradient: AnyGradient](color/gradient.md)
  Returns the standard gradient for the color `self`.
- [func mix(with: Color, by: Double, in: Gradient.ColorSpace) -> Color](color/mix(with:by:in:).md)
  Returns a version of self mixed with `rhs` by the amount specified by `fraction`.
- [func exposureAdjust(Double) -> Color](color/exposureadjust(_:).md)
  Returns a new color with an exposure adjustment applied.
- [func headroom(Double?) -> Color](color/headroom(_:).md)
  Creates a new color with specified HDR content headroom.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/color/opacity(_:))*