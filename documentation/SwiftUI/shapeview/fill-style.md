# fill(_:style:)

**Framework**: SwiftUI  
**Kind**: method

Fills this shape with a color or gradient.

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
nonisolated
func fill<S>(_ content: S = .foreground, style: FillStyle = FillStyle()) -> FillShapeView<Self.Content, S, Self> where S : ShapeStyle
```

#### Return Value

A shape filled with the color or gradient you supply.

## Parameters

- `content`: The color or gradient to use when filling this shape.
- `style`: The style options that determine how the fill renders.

## See Also

- [func stroke<S>(S, style: StrokeStyle, antialiased: Bool) -> StrokeShapeView<Self.Content, S, Self>](shapeview/stroke(_:style:antialiased:).md)
  Traces the outline of this shape with a color or gradient.
- [func stroke<S>(S, lineWidth: CGFloat, antialiased: Bool) -> StrokeShapeView<Self.Content, S, Self>](shapeview/stroke(_:linewidth:antialiased:).md)
  Traces the outline of this shape with a color or gradient.
- [func strokeBorder<S>(S, style: StrokeStyle, antialiased: Bool) -> StrokeBorderShapeView<Self.Content, S, Self>](shapeview/strokeborder(_:style:antialiased:).md)
  Returns a view that’s the result of insetting this view by half of its style’s line width.
- [func strokeBorder<S>(S, lineWidth: CGFloat, antialiased: Bool) -> StrokeBorderShapeView<Self.Content, S, Self>](shapeview/strokeborder(_:linewidth:antialiased:).md)
  Returns a view that’s the result of filling an inner stroke of this view with the content you supply.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/shapeview/fill(_:style:))*