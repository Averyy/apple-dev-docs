# stroke(_:style:antialiased:)

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
func stroke<S>(_ content: S, style: StrokeStyle, antialiased: Bool = true) -> StrokeShapeView<Self, S, EmptyView> where S : ShapeStyle
```

#### Return Value

A stroked shape.

#### Discussion

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
- `style`: The stroke characteristics — such as the line’s width and   whether the stroke is dashed — that determine how to render this   shape.

## See Also

- [func stroke<S>(S, lineWidth: CGFloat) -> some View](shape/stroke(_:linewidth:).md)
  Traces the outline of this shape with a color or gradient.
- [func stroke<S>(S, lineWidth: CGFloat, antialiased: Bool) -> StrokeShapeView<Self, S, EmptyView>](shape/stroke(_:linewidth:antialiased:).md)
  Traces the outline of this shape with a color or gradient.
- [func stroke(lineWidth: CGFloat) -> some Shape](shape/stroke(linewidth:).md)
  Returns a new shape that is a stroked copy of `self` with line-width defined by `lineWidth` and all other properties of `StrokeStyle` having their default values.
- [func stroke<S>(S, style: StrokeStyle) -> some View](shape/stroke(_:style:).md)
  Traces the outline of this shape with a color or gradient.
- [func stroke(style: StrokeStyle) -> some Shape](shape/stroke(style:).md)
  Returns a new shape that is a stroked copy of `self`, using the contents of `style` to define the stroke characteristics.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/shape/stroke(_:style:antialiased:))*