# StrokeStyle

**Framework**: SwiftUI  
**Kind**: struct

The characteristics of a stroke that traces a path.

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
struct StrokeStyle
```

## Topics

### Creating a stroke style
- [init(lineWidth: CGFloat, lineCap: CGLineCap, lineJoin: CGLineJoin, miterLimit: CGFloat, dash: [CGFloat], dashPhase: CGFloat)](strokestyle/init(linewidth:linecap:linejoin:miterlimit:dash:dashphase:).md)
  Creates a new stroke style from the given components.
### Setting stroke style properties
- [var lineWidth: CGFloat](strokestyle/linewidth.md)
  The width of the stroked path.
- [var lineCap: CGLineCap](strokestyle/linecap.md)
  The endpoint style of a line.
- [var lineJoin: CGLineJoin](strokestyle/linejoin.md)
  The join type of a line.
- [var miterLimit: CGFloat](strokestyle/miterlimit.md)
  A threshold used to determine whether to use a bevel instead of a miter at a join.
- [var dash: [CGFloat]](strokestyle/dash.md)
  The lengths of painted and unpainted segments used to make a dashed line.
- [var dashPhase: CGFloat](strokestyle/dashphase.md)
  How far into the dash pattern the line starts.

## Relationships

### Conforms To
- [Animatable](animatable.md)
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [protocol ShapeView](shapeview.md)
  A view that provides a shape that you can use for drawing operations.
- [protocol Shape](shape.md)
  A 2D shape that you can use when drawing a view.
- [struct AnyShape](anyshape.md)
  A type-erased shape value.
- [enum ShapeRole](shaperole.md)
  Ways of styling a shape.
- [struct StrokeShapeView](strokeshapeview.md)
  A shape provider that strokes its shape.
- [struct StrokeBorderShapeView](strokebordershapeview.md)
  A shape provider that strokes the border of its shape.
- [struct FillStyle](fillstyle.md)
  A style for rasterizing vector shapes.
- [struct FillShapeView](fillshapeview.md)
  A shape provider that fills its shape.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/strokestyle)*