# strokeBorder(style:antialiased:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Returns a view that is the result of insetting `self` by `style.lineWidth / 2`, stroking the resulting shape with `style`, and then filling with the foreground color.

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
func strokeBorder(style: StrokeStyle, antialiased: Bool = true) -> some View
```

## See Also

### Setting the stroke border characteristics
- [func strokeBorder(_:lineWidth:antialiased:)](./strokeborder%28_,linewidth,antialiased%29.md)
  Returns a view that is the result of filling the `lineWidth`-sized border (aka inner stroke) of `self` with `content`. This is equivalent to insetting `self` by `lineWidth / 2` and stroking the resulting shape with `lineWidth` as the line-width.
- [func strokeBorder(lineWidth: CGFloat, antialiased: Bool) -> some View](./strokeborder%28linewidth,antialiased%29.md)
  Returns a view that is the result of filling the `lineWidth`-sized border (aka inner stroke) of `self` with the foreground color. This is equivalent to insetting `self` by `lineWidth / 2` and stroking the resulting shape with `lineWidth` as the line-width.
- [func strokeBorder(_:style:antialiased:)](./strokeborder%28_,style,antialiased%29.md)
  Returns a view that is the result of insetting `self` by `style.lineWidth / 2`, stroking the resulting shape with `style`, and then filling with `content`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/insettableshape/strokeborder(style:antialiased:))*