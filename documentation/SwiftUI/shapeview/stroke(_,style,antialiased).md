# stroke(_:style:antialiased:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

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
@export(implementation)
nonisolated func stroke<S>(_ content: S, style: StrokeStyle, antialiased: Bool = true) -> StrokeShapeView<Self.Content, S, Self> where S : ShapeStyle
```

## Return Value

A stroked shape.

## Discussion

The following example adds a dashed purple stroke to a `Capsule`:

```swift
Capsule()
.stroke(
    Color.purple,
    style: StrokeStyle(
        lineWidth: 5,
        lineCap: .round,
        lineJoin: .miter,
        miterLimit: 0,
        dash: [5, 10],
        dashPhase: 0
    )
)
```

## Parameters

- `content`: The color or gradient with which to stroke this shape.
- `style`: The stroke characteristics — such as the line’s width and whether the stroke is dashed — that determine how to render this shape.
- `antialiased`: A Boolean value that specifies whether to allow antialiasing. Pass `true` to allow antialising, otherwise `false`.

## See Also

### Modify the shape
- [func fill<S>(S, style: FillStyle) -> FillShapeView<Self.Content, S, Self>](./fill%28_,style%29.md)
  Fills this shape with a color or gradient.
- [func stroke<S>(S, lineWidth: CGFloat, antialiased: Bool) -> StrokeShapeView<Self.Content, S, Self>](./stroke%28_,linewidth,antialiased%29.md)
  Traces the outline of this shape with a color or gradient.
- [func strokeBorder<S>(S, style: StrokeStyle, antialiased: Bool) -> StrokeBorderShapeView<Self.Content, S, Self>](./strokeborder%28_,style,antialiased%29.md)
  Returns a view that’s the result of insetting this view by half of its style’s line width.
- [func strokeBorder<S>(S, lineWidth: CGFloat, antialiased: Bool) -> StrokeBorderShapeView<Self.Content, S, Self>](./strokeborder%28_,linewidth,antialiased%29.md)
  Returns a view that’s the result of filling an inner stroke of this view with the content you supply.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/shapeview/stroke(_:style:antialiased:))*