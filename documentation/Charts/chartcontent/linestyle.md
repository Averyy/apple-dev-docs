# lineStyle(_:)

**Framework**: Swift Charts  
**Kind**: method

Sets the style for line marks.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
nonisolated
func lineStyle(_ style: StrokeStyle) -> some ChartContent
```

#### Discussion

> ⚠️ **Warning**: Use this `.lineStyle(_:)` overload only if you have a predefined stroke style. The provided stroke style will override default line width and line cap for line marks.

Use this `.lineStyle(_:)` overload only if you have a predefined stroke style. The provided stroke style will override default line width and line cap for line marks.

## Parameters

- `style`: The stroke style.

## See Also

- [func foregroundStyle<S>(S) -> some ChartContent](chartcontent/foregroundstyle(_:).md)
  Sets the foreground style for the chart content.
- [func opacity(Double) -> some ChartContent](chartcontent/opacity(_:).md)
  Sets the opacity for the chart content.
- [func cornerRadius(CGFloat, style: RoundedCornerStyle) -> some ChartContent](chartcontent/cornerradius(_:style:).md)
  Sets the corner radius of the chart content.
- [func interpolationMethod(InterpolationMethod) -> some ChartContent](chartcontent/interpolationmethod(_:).md)
  Plots line and area marks with the interpolation method that you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/charts/chartcontent/linestyle(_:))*