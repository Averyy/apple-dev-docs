# linearGradient(stops:startPoint:endPoint:)

**Framework**: SwiftUI  
**Kind**: method

A linear gradient defined by a collection of color stops.

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
static func linearGradient(stops: [Gradient.Stop], startPoint: UnitPoint, endPoint: UnitPoint) -> LinearGradient
```

#### Discussion

The gradient applies the color function along an axis, as defined by its start and end points. The gradient maps the unit space points into the bounding rectangle of each shape filled with the gradient.

For information about how to use shape styles, see [`ShapeStyle`](shapestyle.md).

## See Also

- [static linearGradient(_:startPoint:endPoint:)](shapestyle/lineargradient(_:startpoint:endpoint:).md)
  A linear gradient.
- [static func linearGradient(colors: [Color], startPoint: UnitPoint, endPoint: UnitPoint) -> LinearGradient](shapestyle/lineargradient(colors:startpoint:endpoint:).md)
  A linear gradient defined by a collection of colors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/shapestyle/lineargradient(stops:startpoint:endpoint:))*