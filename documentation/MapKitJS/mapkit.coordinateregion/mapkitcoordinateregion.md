# mapkit.CoordinateRegion

**Framework**: MapKit JS  
**Kind**: init

A rectangular geographic region that centers around a latitude and longitude coordinate.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
new mapkit.CoordinateRegion(
	mapkit.Coordinate center,
	mapkit.CoordinateSpan span
);
```

#### Discussion

Create a coordinate region by passing a center coordinate and span to the constructor.

```javascript
const coordinate = new mapkit.Coordinate(37.415, -122.048333); // latitude, longitude
const span = new mapkit.CoordinateSpan(.016, .016); // latitude delta, longitude delta
const region = new mapkit.CoordinateRegion(coordinate, span);
```

## Parameters

- `center`: A   that’s the center point of the region.
- `span`: A   that represents the amount of map to display. The span also defines the current zoom level that the map object uses.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/mapkit.coordinateregion/mapkit.coordinateregion)*