# equals

**Framework**: MapKit JS  
**Kind**: method

Returns a Boolean value indicating whether two regions are equal.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
boolean equals(
	mapkit.CoordinateRegion anotherRegion
);
```

#### Return Value

`true` if the region that `anotherRegion` specifies is equal to the calling [`mapkit.CoordinateRegion`](mapkit.coordinateregion/mapkit.coordinateregion.md); otherwise, `false`.

#### Discussion

The following example shows how to determine whether a given region is equal to the region that’s displaying on the map.

```javascript
// Create a map.
var map = new mapkit.Map("my-map-element-id");

// Create a region named myRegion.
var coordinate = new mapkit.Coordinate(37.415, -122.048333); // latitude, longitude
var span = new mapkit.CoordinateSpan(.016, .016); // latitude delta, longitude delta
var myRegion = new mapkit.CoordinateRegion(coordinate, span);

// Check whether myRegion is equal to the current map region.
if (myRegion.equals(map.region))
   console.log("These two regions are equal.");

```

## Parameters

- `anotherRegion`: The region to compare.

## See Also

- [copy](mapkit.coordinateregion/copy.md)
  Returns a copy of the calling coordinate region.
- [toBoundingRegion](mapkit.coordinateregion/toboundingregion.md)
  Returns the bounding region that corresponds to the specified coordinate region.
- [toMapRect](mapkit.coordinateregion/tomaprect.md)
  Returns the map rectangle that corresponds to the calling coordinate region.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/mapkit.coordinateregion/equals)*