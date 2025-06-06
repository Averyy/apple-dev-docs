# strokeBorder(_:lineWidth:antialiased:)

**Framework**: SwiftUI  
**Kind**: method

Returns a view that’s the result of filling an inner stroke of this view with the content you supply.

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
func strokeBorder<S>(_ content: S = .foreground, lineWidth: CGFloat = 1, antialiased: Bool = true) -> StrokeBorderShapeView<Self.Content, S, Self> where S : ShapeStyle
```

#### Discussion

This is equivalent to insetting `self` by `lineWidth / 2` and stroking the resulting shape with `lineWidth` as the line-width.

## See Also

- [func fill<S>(S, style: FillStyle) -> FillShapeView<Self.Content, S, Self>](shapeview/fill(_:style:).md)
  Fills this shape with a color or gradient.
- [func stroke<S>(S, style: StrokeStyle, antialiased: Bool) -> StrokeShapeView<Self.Content, S, Self>](shapeview/stroke(_:style:antialiased:).md)
  Traces the outline of this shape with a color or gradient.
- [func stroke<S>(S, lineWidth: CGFloat, antialiased: Bool) -> StrokeShapeView<Self.Content, S, Self>](shapeview/stroke(_:linewidth:antialiased:).md)
  Traces the outline of this shape with a color or gradient.
- [func strokeBorder<S>(S, style: StrokeStyle, antialiased: Bool) -> StrokeBorderShapeView<Self.Content, S, Self>](shapeview/strokeborder(_:style:antialiased:).md)
  Returns a view that’s the result of insetting this view by half of its style’s line width.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/shapeview/strokeborder(_:linewidth:antialiased:))*