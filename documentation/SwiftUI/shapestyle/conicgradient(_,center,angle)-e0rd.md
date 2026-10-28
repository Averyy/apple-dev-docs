# conicGradient(_:center:angle:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Type Method

A conic gradient that completes a full turn, optionally starting from a given angle and anchored to a relative center point within the filled shape.

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
static func conicGradient(_ gradient: Gradient, center: UnitPoint, angle: Angle = .zero) -> AngularGradient
```

Available when `Self` is `AngularGradient`.

**Other overloads**:

```swift
@export(implementation)
static func conicGradient(_ gradient: AnyGradient, center: UnitPoint = .center, angle: Angle = .zero) -> some ShapeStyle
```

## Discussion

For example, a conic gradient used as a background:

```swift
let gradient = Gradient(colors: [.red, .yellow])

ContentView()
    .background(.conicGradient(gradient))
```

For information about how to use shape styles, see [`ShapeStyle`](../shapestyle.md).

## Parameters

- `gradient`: The gradient to use for filling the shape, providing the colors and their relative stop locations.
- `center`: The relative center of the gradient, mapped from the unit space into the bounding rectangle of the filled shape.
- `angle`: The angle to offset the beginning of the gradient’s full turn.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/shapestyle/conicgradient(_:center:angle:)-e0rd)*