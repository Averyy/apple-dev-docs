# FillShapeView

**Framework**: SwiftUI  
**Kind**: struct

A shape provider that fills its shape.

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
struct FillShapeView<Content, Style, Background> where Content : Shape, Style : ShapeStyle, Background : View
```

#### Overview

You do not create this type directly, it is the return type of `Shape.fill`.

## Topics

### Creating a stroke shape view
- [init(shape: Content, style: Style, fillStyle: FillStyle, background: Background)](fillshapeview/init(shape:style:fillstyle:background:).md)
  Create a FillShapeView.
### Getting shape view properties
- [var background: Background](fillshapeview/background.md)
  The background shown beneath this view.
- [var fillStyle: FillStyle](fillshapeview/fillstyle.md)
  The fill style used when filling this view’s shape.
- [var shape: Content](fillshapeview/shape.md)
  The shape that this type draws and provides for other drawing operations.
- [var style: Style](fillshapeview/style.md)
  The style that fills this view’s shape.

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
- [struct StrokeBorderShapeView](strokebordershapeview.md)
  A shape provider that strokes the border of its shape.
- [struct FillStyle](fillstyle.md)
  A style for rasterizing vector shapes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/fillshapeview)*