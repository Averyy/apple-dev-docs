# stroke(_:lineWidth:antialiased:)

**Framework**: SwiftUI  
**Kind**: method

Traces the outline of this shape with a color or gradient.

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
func stroke<S>(_ content: S, lineWidth: CGFloat = 1, antialiased: Bool = true) -> StrokeShapeView<Self.Content, S, Self> where S : ShapeStyle
```

#### Return Value

A stroked shape.

#### Discussion

The following example draws a circle with a purple stroke:

```swift
Circle().stroke(Color.purple, lineWidth: 5)
```

## Parameters

- `content`: The color or gradient with which to stroke this shape.
- `lineWidth`: The width of the stroke that outlines this shape.

## See Also

- [func fill<S>(S, style: FillStyle) -> FillShapeView<Self.Content, S, Self>](shapeview/fill(_:style:).md)
  Fills this shape with a color or gradient.
- [func stroke<S>(S, style: StrokeStyle, antialiased: Bool) -> StrokeShapeView<Self.Content, S, Self>](shapeview/stroke(_:style:antialiased:).md)
  Traces the outline of this shape with a color or gradient.
- [func strokeBorder<S>(S, style: StrokeStyle, antialiased: Bool) -> StrokeBorderShapeView<Self.Content, S, Self>](shapeview/strokeborder(_:style:antialiased:).md)
  Returns a view that’s the result of insetting this view by half of its style’s line width.
- [func strokeBorder<S>(S, lineWidth: CGFloat, antialiased: Bool) -> StrokeBorderShapeView<Self.Content, S, Self>](shapeview/strokeborder(_:linewidth:antialiased:).md)
  Returns a view that’s the result of filling an inner stroke of this view with the content you supply.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/shapeview/stroke(_:linewidth:antialiased:))*