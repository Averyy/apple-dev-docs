# mapkit.Coordinate

**Framework**: MapKit JS  
**Kind**: class

An object representing the latitude and longitude for a point on the Earth’s surface.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
interface mapkit.Coordinate
```

## Mentions

- [Handling map events](handling-map-events.md)

#### Overview

A [`mapkit.Coordinate`](mapkit.coordinate/mapkit.coordinate.md) is a point on a spherical representation of the Earth at a specific degree of latitude (`90` and -`90`) and longitude (`180` to -`180`) that you use to search for locations, place annotations, and other objects on the map.

## Topics

### Creating a coordinate
- [mapkit.Coordinate](mapkit.coordinate/mapkit.coordinate.md)
  Creates a coordinate object with the specified latitude and longitude.
### Defining the coordinates
- [latitude](mapkit.coordinate/latitude.md)
  The latitude, in degrees.
- [longitude](mapkit.coordinate/longitude.md)
  The longitude, in degrees.
### Comparing, copying, and converting coordinates
- [copy](mapkit.coordinate/copy.md)
  Returns a copy of the coordinate.
- [equals](mapkit.coordinate/equals.md)
  Returns a Boolean value indicating whether two coordinates are equal.
- [toMapPoint](mapkit.coordinate/tomappoint.md)
  Returns the map point that corresponds to the coordinate.
- [toUnwrappedMapPoint](mapkit.coordinate/tounwrappedmappoint.md)
  Returns the unwrapped map point that corresponds to the coordinate.

## See Also

- [mapkit.CoordinateRegion](mapkit.coordinateregion.md)
  A rectangular area on a map that a center coordinate and a span define, in degrees of latitude and longitude.
- [mapkit.CoordinateSpan](mapkit.coordinatespan.md)
  The width and height of a map region.
- [mapkit.BoundingRegion](mapkit.boundingregion.md)
  A rectangular area on a map, which coordinates of the rectangle’s northeast and southwest corners define.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/mapkit.coordinate)*