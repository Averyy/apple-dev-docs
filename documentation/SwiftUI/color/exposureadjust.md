# exposureAdjust(_:)

**Framework**: SwiftUI  
**Kind**: method

Returns a new color with an exposure adjustment applied.

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
func exposureAdjust(_ stops: Double) -> Color
```

#### Return Value

A new color with the exposure adjustment applied.

#### Discussion

This function adjusts the exposure of a color by multipling its linear-light representation by `pow(2, stops)` and adjusting its HDR content headroom.

For example the system yellow color could have its brightness increased by two exposure levels:

```swift
Color.yellow.exposureAdjust(2)
```

## Parameters

- `stops`: The number of exposure levels to adjust by.

## See Also

- [func opacity(Double) -> Color](color/opacity(_:).md)
  Multiplies the opacity of the color by the given amount.
- [var gradient: AnyGradient](color/gradient.md)
  Returns the standard gradient for the color `self`.
- [func mix(with: Color, by: Double, in: Gradient.ColorSpace) -> Color](color/mix(with:by:in:).md)
  Returns a version of self mixed with `rhs` by the amount specified by `fraction`.
- [func headroom(Double?) -> Color](color/headroom(_:).md)
  Creates a new color with specified HDR content headroom.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/color/exposureadjust(_:))*