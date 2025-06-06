# addColorStopAtIndex

**Framework**: MapKit JS  
**Kind**: method

Adds a color transition at the index point in the list of points within a polyline.

**Availability**:
- MapKit JS 5.45+

## Declaration

```swift
void addColorStopAtIndex(
	number index,
	string color
);
```

#### Discussion

If the index is invalid, MapKit JS logs a warning to the console, but doesn’t change the object.

## Parameters

- `index`: A valid index into a polyline’s  .
- `color`: The CSS color at the index point.

## See Also

- [mapkit.LineGradient](mapkit.linegradient/mapkit.linegradient.md)
  Creates a style that renders a gradient along the length of a line.
- [addColorStop](mapkit.linegradient/addcolorstop.md)
  Adds a color transition point to the gradient.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/mapkit.linegradient/addcolorstopatindex)*