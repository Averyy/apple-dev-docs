# toCoordinateRegion

**Framework**: MapKit JS  
**Kind**: method

Returns the region that corresponds to a map rectangle.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
mapkit.CoordinateRegion toCoordinateRegion();
```

#### Return Value

A [`mapkit.CoordinateRegion`](mapkit.coordinateregion.md) object that corresponds to a map rectangle.

#### Discussion

It’s often easier to work with a map rectangle than a [`mapkit.CoordinateRegion`](mapkit.coordinateregion.md).

The following example demonstrates how to convert a [`mapkit.MapRect`](mapkit.maprect/mapkit.maprect.md) instance to a [`mapkit.CoordinateRegion`](mapkit.coordinateregion.md) and back again:

```javascript
var mapRect = new mapkit.MapRect(0.1, 0.2, 0.3, 0.4);

// Return a coordinate region with center (33.841220320476786, -90) and span (106.57400641480324, 108).
var coordinateRegion = mapRect.toCoordinateRegion();

// Return the same map rectangle as mapRect, plus or minus any floating point inaccuracies.
var newMapRect = coordinateRegion.toMapRect();
```

## See Also

- [copy](mapkit.maprect/copy.md)
  Returns a copy of a map rectangle.
- [equals](mapkit.maprect/equals.md)
  Compares whether two map rectangles are equal.
- [scale](mapkit.maprect/scale.md)
  Returns a scaled map rectangle for a map location.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/mapkit.maprect/tocoordinateregion)*