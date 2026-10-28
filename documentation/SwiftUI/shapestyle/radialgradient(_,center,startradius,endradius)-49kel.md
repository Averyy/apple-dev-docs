# radialGradient(_:center:startRadius:endRadius:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Type Method

A radial gradient.

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
static func radialGradient(_ gradient: Gradient, center: UnitPoint, startRadius: CGFloat, endRadius: CGFloat) -> RadialGradient
```

Available when `Self` is `RadialGradient`.

**Other overloads**:

```swift
@export(implementation)
static func radialGradient(_ gradient: AnyGradient, center: UnitPoint = .center, startRadius: CGFloat = 0, endRadius: CGFloat) -> some ShapeStyle
```

## Discussion

The gradient applies the color function as the distance from a center point, scaled to fit within the defined start and end radii. The gradient maps the unit space center point into the bounding rectangle of each shape filled with the gradient.

For information about how to use shape styles, see [`ShapeStyle`](../shapestyle.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/shapestyle/radialgradient(_:center:startradius:endradius:)-49kel)*