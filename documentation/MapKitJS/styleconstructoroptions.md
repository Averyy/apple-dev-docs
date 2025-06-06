# StyleConstructorOptions

**Framework**: MapKit JS  
**Kind**: struct

Initial values of options for applying style to overlays.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
dictionary StyleConstructorOptions {
	string strokeColor;
	number strokeOpacity;
	number strokeStart;
	number strokeEnd;
	number lineWidth;
	string lineCap;
	string lineJoin;
	number[] lineDash;
	number lineDashOffset;
	mapkit.LineGradient lineGradient;
	string fillColor;
	number fillOpacity;
	string fillRule;
};
```

## Topics

### Setting fill styles
- [fillColor](styleconstructoroptions/fillcolor.md)
  The fill color of a shape.
- [fillOpacity](styleconstructoroptions/fillopacity.md)
  The opacity of the fill color.
- [fillRule](styleconstructoroptions/fillrule.md)
  A rule for determining whether a point is inside or outside a polygon.
### Setting line styles
- [lineCap](styleconstructoroptions/linecap.md)
  The style to use when drawing line endings.
- [lineDash](styleconstructoroptions/linedash.md)
  An array of line and gap lengths for creating a dashed line.
- [lineDashOffset](styleconstructoroptions/linedashoffset.md)
  The number of CSS pixels to use as the offset when drawing a line’s dash pattern.
- [lineJoin](styleconstructoroptions/linejoin.md)
  The style to use when drawing joins between line segments.
- [lineWidth](styleconstructoroptions/linewidth.md)
  The width of a line’s stroke, in CSS pixels.
### Setting stroke styles
- [strokeColor](styleconstructoroptions/strokecolor.md)
  The stroke color of a line.
- [strokeOpacity](styleconstructoroptions/strokeopacity.md)
  The opacity of the stroke color.
- [strokeStart](styleconstructoroptions/strokestart.md)
  The unit distance along the line where a stroke begins.
- [strokeEnd](styleconstructoroptions/strokeend.md)
  The unit distance along the line where a stroke ends.
- [lineGradient](styleconstructoroptions/linegradient.md)
  The gradient to apply along the line.

## See Also

- [mapkit.Style](mapkit.style/mapkit.style.md)
  Creates and initializes a style object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/styleconstructoroptions)*