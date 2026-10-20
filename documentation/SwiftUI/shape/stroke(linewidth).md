# stroke(lineWidth:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Returns a new shape that is a stroked copy of `self` with line-width defined by `lineWidth` and all other properties of `StrokeStyle` having their default values.

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
func stroke(lineWidth: CGFloat = 1) -> some Shape
```

## See Also

### Setting the stroke characteristics
- [func stroke<S>(S, lineWidth: CGFloat) -> some View](./stroke%28_,linewidth%29.md)
  Traces the outline of this shape with a color or gradient.
- [func stroke<S>(S, lineWidth: CGFloat, antialiased: Bool) -> StrokeShapeView<Self, S, EmptyView>](./stroke%28_,linewidth,antialiased%29.md)
  Traces the outline of this shape with a color or gradient.
- [func stroke<S>(S, style: StrokeStyle) -> some View](./stroke%28_,style%29.md)
  Traces the outline of this shape with a color or gradient.
- [func stroke<S>(S, style: StrokeStyle, antialiased: Bool) -> StrokeShapeView<Self, S, EmptyView>](./stroke%28_,style,antialiased%29.md)
  Traces the outline of this shape with a color or gradient.
- [func stroke(style: StrokeStyle) -> some Shape](./stroke%28style%29.md)
  Returns a new shape that is a stroked copy of `self`, using the contents of `style` to define the stroke characteristics.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/shape/stroke(linewidth:))*