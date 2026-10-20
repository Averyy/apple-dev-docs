# strokeBorder(_:style:antialiased:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Returns a view that is the result of insetting `self` by `style.lineWidth / 2`, stroking the resulting shape with `style`, and then filling with `content`.

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
nonisolated func strokeBorder<S>(_ content: S = .foreground, style: StrokeStyle, antialiased: Bool = true) -> StrokeBorderShapeView<Self, S, EmptyView> where S : ShapeStyle
```

**Other overloads**:

```swift
func strokeBorder<S>(_ content: S, style: StrokeStyle, antialiased: Bool = true) -> some View where S : ShapeStyle
```

## See Also

### Setting the stroke border characteristics
- [func strokeBorder(_:lineWidth:antialiased:)](./strokeborder%28_,linewidth,antialiased%29.md)
  Returns a view that is the result of filling the `lineWidth`-sized border (aka inner stroke) of `self` with `content`. This is equivalent to insetting `self` by `lineWidth / 2` and stroking the resulting shape with `lineWidth` as the line-width.
- [func strokeBorder(lineWidth: CGFloat, antialiased: Bool) -> some View](./strokeborder%28linewidth,antialiased%29.md)
  Returns a view that is the result of filling the `lineWidth`-sized border (aka inner stroke) of `self` with the foreground color. This is equivalent to insetting `self` by `lineWidth / 2` and stroking the resulting shape with `lineWidth` as the line-width.
- [func strokeBorder(style: StrokeStyle, antialiased: Bool) -> some View](./strokeborder%28style,antialiased%29.md)
  Returns a view that is the result of insetting `self` by `style.lineWidth / 2`, stroking the resulting shape with `style`, and then filling with the foreground color.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/insettableshape/strokeborder(_:style:antialiased:))*