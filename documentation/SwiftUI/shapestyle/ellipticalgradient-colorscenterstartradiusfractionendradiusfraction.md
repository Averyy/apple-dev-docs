# ellipticalGradient(colors:center:startRadiusFraction:endRadiusFraction:)

**Framework**: SwiftUI  
**Kind**: method

A radial gradient that draws an ellipse defined by a collection of colors.

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
static func ellipticalGradient(colors: [Color], center: UnitPoint = .center, startRadiusFraction: CGFloat = 0, endRadiusFraction: CGFloat = 0.5) -> EllipticalGradient
```

#### Discussion

The gradient maps its coordinate space to the unit space square in which its center and radii are defined, then stretches that square to fill its bounding rect, possibly also stretching the circular gradient to have elliptical contours.

For example, an elliptical gradient used as a background:

```swift
.background(.elliptical(colors: [.red, .yellow]))
```

For information about how to use shape styles, see [`ShapeStyle`](shapestyle.md).

## See Also

- [static ellipticalGradient(_:center:startRadiusFraction:endRadiusFraction:)](shapestyle/ellipticalgradient(_:center:startradiusfraction:endradiusfraction:).md)
  A radial gradient that draws an ellipse.
- [static func ellipticalGradient(stops: [Gradient.Stop], center: UnitPoint, startRadiusFraction: CGFloat, endRadiusFraction: CGFloat) -> EllipticalGradient](shapestyle/ellipticalgradient(stops:center:startradiusfraction:endradiusfraction:).md)
  A radial gradient that draws an ellipse defined by a collection of color stops.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/shapestyle/ellipticalgradient(colors:center:startradiusfraction:endradiusfraction:))*