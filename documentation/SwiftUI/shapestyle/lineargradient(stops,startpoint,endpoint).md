# linearGradient(stops:startPoint:endPoint:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Type Method

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
@export(implementation)
static func linearGradient(stops: [Gradient.Stop], startPoint: UnitPoint, endPoint: UnitPoint) -> LinearGradient
```

Available when `Self` is `LinearGradient`.

## Discussion

The gradient applies the color function along an axis, as defined by its start and end points. The gradient maps the unit space points into the bounding rectangle of each shape filled with the gradient.

For information about how to use shape styles, see [`ShapeStyle`](../shapestyle.md).

## See Also

### Linear gradients
- [static linearGradient(_:startPoint:endPoint:)](./lineargradient%28_,startpoint,endpoint%29.md)
  A linear gradient.
- [static func linearGradient(colors: [Color], startPoint: UnitPoint, endPoint: UnitPoint) -> LinearGradient](./lineargradient%28colors,startpoint,endpoint%29.md)
  A linear gradient defined by a collection of colors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/shapestyle/lineargradient(stops:startpoint:endpoint:))*