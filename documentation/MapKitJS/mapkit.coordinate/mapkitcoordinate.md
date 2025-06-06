# mapkit.Coordinate

**Framework**: MapKit JS  
**Kind**: init

Creates a coordinate object with the specified latitude and longitude.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
new mapkit.Coordinate(
	number latitude,
	number longitude
);
```

#### Discussion

Create a new `mapkit.Coordinate` like this:

```javascript
var coordinate = new mapkit.Coordinate(37.415, -122.048333);	// latitude, longitude
coordinate.equals(otherCoordinate) // Returns true if otherCoordinate is at the same position (within a small margin of error).
```

## Parameters

- `latitude`: The latitude in degrees.
- `longitude`: The longitude in degrees.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/mapkit.coordinate/mapkit.coordinate)*