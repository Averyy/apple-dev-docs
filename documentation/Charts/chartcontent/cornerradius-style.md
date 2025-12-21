# cornerRadius(_:style:)

**Framework**: Swift Charts  
**Kind**: method

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

- [func foregroundStyle<S>(S) -> some ChartContent](chartcontent/foregroundstyle(_:).md)
  Sets the foreground style for the chart content.
- [func opacity(Double) -> some ChartContent](chartcontent/opacity(_:).md)
  Sets the opacity for the chart content.
- [func blur(radius: CGFloat) -> some ChartContent](chartcontent/blur(radius:).md)
  Applies a Gaussian blur to this chart content.
- [func lineStyle(StrokeStyle) -> some ChartContent](chartcontent/linestyle(_:).md)
  Sets the style for line marks.
- [func shadow(color: Color, radius: CGFloat, x: CGFloat, y: CGFloat) -> some ChartContent](chartcontent/shadow(color:radius:x:y:).md)
  A chart content that adds a shadow to this chart content.
- [func interpolationMethod(InterpolationMethod) -> some ChartContent](chartcontent/interpolationmethod(_:).md)
  Plots line and area marks with the interpolation method that you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/charts/chartcontent/cornerradius(_:style:))*