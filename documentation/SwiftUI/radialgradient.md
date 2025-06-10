# RadialGradient

**Framework**: SwiftUI  
**Kind**: struct

A radial gradient.

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
struct RadialGradient
```

#### Overview

The gradient applies the color function as the distance from a center point, scaled to fit within the defined start and end radii. The gradient maps the unit space center point into the bounding rectangle of each shape filled with the gradient.

When using a radial gradient as a shape style, you can also use [`radialGradient(_:center:startRadius:endRadius:)`](shapestyle/radialgradient(_:center:startradius:endradius:).md).

## Topics

### Creating a radial gradient
- [init(gradient: Gradient, center: UnitPoint, startRadius: CGFloat, endRadius: CGFloat)](radialgradient/init(gradient:center:startradius:endradius:).md)
  Creates a radial gradient from a base gradient.
- [init(colors: [Color], center: UnitPoint, startRadius: CGFloat, endRadius: CGFloat)](radialgradient/init(colors:center:startradius:endradius:).md)
  Creates a radial gradient from a collection of colors.
- [init(stops: [Gradient.Stop], center: UnitPoint, startRadius: CGFloat, endRadius: CGFloat)](radialgradient/init(stops:center:startradius:endradius:).md)
  Creates a radial gradient from a collection of color stops.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [ShapeStyle](shapestyle.md)
- [View](view.md)

## See Also

- [struct AngularGradient](angulargradient.md)
  An angular gradient.
- [struct EllipticalGradient](ellipticalgradient.md)
  A radial gradient that draws an ellipse.
- [struct LinearGradient](lineargradient.md)
  A linear gradient.
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

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/radialgradient)*