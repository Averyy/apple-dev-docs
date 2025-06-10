# LinearGradient

**Framework**: SwiftUI  
**Kind**: struct

A linear gradient.

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
struct LinearGradient
```

## Mentions

- [Laying out a simple view](laying-out-a-simple-view.md)

#### Overview

The gradient applies the color function along an axis, as defined by its start and end points. The gradient maps the unit space points into the bounding rectangle of each shape filled with the gradient.

When using a linear gradient as a shape style, you can also use [`linearGradient(_:startPoint:endPoint:)`](shapestyle/lineargradient(_:startpoint:endpoint:).md).

## Topics

### Creating a linear gradient
- [init(gradient: Gradient, startPoint: UnitPoint, endPoint: UnitPoint)](lineargradient/init(gradient:startpoint:endpoint:).md)
  Creates a linear gradient from a base gradient.
- [init(colors: [Color], startPoint: UnitPoint, endPoint: UnitPoint)](lineargradient/init(colors:startpoint:endpoint:).md)
  Creates a linear gradient from a collection of colors.
- [init(stops: [Gradient.Stop], startPoint: UnitPoint, endPoint: UnitPoint)](lineargradient/init(stops:startpoint:endpoint:).md)
  Creates a linear gradient from a collection of color stops.

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

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/lineargradient)*