# scale

**Framework**: MapKit JS  
**Kind**: method

Returns a scaled map rectangle for a map location.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
mapkit.MapRect scale(
	number scaleFactor,
	mapkit.MapPoint scaleCenter
);
```

#### Discussion

The following example demonstrates scaling a `mapkit.MapRect` instance first with a common center, and then with a common origin:

```javascript
const mapRect = new mapkit.MapRect(0.1, 0.2, 0.3, 0.4);

// Scale a MapRect to be 2x the width and 2x the height of mapRect 
// and have the same center.
const scaledRect = mapRect.scale(2);

// Same scale but this time mapRect and scaledRectAroundOrigin 
// have the same origin rather than the same center.
const scaledRectAroundOrigin = mapRect.scale(2, new mapkit.MapPoint(mapRect.minX(), mapRect.maxX()));

```

## Parameters

- `scaleFactor`: The scale factor.
- `scaleCenter`: The center map point for scaling.

## See Also

- [copy](mapkit.maprect/copy.md)
  Returns a copy of a map rectangle.
- [equals](mapkit.maprect/equals.md)
  Compares whether two map rectangles are equal.
- [toCoordinateRegion](mapkit.maprect/tocoordinateregion.md)
  Returns the region that corresponds to a map rectangle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/mapkit.maprect/scale)*