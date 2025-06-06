# radialGradient(colors:center:startRadius:endRadius:)

**Framework**: SwiftUI  
**Kind**: method

A radial gradient defined by a collection of colors.

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
static func radialGradient(colors: [Color], center: UnitPoint, startRadius: CGFloat, endRadius: CGFloat) -> RadialGradient
```

#### Discussion

The gradient applies the color function as the distance from a center point, scaled to fit within the defined start and end radii. The gradient maps the unit space center point into the bounding rectangle of each shape filled with the gradient.

For information about how to use shape styles, see [`ShapeStyle`](shapestyle.md).

## See Also

- [static radialGradient(_:center:startRadius:endRadius:)](shapestyle/radialgradient(_:center:startradius:endradius:).md)
  A radial gradient.
- [static func radialGradient(stops: [Gradient.Stop], center: UnitPoint, startRadius: CGFloat, endRadius: CGFloat) -> RadialGradient](shapestyle/radialgradient(stops:center:startradius:endradius:).md)
  A radial gradient defined by a collection of color stops.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/shapestyle/radialgradient(colors:center:startradius:endradius:))*