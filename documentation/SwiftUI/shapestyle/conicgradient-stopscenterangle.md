# conicGradient(stops:center:angle:)

**Framework**: SwiftUI  
**Kind**: method

A conic gradient defined by a collection of color stops that completes a full turn.

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
static func conicGradient(stops: [Gradient.Stop], center: UnitPoint, angle: Angle = .zero) -> AngularGradient
```

#### Discussion

For more information on how to use conic gradients, see [`conicGradient(_:center:angle:)`](shapestyle/conicgradient(_:center:angle:).md).

## Parameters

- `stops`: The color stops of the gradient, defining each component   color and their relative location along the gradient’s full length.
- `center`: The relative center of the gradient, mapped from the unit   space into the bounding rectangle of the filled shape.
- `angle`: The angle to offset the beginning of the gradient’s full   turn.

## See Also

- [static conicGradient(_:center:angle:)](shapestyle/conicgradient(_:center:angle:).md)
  A conic gradient that completes a full turn, optionally starting from a given angle and anchored to a relative center point within the filled shape.
- [static func conicGradient(colors: [Color], center: UnitPoint, angle: Angle) -> AngularGradient](shapestyle/conicgradient(colors:center:angle:).md)
  A conic gradient defined by a collection of colors that completes a full turn.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/shapestyle/conicgradient(stops:center:angle:))*