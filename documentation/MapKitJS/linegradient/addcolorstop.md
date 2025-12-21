# addColorStop(offset, color)

**Framework**: MapKit JS  
**Kind**: method

Adds a color transition point to the gradient.

**Availability**:
- MapKit JS 5.45+

## Declaration

```swift
addColorStop(offset: number, color: string): void;
```

#### Discussion

If offset is less than `0` or greater than `1`, MapKit JS logs a warning to the console, but doesn’t change the object.

## Parameters

- `offset`: The unit distance at which to add the color.
- `color`: The CSS color at the transition point.

## See Also

- [new LineGradient(colorStops)](linegradient/linegradientconstructor.md)
  Creates a style that renders a gradient along the length of a line.
- [addColorStopAtIndex(index, color)](linegradient/addcolorstopatindex.md)
  Adds a color transition at the index point in the list of points within a polyline.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/linegradient/addcolorstop)*