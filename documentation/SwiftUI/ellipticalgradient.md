# EllipticalGradient

**Framework**: SwiftUI  
**Kind**: struct

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
@frozen
struct EllipticalGradient
```

#### Overview

The gradient maps its coordinate space to the unit space square in which its center and radii are defined, then stretches that square to fill its bounding rect, possibly also stretching the circular gradient to have elliptical contours.

For example, an elliptical gradient centered on the view, filling its bounds:

```swift
EllipticalGradient(gradient: .init(colors: [.red, .yellow]))
```

When using an elliptical gradient as a shape style, you can also use [`ellipticalGradient(_:center:startRadiusFraction:endRadiusFraction:)`](shapestyle/ellipticalgradient(_:center:startradiusfraction:endradiusfraction:).md).

## Topics

### Creating an elliptical gradient
- [init(gradient: Gradient, center: UnitPoint, startRadiusFraction: CGFloat, endRadiusFraction: CGFloat)](ellipticalgradient/init(gradient:center:startradiusfraction:endradiusfraction:).md)
  Creates an elliptical gradient.
- [init(colors: [Color], center: UnitPoint, startRadiusFraction: CGFloat, endRadiusFraction: CGFloat)](ellipticalgradient/init(colors:center:startradiusfraction:endradiusfraction:).md)
  Creates an elliptical gradient from a collection of colors.
- [init(stops: [Gradient.Stop], center: UnitPoint, startRadiusFraction: CGFloat, endRadiusFraction: CGFloat)](ellipticalgradient/init(stops:center:startradiusfraction:endradiusfraction:).md)
  Creates an elliptical gradient from a collection of color stops.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [ShapeStyle](shapestyle.md)
- [View](view.md)

## See Also

- [struct AngularGradient](angulargradient.md)
  An angular gradient.
- [struct LinearGradient](lineargradient.md)
  A linear gradient.
- [struct RadialGradient](radialgradient.md)
  A radial gradient.
- [struct Material](material.md)
  A background material type.
- [struct ImagePaint](imagepaint.md)
  A shape style that fills a shape by repeating a region of an image.
- [struct HierarchicalShapeStyle](hierarchicalshapestyle.md)
  A shape style that maps to one of the numbered content styles.
- [struct HierarchicalShapeStyleModifier](hierarchicalshapestylemodifier.md)
  Styles that you can apply to hierarchical shapes.
- [struct ForegroundStyle](foregroundstyle.md)
  The foreground style in the current context.
- [struct BackgroundStyle](backgroundstyle.md)
  The background style in the current context.
- [struct SelectionShapeStyle](selectionshapestyle.md)
  A style used to visually indicate selection following platform conventional colors and behaviors.
- [struct SeparatorShapeStyle](separatorshapestyle.md)
  A style appropriate for foreground separator or border lines.
- [struct TintShapeStyle](tintshapestyle.md)
  A style that reflects the current tint color.
- [struct FillShapeStyle](fillshapestyle.md)
  A shape style that displays one of the overlay fills.
- [struct LinkShapeStyle](linkshapestyle.md)
  A style appropriate for links.
- [struct PlaceholderTextShapeStyle](placeholdertextshapestyle.md)
  A style appropriate for placeholder text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/ellipticalgradient)*