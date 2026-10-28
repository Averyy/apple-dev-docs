# ellipticalGradient(_:center:startRadiusFraction:endRadiusFraction:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Type Method

A radial gradient that draws an ellipse.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
@export(implementation)
static func ellipticalGradient(_ gradient: Gradient, center: UnitPoint = .center, startRadiusFraction: CGFloat = 0, endRadiusFraction: CGFloat = 0.5) -> EllipticalGradient
```

Available when `Self` is `EllipticalGradient`.

**Other overloads**:

```swift
@export(implementation)
static func ellipticalGradient(_ gradient: AnyGradient, center: UnitPoint = .center, startRadiusFraction: CGFloat = 0, endRadiusFraction: CGFloat = 0.5) -> some ShapeStyle
```

## Discussion

The gradient maps its coordinate space to the unit space square in which its center and radii are defined, then stretches that square to fill its bounding rect, possibly also stretching the circular gradient to have elliptical contours.

For example, an elliptical gradient used as a background:

```swift
let gradient = Gradient(colors: [.red, .yellow])

ContentView()
    .background(.ellipticalGradient(gradient))
```

For information about how to use shape styles, see [`ShapeStyle`](../shapestyle.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/shapestyle/ellipticalgradient(_:center:startradiusfraction:endradiusfraction:)-fmox)*