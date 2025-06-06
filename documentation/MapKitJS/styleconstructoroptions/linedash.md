# lineDash

**Framework**: MapKit JS  
**Kind**: property

An array of line and gap lengths for creating a dashed line.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
attribute number[] lineDash;
```

#### Discussion

This property provides an array to use as the line’s dash pattern where the numbers represent line and gap lengths in CSS pixels. For example, `[10, 5]` means draw for 10 pixels, leave a 5-pixel gap, then repeat. If there’s an odd number of elements in the array, MapKit JS copies and duplicates it. Set to an empty array (`[]`), to draw solid lines. The default line dash array is `[]`.

## See Also

- [lineCap](styleconstructoroptions/linecap.md)
  The style to use when drawing line endings.
- [lineDashOffset](styleconstructoroptions/linedashoffset.md)
  The number of CSS pixels to use as the offset when drawing a line’s dash pattern.
- [lineJoin](styleconstructoroptions/linejoin.md)
  The style to use when drawing joins between line segments.
- [lineWidth](styleconstructoroptions/linewidth.md)
  The width of a line’s stroke, in CSS pixels.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/styleconstructoroptions/linedash)*