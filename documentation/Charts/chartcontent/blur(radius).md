# blur(radius:)

**Framework**: Swift Charts  
**Kind**: method  
**Role**: Instance Method

Applies a Gaussian blur to this chart content.

**Availability**:
- iOS 16.4+
- iPadOS 16.4+
- Mac Catalyst 16.4+
- macOS 13.3+
- tvOS 16.4+
- visionOS 1.0+
- watchOS 9.4+

## Declaration

```swift
nonisolated
func blur(radius: CGFloat) -> some ChartContent
```

## Parameters

- `radius`: The radial size of the blur. A blur is more diffuse when its radius is large.

## See Also

### Styling marks
- [func foregroundStyle<S>(S) -> some ChartContent](./foregroundstyle%28_%29.md)
  Sets the foreground style for the chart content.
- [func opacity(Double) -> some ChartContent](./opacity%28_%29.md)
  Sets the opacity for the chart content.
- [func cornerRadius(CGFloat, style: RoundedCornerStyle) -> some ChartContent](./cornerradius%28_,style%29.md)
  Sets the corner radius of the chart content.
- [func lineStyle(StrokeStyle) -> some ChartContent](./linestyle%28_%29.md)
  Sets the style for line marks.
- [func shadow(color: Color, radius: CGFloat, x: CGFloat, y: CGFloat) -> some ChartContent](./shadow%28color,radius,x,y%29.md)
  A chart content that adds a shadow to this chart content.
- [func interpolationMethod(InterpolationMethod) -> some ChartContent](./interpolationmethod%28_%29.md)
  Plots line and area marks with the interpolation method that you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/charts/chartcontent/blur(radius:))*