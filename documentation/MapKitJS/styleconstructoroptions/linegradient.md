# lineGradient

**Framework**: MapKit JS  
**Kind**: property

The gradient to apply along the line.

**Availability**:
- MapKit JS 5.45+

## Declaration

```swift
lineGradient?: LineGradient;
```

#### Discussion

If a style has both [`strokeColor`](style/strokecolor.md) and [`lineGradient`](style/linegradient.md) definitions, [`lineGradient`](style/linegradient.md) takes precedence and displays. If you don’t define a color at the start or end location within the gradient, MapKit JS uses the style’s [`strokeColor`](style/strokecolor.md).

## See Also

- [strokeColor](styleconstructoroptions/strokecolor.md)
  The stroke color of a line.
- [strokeOpacity](styleconstructoroptions/strokeopacity.md)
  The opacity of the stroke color.
- [strokeStart](styleconstructoroptions/strokestart.md)
  The unit distance along the line where a stroke begins.
- [strokeEnd](styleconstructoroptions/strokeend.md)
  The unit distance along the line where a stroke ends.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/styleconstructoroptions/linegradient)*