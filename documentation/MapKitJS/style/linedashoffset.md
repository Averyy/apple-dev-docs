# lineDashOffset

**Framework**: MapKit JS  
**Kind**: property  
**Role**: Instance Property

The number of CSS pixels to use as an offset when drawing a line’s dash pattern.

**Availability**:
- MapKit JS 5.0+

## Declaration

```
get lineDashOffset(): number;
set lineDashOffset(lineDashOffset: number);
```

#### Discussion

This has no effect if you set `lineDash` to draw solid lines. The default line dash offset is `0`.

## See Also

### Styling lines
- [lineCap](./linecap.md)
  The style to use when drawing line endings.
- [lineDash](./linedash.md)
  An array of line and gap lengths for creating a dashed line.
- [lineJoin](./linejoin.md)
  The corner style to apply when joining line segments.
- [lineWidth](./linewidth.md)
  The width of a line’s stroke, in CSS pixels.
- [lineGradient](./linegradient.md)
  The gradient to apply along the line.
- [class LineGradient](../linegradient.md)
  A line that displays with a gradient along the length of the line.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/style/linedashoffset)*