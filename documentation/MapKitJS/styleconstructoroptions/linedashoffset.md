# lineDashOffset

**Framework**: MapKit JS  
**Kind**: property  
**Role**: Interface Property

The number of CSS pixels to use as the offset when drawing a line’s dash pattern.

**Availability**:
- MapKit JS 5.0+

## Declaration

```
lineDashOffset?: number;
```

## Discussion

This has no effect if you set `lineDash` to draw solid lines by setting this property to an empty array. The default line dash offset is `0`.

## See Also

### Setting line styles
- [lineCap](./linecap.md)
  The style to use when drawing line endings.
- [lineDash](./linedash.md)
  An array of line and gap lengths for creating a dashed line.
- [lineJoin](./linejoin.md)
  The style to use when drawing joins between line segments.
- [lineWidth](./linewidth.md)
  The width of a line’s stroke, in CSS pixels.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/styleconstructoroptions/linedashoffset)*