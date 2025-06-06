# stroke(lineWidth:)

**Framework**: SwiftUI  
**Kind**: method

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

- [func stroke<S>(S, lineWidth: CGFloat) -> some View](shape/stroke(_:linewidth:).md)
  Traces the outline of this shape with a color or gradient.
- [func stroke<S>(S, lineWidth: CGFloat, antialiased: Bool) -> StrokeShapeView<Self, S, EmptyView>](shape/stroke(_:linewidth:antialiased:).md)
  Traces the outline of this shape with a color or gradient.
- [func stroke<S>(S, style: StrokeStyle) -> some View](shape/stroke(_:style:).md)
  Traces the outline of this shape with a color or gradient.
- [func stroke<S>(S, style: StrokeStyle, antialiased: Bool) -> StrokeShapeView<Self, S, EmptyView>](shape/stroke(_:style:antialiased:).md)
  Traces the outline of this shape with a color or gradient.
- [func stroke(style: StrokeStyle) -> some Shape](shape/stroke(style:).md)
  Returns a new shape that is a stroked copy of `self`, using the contents of `style` to define the stroke characteristics.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/shape/stroke(linewidth:))*