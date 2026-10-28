# exposureAdjust(_:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Returns a new color with an exposure adjustment applied.

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
@export(implementation)
func exposureAdjust(_ stops: Double) -> Color
```

## Return Value

A new color with the exposure adjustment applied.

## Discussion

This function adjusts the exposure of a color by multipling its linear-light representation by `pow(2, stops)` and adjusting its HDR content headroom.

For example the system yellow color could have its brightness increased by two exposure levels:

```swift
Color.yellow.exposureAdjust(2)
```

## Parameters

- `stops`: The number of exposure levels to adjust by.

## See Also

### Modifying a color
- [func opacity(Double) -> Color](./opacity%28_%29.md)
  Multiplies the opacity of the color by the given amount.
- [var gradient: AnyGradient](./gradient.md)
  Returns the standard gradient for the color `self`.
- [func mix(with: Color, by: Double, in: Gradient.ColorSpace) -> Color](./mix%28with,by,in%29.md)
  Returns a version of self mixed with `rhs` by the amount specified by `fraction`.
- [func headroom(Double?) -> Color](./headroom%28_%29.md)
  Creates a new color with specified HDR content headroom.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/color/exposureadjust(_:))*