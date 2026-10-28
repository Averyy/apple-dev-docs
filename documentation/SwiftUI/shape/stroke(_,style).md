# stroke(_:style:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Traces the outline of this shape with a color or gradient.

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
nonisolated
func stroke<S>(_ content: S, style: StrokeStyle) -> some View where S : ShapeStyle
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

## See Also

### Setting the stroke characteristics
- [func stroke<S>(S, lineWidth: CGFloat) -> some View](./stroke%28_,linewidth%29.md)
  Traces the outline of this shape with a color or gradient.
- [func stroke<S>(S, lineWidth: CGFloat, antialiased: Bool) -> StrokeShapeView<Self, S, EmptyView>](./stroke%28_,linewidth,antialiased%29.md)
  Traces the outline of this shape with a color or gradient.
- [func stroke(lineWidth: CGFloat) -> some Shape](./stroke%28linewidth%29.md)
  Returns a new shape that is a stroked copy of `self` with line-width defined by `lineWidth` and all other properties of `StrokeStyle` having their default values.
- [func stroke<S>(S, style: StrokeStyle, antialiased: Bool) -> StrokeShapeView<Self, S, EmptyView>](./stroke%28_,style,antialiased%29.md)
  Traces the outline of this shape with a color or gradient.
- [func stroke(style: StrokeStyle) -> some Shape](./stroke%28style%29.md)
  Returns a new shape that is a stroked copy of `self`, using the contents of `style` to define the stroke characteristics.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/shape/stroke(_:style:))*