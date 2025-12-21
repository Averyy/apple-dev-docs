# lineDashOffset

**Framework**: MapKit JS  
**Kind**: property

The number of CSS pixels to use as an offset when drawing a line’s dash pattern.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
get lineDashOffset(): number;
set lineDashOffset(lineDashOffset: number);
```

#### Discussion

This has no effect if you set `lineDash` to draw solid lines. The default line dash offset is `0`.

## See Also

- [lineCap](style/linecap.md)
  The style to use when drawing line endings.
- [lineDash](style/linedash.md)
  An array of line and gap lengths for creating a dashed line.
- [lineJoin](style/linejoin.md)
  The corner style to apply when joining line segments.
- [lineWidth](style/linewidth.md)
  The width of a line’s stroke, in CSS pixels.
- [lineGradient](style/linegradient.md)
  The gradient to apply along the line.
- [class LineGradient](linegradient.md)
  A line that displays with a gradient along the length of the line.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/style/linedashoffset)*