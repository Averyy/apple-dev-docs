# ellipticalGradient(_:center:startRadiusFraction:endRadiusFraction:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Type Method

A radial gradient that draws an ellipse.

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
static func ellipticalGradient(_ gradient: AnyGradient, center: UnitPoint = .center, startRadiusFraction: CGFloat = 0, endRadiusFraction: CGFloat = 0.5) -> some ShapeStyle
```

Available when `Self` is `EllipticalGradient`.

**Other overloads**:

```swift
@export(implementation)
static func ellipticalGradient(_ gradient: Gradient, center: UnitPoint = .center, startRadiusFraction: CGFloat = 0, endRadiusFraction: CGFloat = 0.5) -> EllipticalGradient
```

#### Discussion

The gradient maps its coordinate space to the unit space square in which its center and radii are defined, then stretches that square to fill its bounding rect, possibly also stretching the circular gradient to have elliptical contours.

For example, an elliptical gradient used as a background:

```swift
ContentView()
    .background(.ellipticalGradient(.red.gradient))
```

For information about how to use shape styles, see [`ShapeStyle`](../shapestyle.md).

## See Also

### Elliptical gradients
- [static func ellipticalGradient(colors: [Color], center: UnitPoint, startRadiusFraction: CGFloat, endRadiusFraction: CGFloat) -> EllipticalGradient](./ellipticalgradient%28colors,center,startradiusfraction,endradiusfraction%29.md)
  A radial gradient that draws an ellipse defined by a collection of colors.
- [static func ellipticalGradient(stops: [Gradient.Stop], center: UnitPoint, startRadiusFraction: CGFloat, endRadiusFraction: CGFloat) -> EllipticalGradient](./ellipticalgradient%28stops,center,startradiusfraction,endradiusfraction%29.md)
  A radial gradient that draws an ellipse defined by a collection of color stops.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/shapestyle/ellipticalgradient(_:center:startradiusfraction:endradiusfraction:))*