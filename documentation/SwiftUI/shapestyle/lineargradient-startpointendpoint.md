# linearGradient(_:startPoint:endPoint:)

**Framework**: SwiftUI  
**Kind**: method

A linear gradient.

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
static func linearGradient(_ gradient: AnyGradient, startPoint: UnitPoint, endPoint: UnitPoint) -> some ShapeStyle
```

#### Discussion

The gradient applies the color function along an axis, as defined by its start and end points. The gradient maps the unit space points into the bounding rectangle of each shape filled with the gradient.

For example, a linear gradient used as a background:

```swift
ContentView()
    .background(.linearGradient(.red.gradient,
        startPoint: .top, endPoint: .bottom))
```

For information about how to use shape styles, see [`ShapeStyle`](shapestyle.md).

## See Also

- [static func linearGradient(colors: [Color], startPoint: UnitPoint, endPoint: UnitPoint) -> LinearGradient](shapestyle/lineargradient(colors:startpoint:endpoint:).md)
  A linear gradient defined by a collection of colors.
- [static func linearGradient(stops: [Gradient.Stop], startPoint: UnitPoint, endPoint: UnitPoint) -> LinearGradient](shapestyle/lineargradient(stops:startpoint:endpoint:).md)
  A linear gradient defined by a collection of color stops.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/shapestyle/lineargradient(_:startpoint:endpoint:))*