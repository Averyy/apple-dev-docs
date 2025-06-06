# toBoundingRegion

**Framework**: MapKit JS  
**Kind**: method

Returns the bounding region that corresponds to the specified coordinate region.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
mapkit.BoundingRegion toBoundingRegion();
```

#### Return Value

A [`mapkit.BoundingRegion`](mapkit.boundingregion/mapkit.boundingregion.md).

#### Discussion

A bounding region is similar to a coordinate region; both represent a rectangular area on the 2D projected surface of the map. MapKit JS defines a coordinate region by a center coordinate and a span. The framework defines a bounding region by coordinates representing the rectangle’s northeast and southwest corners.

The following example shows how to convert a coordinate region to a bounding region:

```javascript
// Create a coordinate region named myRegion.
var coordinate = new mapkit.Coordinate(37.415, -122.048333); 
// The initializer requires parameters in the order of latitude, longitude.
var span = new mapkit.CoordinateSpan(.016, .016); 
// The initializer requires parameters in the order of latitude delta, longitude delta.
var myRegion = new mapkit.CoordinateRegion(coordinate, span);

// Convert this coordinate region to a bounding region.
var myBoundingRegion = myRegion.toBoundingRegion();
```

## See Also

- [copy](mapkit.coordinateregion/copy.md)
  Returns a copy of the calling coordinate region.
- [equals](mapkit.coordinateregion/equals.md)
  Returns a Boolean value indicating whether two regions are equal.
- [toMapRect](mapkit.coordinateregion/tomaprect.md)
  Returns the map rectangle that corresponds to the calling coordinate region.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/mapkit.coordinateregion/toboundingregion)*