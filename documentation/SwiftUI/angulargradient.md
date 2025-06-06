# AngularGradient

**Framework**: SwiftUI  
**Kind**: struct

An angular gradient.

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
@frozen
struct AngularGradient
```

#### Overview

An angular gradient is also known as a “conic” gradient. This gradient applies the color function as the angle changes, relative to a center point and defined start and end angles. If `endAngle - startAngle > 2π`, the gradient only draws the last complete turn. If `endAngle - startAngle < 2π`, the gradient fills the missing area with the colors defined by gradient locations one and zero, transitioning between the two halfway across the missing area. The gradient maps the unit space center point into the bounding rectangle of each shape filled with the gradient.

When using an angular gradient as a shape style, you can also use [`angularGradient(_:center:startAngle:endAngle:)`](shapestyle/angulargradient(_:center:startangle:endangle:).md), [`conicGradient(_:center:angle:)`](shapestyle/conicgradient(_:center:angle:).md), or similar methods.

## Topics

### Creating a full rotation angular gradient
- [init(gradient: Gradient, center: UnitPoint, angle: Angle)](angulargradient/init(gradient:center:angle:).md)
  Creates a conic gradient that completes a full turn.
- [init(colors: [Color], center: UnitPoint, angle: Angle)](angulargradient/init(colors:center:angle:).md)
  Creates a conic gradient from a collection of colors that completes a full turn.
- [init(stops: [Gradient.Stop], center: UnitPoint, angle: Angle)](angulargradient/init(stops:center:angle:).md)
  Creates a conic gradient from a collection of color stops that completes a full turn.
### Creating a partial rotation angular gradient
- [init(gradient: Gradient, center: UnitPoint, startAngle: Angle, endAngle: Angle)](angulargradient/init(gradient:center:startangle:endangle:).md)
  Creates an angular gradient.
- [init(colors: [Color], center: UnitPoint, startAngle: Angle, endAngle: Angle)](angulargradient/init(colors:center:startangle:endangle:).md)
  Creates an angular gradient from a collection of colors.
- [init(stops: [Gradient.Stop], center: UnitPoint, startAngle: Angle, endAngle: Angle)](angulargradient/init(stops:center:startangle:endangle:).md)
  Creates an angular gradient from a collection of color stops.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [ShapeStyle](shapestyle.md)
- [View](view.md)

## See Also

- [struct EllipticalGradient](ellipticalgradient.md)
  A radial gradient that draws an ellipse.
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

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/angulargradient)*