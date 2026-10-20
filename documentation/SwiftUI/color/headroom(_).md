# headroom(_:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Creates a new color with specified HDR content headroom.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

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

- `headroom`: The headroom value to associate with the new color.

## See Also

### Modifying a color
- [func opacity(Double) -> Color](./opacity%28_%29.md)
  Multiplies the opacity of the color by the given amount.
- [var gradient: AnyGradient](./gradient.md)
  Returns the standard gradient for the color `self`.
- [func mix(with: Color, by: Double, in: Gradient.ColorSpace) -> Color](./mix%28with,by,in%29.md)
  Returns a version of self mixed with `rhs` by the amount specified by `fraction`.
- [func exposureAdjust(Double) -> Color](./exposureadjust%28_%29.md)
  Returns a new color with an exposure adjustment applied.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/color/headroom(_:))*