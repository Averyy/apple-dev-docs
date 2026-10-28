# lineJoin

**Framework**: MapKit JS  
**Kind**: property  
**Role**: Interface Property

The style to use when drawing joins between line segments.

**Availability**:
- MapKit JS 5.0+

## Declaration

```
lineJoin?: "bevel" | "miter" | "round";
```

## Discussion

The three options for line joins are `miter` (the join is a sharp corner), `round` (the join is a rounded corner), or `bevel` (the join is a beveled corner). The default line join is `round`.

## See Also

### Setting line styles
- [lineCap](./linecap.md)
  The style to use when drawing line endings.
- [lineDash](./linedash.md)
  An array of line and gap lengths for creating a dashed line.
- [lineDashOffset](./linedashoffset.md)
  The number of CSS pixels to use as the offset when drawing a line’s dash pattern.
- [lineWidth](./linewidth.md)
  The width of a line’s stroke, in CSS pixels.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/styleconstructoroptions/linejoin)*