# linearGradient(_:startPoint:endPoint:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Type Method

A linear gradient.

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
static func linearGradient(_ gradient: Gradient, startPoint: UnitPoint, endPoint: UnitPoint) -> LinearGradient
```

Available when `Self` is `LinearGradient`.

**Other overloads**:

```swift
@export(implementation)
static func linearGradient(_ gradient: AnyGradient, startPoint: UnitPoint, endPoint: UnitPoint) -> some ShapeStyle
```

## Discussion

The gradient applies the color function along an axis, as defined by its start and end points. The gradient maps the unit space points into the bounding rectangle of each shape filled with the gradient.

For information about how to use shape styles, see [`ShapeStyle`](../shapestyle.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/shapestyle/lineargradient(_:startpoint:endpoint:)-753nc)*