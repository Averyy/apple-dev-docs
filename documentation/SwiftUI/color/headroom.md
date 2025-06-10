# headroom(_:)

**Framework**: SwiftUI  
**Kind**: method

Creates a new color with specified HDR content headroom.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

## Declaration

```swift
func headroom(_ headroom: Double?) -> Color
```

#### Return Value

A new color with the specified content headroom.

#### Discussion

High Dynamic Range colors (those with RGB components outside the standard [0, 1] range) should be annotated with their headroom to ensure that they are displayed correctly. Knowing content headroom allows the rendering system to automatically increase display headroom when the color is displayed and to tone map the color when the available display headroom is insufficient to render the color as intended.

For example a custom yellow color whose brightness has been increased by two exposure levels:

```swift
Color(.sRGB, red: 1.83, green: 1.47, blue: 0)
    .headroom(4)
```

note that headroom is a linear quantity, and as such any color adjustments should typically be made in a linear color space.

## Parameters

- `headroom`: The headroom value to associate with the   new color.

## See Also

- [func opacity(Double) -> Color](color/opacity(_:).md)
  Multiplies the opacity of the color by the given amount.
- [var gradient: AnyGradient](color/gradient.md)
  Returns the standard gradient for the color `self`.
- [func mix(with: Color, by: Double, in: Gradient.ColorSpace) -> Color](color/mix(with:by:in:).md)
  Returns a version of self mixed with `rhs` by the amount specified by `fraction`.
- [func exposureAdjust(Double) -> Color](color/exposureadjust(_:).md)
  Returns a new color with an exposure adjustment applied.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/color/headroom(_:))*