# StrokeBorderShapeView

**Framework**: SwiftUI  
**Kind**: struct

A shape provider that strokes the border of its shape.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
@frozen
struct StrokeBorderShapeView<Content, Style, Background> where Content : InsettableShape, Style : ShapeStyle, Background : View
```

#### Overview

You don’t create this type directly; it’s the return type of `Shape.strokeBorder`.

## Topics

### Creating a stroke border shape view
- [init(shape: Content, style: Style, strokeStyle: StrokeStyle, isAntialiased: Bool, background: Background)](strokebordershapeview/init(shape:style:strokestyle:isantialiased:background:).md)
  Create a stroke border shape.
### Getting shape view properties
- [var background: Background](strokebordershapeview/background.md)
  The background shown beneath this view.
- [var isAntialiased: Bool](strokebordershapeview/isantialiased.md)
  Whether this shape should be drawn antialiased.
- [var shape: Content](strokebordershapeview/shape.md)
  The shape that this type draws and provides for other drawing operations.
- [var strokeStyle: StrokeStyle](strokebordershapeview/strokestyle.md)
  The stroke style used when stroking this view’s shape.
- [var style: Style](strokebordershapeview/style.md)
  The style that strokes the border of this view’s shape.

## Relationships

### Conforms To
- [ShapeView](shapeview.md)
- [View](view.md)

## See Also

- [protocol ShapeView](shapeview.md)
  A view that provides a shape that you can use for drawing operations.
- [protocol Shape](shape.md)
  A 2D shape that you can use when drawing a view.
- [struct AnyShape](anyshape.md)
  A type-erased shape value.
- [enum ShapeRole](shaperole.md)
  Ways of styling a shape.
- [struct StrokeStyle](strokestyle.md)
  The characteristics of a stroke that traces a path.
- [struct StrokeShapeView](strokeshapeview.md)
  A shape provider that strokes its shape.
- [struct FillStyle](fillstyle.md)
  A style for rasterizing vector shapes.
- [struct FillShapeView](fillshapeview.md)
  A shape provider that fills its shape.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/strokebordershapeview)*