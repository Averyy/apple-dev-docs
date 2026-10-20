# lineJoin

**Framework**: MapKit JS  
**Kind**: property  
**Role**: Instance Property

The corner style to apply when joining line segments.

**Availability**:
- MapKit JS 5.0+

## Declaration

```
get lineJoin(): "round" | "bevel" | "miter";
set lineJoin(lineJoin: "round" | "bevel" | "miter");
```

#### Discussion

The three options for line joins are `miter` (join is a sharp corner), `round` (join is a rounded corner), or `bevel` (join is a beveled corner). The default line join is `round`.

## See Also

### Styling lines
- [lineCap](./linecap.md)
  The style to use when drawing line endings.
- [lineDash](./linedash.md)
  An array of line and gap lengths for creating a dashed line.
- [lineDashOffset](./linedashoffset.md)
  The number of CSS pixels to use as an offset when drawing a line’s dash pattern.
- [lineWidth](./linewidth.md)
  The width of a line’s stroke, in CSS pixels.
- [lineGradient](./linegradient.md)
  The gradient to apply along the line.
- [class LineGradient](../linegradient.md)
  A line that displays with a gradient along the length of the line.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/style/linejoin)*