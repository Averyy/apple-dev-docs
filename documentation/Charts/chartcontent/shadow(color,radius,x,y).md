# shadow(color:radius:x:y:)

**Framework**: Swift Charts  
**Kind**: method  
**Role**: Instance Method

A chart content that adds a shadow to this chart content.

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
func shadow(color: Color = Color(.sRGBLinear, white: 0, opacity: 0.33), radius: CGFloat, x: CGFloat = 0, y: CGFloat = 0) -> some ChartContent
```

## Parameters

- `color`: The shadow’s color.
- `radius`: A measure of how much to blur the shadow. Larger values result in more blur.
- `x`: An amount to offset the shadow horizontally.
- `y`: An amount to offset the shadow vertically.

## See Also

### Styling marks
- [func foregroundStyle<S>(S) -> some ChartContent](./foregroundstyle%28_%29.md)
  Sets the foreground style for the chart content.
- [func opacity(Double) -> some ChartContent](./opacity%28_%29.md)
  Sets the opacity for the chart content.
- [func blur(radius: CGFloat) -> some ChartContent](./blur%28radius%29.md)
  Applies a Gaussian blur to this chart content.
- [func cornerRadius(CGFloat, style: RoundedCornerStyle) -> some ChartContent](./cornerradius%28_,style%29.md)
  Sets the corner radius of the chart content.
- [func lineStyle(StrokeStyle) -> some ChartContent](./linestyle%28_%29.md)
  Sets the style for line marks.
- [func interpolationMethod(InterpolationMethod) -> some ChartContent](./interpolationmethod%28_%29.md)
  Plots line and area marks with the interpolation method that you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/charts/chartcontent/shadow(color:radius:x:y:))*