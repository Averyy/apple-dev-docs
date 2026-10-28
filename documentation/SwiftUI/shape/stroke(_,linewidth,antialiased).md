# stroke(_:lineWidth:antialiased:)

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
nonisolated func stroke<S>(_ content: S, lineWidth: CGFloat = 1, antialiased: Bool = true) -> StrokeShapeView<Self, S, EmptyView> where S : ShapeStyle
```

## Return Value

A stroked shape.

## Discussion

The following example draws a circle with a purple stroke:

```swift
Circle().stroke(Color.purple, lineWidth: 5)
```

## Parameters

- `content`: The color or gradient with which to stroke this shape.
- `lineWidth`: The width of the stroke that outlines this shape.
- `antialiased`: A Boolean value that specifies whether to allow antialiasing. Pass `true` to allow antialising, otherwise `false`.

## See Also

### Setting the stroke characteristics
- [func stroke<S>(S, lineWidth: CGFloat) -> some View](./stroke%28_,linewidth%29.md)
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

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/shape/stroke(_:linewidth:antialiased:))*