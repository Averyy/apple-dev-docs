# lineGradient

**Framework**: MapKit JS  
**Kind**: property

The gradient to apply along the line.

**Availability**:
- MapKit JS 5.45+

## Declaration

```swift
attribute mapkit.LineGradient lineGradient;
```

#### Discussion

If a style has both [`strokeColor`](mapkit.style/strokecolor.md) and [`lineGradient`](mapkit.style/linegradient.md) definitions, MapKit JS displays the [`lineGradient`](mapkit.style/linegradient.md). If you don’t define a color at the start or end location within the gradient, MapKit JS uses the style’s [`strokeColor`](mapkit.style/strokecolor.md) as the default.

## See Also

- [lineCap](mapkit.style/linecap.md)
  The style to use when drawing line endings.
- [lineDash](mapkit.style/linedash.md)
  An array of line and gap lengths for creating a dashed line.
- [lineDashOffset](mapkit.style/linedashoffset.md)
  The number of CSS pixels to use as an offset when drawing a line’s dash pattern.
- [lineJoin](mapkit.style/linejoin.md)
  The corner style to apply when joining line segments.
- [lineWidth](mapkit.style/linewidth.md)
  The width of a line’s stroke, in CSS pixels.
- [mapkit.LineGradient](mapkit.linegradient.md)
  A line that displays with a gradient along the length of the line.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/mapkit.style/linegradient)*