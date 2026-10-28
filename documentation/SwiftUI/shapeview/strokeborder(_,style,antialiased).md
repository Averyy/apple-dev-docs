# strokeBorder(_:style:antialiased:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Returns a view that’s the result of insetting this view by half of its style’s line width.

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
@export(implementation)
nonisolated func strokeBorder<S>(_ content: S = .foreground, style: StrokeStyle, antialiased: Bool = true) -> StrokeBorderShapeView<Self.Content, S, Self> where S : ShapeStyle
```

Available when `Content` conforms to `InsettableShape`.

## Discussion

This method strokes the resulting shape with `style` and fills it with `content`.

## See Also

### Modify the shape
- [func fill<S>(S, style: FillStyle) -> FillShapeView<Self.Content, S, Self>](./fill%28_,style%29.md)
  Fills this shape with a color or gradient.
- [func stroke<S>(S, style: StrokeStyle, antialiased: Bool) -> StrokeShapeView<Self.Content, S, Self>](./stroke%28_,style,antialiased%29.md)
  Traces the outline of this shape with a color or gradient.
- [func stroke<S>(S, lineWidth: CGFloat, antialiased: Bool) -> StrokeShapeView<Self.Content, S, Self>](./stroke%28_,linewidth,antialiased%29.md)
  Traces the outline of this shape with a color or gradient.
- [func strokeBorder<S>(S, lineWidth: CGFloat, antialiased: Bool) -> StrokeBorderShapeView<Self.Content, S, Self>](./strokeborder%28_,linewidth,antialiased%29.md)
  Returns a view that’s the result of filling an inner stroke of this view with the content you supply.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/shapeview/strokeborder(_:style:antialiased:))*