# radialGradient(_:center:startRadius:endRadius:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Type Method

A radial gradient.

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
@export(implementation)
static func radialGradient(_ gradient: AnyGradient, center: UnitPoint = .center, startRadius: CGFloat = 0, endRadius: CGFloat) -> some ShapeStyle
```

Available when `Self` is `RadialGradient`.

**Other overloads**:

```swift
@export(implementation)
static func radialGradient(_ gradient: Gradient, center: UnitPoint, startRadius: CGFloat, endRadius: CGFloat) -> RadialGradient
```

#### Discussion

The gradient applies the color function as the distance from a center point, scaled to fit within the defined start and end radii. The gradient maps the unit space center point into the bounding rectangle of each shape filled with the gradient.

For example, a radial gradient used as a background:

```swift
ContentView()
    .background(.radialGradient(.red.gradient, endRadius: 100))
```

For information about how to use shape styles, see [`ShapeStyle`](../shapestyle.md).

## See Also

### Radial gradients
- [static func radialGradient(colors: [Color], center: UnitPoint, startRadius: CGFloat, endRadius: CGFloat) -> RadialGradient](./radialgradient%28colors,center,startradius,endradius%29.md)
  A radial gradient defined by a collection of colors.
- [static func radialGradient(stops: [Gradient.Stop], center: UnitPoint, startRadius: CGFloat, endRadius: CGFloat) -> RadialGradient](./radialgradient%28stops,center,startradius,endradius%29.md)
  A radial gradient defined by a collection of color stops.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/shapestyle/radialgradient(_:center:startradius:endradius:))*