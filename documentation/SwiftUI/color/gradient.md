# gradient

**Framework**: SwiftUI  
**Kind**: property  
**Role**: Instance Property

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

### Modifying a color
- [func opacity(Double) -> Color](./opacity%28_%29.md)
  Multiplies the opacity of the color by the given amount.
- [func mix(with: Color, by: Double, in: Gradient.ColorSpace) -> Color](./mix%28with,by,in%29.md)
  Returns a version of self mixed with `rhs` by the amount specified by `fraction`.
- [func exposureAdjust(Double) -> Color](./exposureadjust%28_%29.md)
  Returns a new color with an exposure adjustment applied.
- [func headroom(Double?) -> Color](./headroom%28_%29.md)
  Creates a new color with specified HDR content headroom.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/color/gradient)*