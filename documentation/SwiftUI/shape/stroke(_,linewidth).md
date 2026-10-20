# stroke(_:lineWidth:)

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
func stroke<S>(_ content: S, lineWidth: CGFloat = 1) -> some View where S : ShapeStyle
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

### Setting the stroke characteristics
- [func stroke<S>(S, lineWidth: CGFloat, antialiased: Bool) -> StrokeShapeView<Self, S, EmptyView>](./stroke%28_,linewidth,antialiased%29.md)
  Traces the outline of this shape with a color or gradient.
- [func stroke(lineWidth: CGFloat) -> some Shape](./stroke%28linewidth%29.md)
  Returns a new shape that is a stroked copy of `self` with line-width defined by `lineWidth` and all other properties of `StrokeStyle` having their default values.
- [func stroke<S>(S, style: StrokeStyle) -> some View](./stroke%28_,style%29.md)
  Traces the outline of this shape with a color or gradient.
- [func stroke<S>(S, style: StrokeStyle, antialiased: Bool) -> StrokeShapeView<Self, S, EmptyView>](./stroke%28_,style,antialiased%29.md)
  Traces the outline of this shape with a color or gradient.
- [func stroke(style: StrokeStyle) -> some Shape](./stroke%28style%29.md)
  Returns a new shape that is a stroked copy of `self`, using the contents of `style` to define the stroke characteristics.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/shape/stroke(_:linewidth:))*