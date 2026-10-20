# cornerRadius(_:style:)

**Framework**: Swift Charts  
**Kind**: method  
**Role**: Instance Method

Sets the corner radius of the chart content.

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
func cornerRadius(_ radius: CGFloat, style: RoundedCornerStyle = .continuous) -> some ChartContent
```

## Parameters

- `radius`: The corner radius.
- `style`: The style of the rounded corners.

## See Also

### Styling marks
- [func foregroundStyle<S>(S) -> some ChartContent](./foregroundstyle%28_%29.md)
  Sets the foreground style for the chart content.
- [func opacity(Double) -> some ChartContent](./opacity%28_%29.md)
  Sets the opacity for the chart content.
- [func blur(radius: CGFloat) -> some ChartContent](./blur%28radius%29.md)
  Applies a Gaussian blur to this chart content.
- [func lineStyle(StrokeStyle) -> some ChartContent](./linestyle%28_%29.md)
  Sets the style for line marks.
- [func shadow(color: Color, radius: CGFloat, x: CGFloat, y: CGFloat) -> some ChartContent](./shadow%28color,radius,x,y%29.md)
  A chart content that adds a shadow to this chart content.
- [func interpolationMethod(InterpolationMethod) -> some ChartContent](./interpolationmethod%28_%29.md)
  Plots line and area marks with the interpolation method that you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/charts/chartcontent/cornerradius(_:style:))*