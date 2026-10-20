# angularGradient(colors:center:startAngle:endAngle:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Type Method

An angular gradient defined by a collection of colors.

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
static func angularGradient(colors: [Color], center: UnitPoint, startAngle: Angle, endAngle: Angle) -> AngularGradient
```

Available when `Self` is `AngularGradient`.

#### Discussion

For more information on how to use angular gradients, see [`angularGradient(_:center:startAngle:endAngle:)`](./angulargradient%28_,center,startangle,endangle%29.md).

## Parameters

- `colors`: The colors of the gradient, evenly spaced along its full length.
- `center`: The relative center of the gradient, mapped from the unit space into the bounding rectangle of the filled shape.
- `startAngle`: The angle that marks the beginning of the gradient.
- `endAngle`: The angle that marks the end of the gradient.

## See Also

### Angular gradients
- [static angularGradient(_:center:startAngle:endAngle:)](./angulargradient%28_,center,startangle,endangle%29.md)
  An angular gradient, which applies the color function as the angle changes between the start and end angles, and anchored to a relative center point within the filled shape.
- [static func angularGradient(stops: [Gradient.Stop], center: UnitPoint, startAngle: Angle, endAngle: Angle) -> AngularGradient](./angulargradient%28stops,center,startangle,endangle%29.md)
  An angular gradient defined by a collection of color stops.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/shapestyle/angulargradient(colors:center:startangle:endangle:))*