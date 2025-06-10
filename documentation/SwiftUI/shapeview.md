# ShapeView

**Framework**: SwiftUI  
**Kind**: protocol

A view that provides a shape that you can use for drawing operations.

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
protocol ShapeView<Content> : View, _RemoveGlobalActorIsolation
```

#### Overview

Use this type with the drawing methods on [`Shape`](shape.md) to apply multiple fills and/or strokes to a shape. For example, the following code applies a fill and stroke to a capsule shape:

```swift
Capsule()
    .fill(.yellow)
    .stroke(.blue, lineWidth: 8)
```

## Topics

### Getting the shape
- [var shape: Self.Content](shapeview/shape.md)
  The shape that this type draws and provides for other drawing operations.
- [associatedtype Content : Shape](shapeview/content.md)
  The type of shape this can provide.
### Modify the shape
- [func fill<S>(S, style: FillStyle) -> FillShapeView<Self.Content, S, Self>](shapeview/fill(_:style:).md)
  Fills this shape with a color or gradient.
- [func stroke<S>(S, style: StrokeStyle, antialiased: Bool) -> StrokeShapeView<Self.Content, S, Self>](shapeview/stroke(_:style:antialiased:).md)
  Traces the outline of this shape with a color or gradient.
- [func stroke<S>(S, lineWidth: CGFloat, antialiased: Bool) -> StrokeShapeView<Self.Content, S, Self>](shapeview/stroke(_:linewidth:antialiased:).md)
  Traces the outline of this shape with a color or gradient.
- [func strokeBorder<S>(S, style: StrokeStyle, antialiased: Bool) -> StrokeBorderShapeView<Self.Content, S, Self>](shapeview/strokeborder(_:style:antialiased:).md)
  Returns a view that’s the result of insetting this view by half of its style’s line width.
- [func strokeBorder<S>(S, lineWidth: CGFloat, antialiased: Bool) -> StrokeBorderShapeView<Self.Content, S, Self>](shapeview/strokeborder(_:linewidth:antialiased:).md)
  Returns a view that’s the result of filling an inner stroke of this view with the content you supply.

## Relationships

### Inherits From
- [View](view.md)
### Conforming Types
- [FillShapeView](fillshapeview.md)
- [StrokeBorderShapeView](strokebordershapeview.md)
- [StrokeShapeView](strokeshapeview.md)

## See Also

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
- [struct FillShapeView](fillshapeview.md)
  A shape provider that fills its shape.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/shapeview)*