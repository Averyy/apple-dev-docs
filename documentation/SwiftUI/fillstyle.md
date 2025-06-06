# FillStyle

**Framework**: SwiftUI  
**Kind**: struct

A style for rasterizing vector shapes.

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
struct FillStyle
```

## Topics

### Creating a fill style
- [init(eoFill: Bool, antialiased: Bool)](fillstyle/init(eofill:antialiased:).md)
  Creates a new fill style with the specified settings.
### Setting fill style properties
- [var isEOFilled: Bool](fillstyle/iseofilled.md)
  A Boolean value that indicates whether to use the even-odd rule when rendering a shape.
- [var isAntialiased: Bool](fillstyle/isantialiased.md)
  A Boolean value that indicates whether to apply antialiasing to the edges of a shape.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Sendable](../Swift/Sendable.md)

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
- [struct FillShapeView](fillshapeview.md)
  A shape provider that fills its shape.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/fillstyle)*