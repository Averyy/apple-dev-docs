# conicGradient(_:center:angle:)

**Framework**: SwiftUI  
**Kind**: method

A conic gradient that completes a full turn, optionally starting from a given angle and anchored to a relative center point within the filled shape.

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
static func conicGradient(_ gradient: AnyGradient, center: UnitPoint = .center, angle: Angle = .zero) -> some ShapeStyle
```

#### Discussion

For example, a conic gradient used as a background:

```swift
let gradient = Gradient(colors: [.red, .yellow])

ContentView()
    .background(.conicGradient(gradient))
```

For information about how to use shape styles, see [`ShapeStyle`](shapestyle.md).

## Parameters

- `gradient`: The gradient to use for filling the shape, providing the   colors and their relative stop locations.
- `center`: The relative center of the gradient, mapped from the unit   space into the bounding rectangle of the filled shape.
- `angle`: The angle to offset the beginning of the gradient’s full   turn.

## See Also

- [static func conicGradient(colors: [Color], center: UnitPoint, angle: Angle) -> AngularGradient](shapestyle/conicgradient(colors:center:angle:).md)
  A conic gradient defined by a collection of colors that completes a full turn.
- [static func conicGradient(stops: [Gradient.Stop], center: UnitPoint, angle: Angle) -> AngularGradient](shapestyle/conicgradient(stops:center:angle:).md)
  A conic gradient defined by a collection of color stops that completes a full turn.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/shapestyle/conicgradient(_:center:angle:))*