# addColorStopAtIndex(index, color)

**Framework**: MapKit JS  
**Kind**: method

Adds a color transition at the index point in the list of points within a polyline.

**Availability**:
- MapKit JS 5.45+

## Declaration

```swift
addColorStopAtIndex(index: number, color: string): void;
```

#### Discussion

If the index is invalid, MapKit JS logs a warning to the console, but doesn’t change the object.

## Parameters

- `index`: A valid index into a polyline’s  .
- `color`: The CSS color at the index point.

## See Also

- [new LineGradient(colorStops)](linegradient/linegradientconstructor.md)
  Creates a style that renders a gradient along the length of a line.
- [addColorStop(offset, color)](linegradient/addcolorstop.md)
  Adds a color transition point to the gradient.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/linegradient/addcolorstopatindex)*