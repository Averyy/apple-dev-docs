# blur(radius:)

**Framework**: Swift Charts  
**Kind**: method

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

- [func foregroundStyle<S>(S) -> some ChartContent](chartcontent/foregroundstyle(_:).md)
  Sets the foreground style for the chart content.
- [func opacity(Double) -> some ChartContent](chartcontent/opacity(_:).md)
  Sets the opacity for the chart content.
- [func cornerRadius(CGFloat, style: RoundedCornerStyle) -> some ChartContent](chartcontent/cornerradius(_:style:).md)
  Sets the corner radius of the chart content.
- [func lineStyle(StrokeStyle) -> some ChartContent](chartcontent/linestyle(_:).md)
  Sets the style for line marks.
- [func shadow(color: Color, radius: CGFloat, x: CGFloat, y: CGFloat) -> some ChartContent](chartcontent/shadow(color:radius:x:y:).md)
  A chart content that adds a shadow to this chart content.
- [func interpolationMethod(InterpolationMethod) -> some ChartContent](chartcontent/interpolationmethod(_:).md)
  Plots line and area marks with the interpolation method that you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/charts/chartcontent/blur(radius:))*