# ImagePaint

**Framework**: SwiftUI  
**Kind**: struct

A shape style that fills a shape by repeating a region of an image.

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
struct ImagePaint
```

#### Overview

You can also use [`image(_:sourceRect:scale:)`](shapestyle/image(_:sourcerect:scale:).md) to construct this style.

## Topics

### Creating an image paint style
- [init(image: Image, sourceRect: CGRect, scale: CGFloat)](imagepaint/init(image:sourcerect:scale:).md)
  Creates a shape-filling shape style.
### Configuring the image paint style
- [var image: Image](imagepaint/image.md)
  The image to be drawn.
- [var scale: CGFloat](imagepaint/scale.md)
  A scale factor applied to the image while being drawn.
- [var sourceRect: CGRect](imagepaint/sourcerect.md)
  A unit-space rectangle defining how much of the source image to draw.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [ShapeStyle](shapestyle.md)

## See Also

- [struct AngularGradient](angulargradient.md)
  An angular gradient.
- [struct EllipticalGradient](ellipticalgradient.md)
  A radial gradient that draws an ellipse.
- [struct LinearGradient](lineargradient.md)
  A linear gradient.
- [struct RadialGradient](radialgradient.md)
  A radial gradient.
- [struct Material](material.md)
  A background material type.
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

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/imagepaint)*