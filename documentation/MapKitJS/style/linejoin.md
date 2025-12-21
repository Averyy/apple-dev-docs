# lineJoin

**Framework**: MapKit JS  
**Kind**: property

The corner style to apply when joining line segments.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
get lineJoin(): CanvasLineJoin;
set lineJoin(lineJoin: CanvasLineJoin);
```

#### Discussion

The three options for line joins are `miter` (join is a sharp corner), `round` (join is a rounded corner), or `bevel` (join is a beveled corner). The default line join is `round`.

## See Also

- [lineCap](style/linecap.md)
  The style to use when drawing line endings.
- [lineDash](style/linedash.md)
  An array of line and gap lengths for creating a dashed line.
- [lineDashOffset](style/linedashoffset.md)
  The number of CSS pixels to use as an offset when drawing a line’s dash pattern.
- [lineWidth](style/linewidth.md)
  The width of a line’s stroke, in CSS pixels.
- [lineGradient](style/linegradient.md)
  The gradient to apply along the line.
- [class LineGradient](linegradient.md)
  A line that displays with a gradient along the length of the line.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/style/linejoin)*