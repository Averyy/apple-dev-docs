# gradient

**Framework**: SwiftUI  
**Kind**: property

Returns the standard gradient for the color `self`.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
var gradient: AnyGradient { get }
```

#### Discussion

For example, filling a rectangle with a gradient derived from the standard blue color:

```swift
Rectangle().fill(.blue.gradient)
```

## See Also

- [func opacity(Double) -> Color](color/opacity(_:).md)
  Multiplies the opacity of the color by the given amount.
- [func mix(with: Color, by: Double, in: Gradient.ColorSpace) -> Color](color/mix(with:by:in:).md)
  Returns a version of self mixed with `rhs` by the amount specified by `fraction`.
- [func exposureAdjust(Double) -> Color](color/exposureadjust(_:).md)
  Returns a new color with an exposure adjustment applied.
- [func headroom(Double?) -> Color](color/headroom(_:).md)
  Creates a new color with specified HDR content headroom.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/color/gradient)*