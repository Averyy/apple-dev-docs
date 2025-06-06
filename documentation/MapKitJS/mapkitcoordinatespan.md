# mapkit.CoordinateSpan

**Framework**: MapKit JS  
**Kind**: class

The width and height of a map region.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
interface mapkit.CoordinateSpan
```

#### Overview

You use the delta values in a coordinate span to indicate the desired zoom level of the map. Smaller delta values correspond to a higher zoom level. The  in this class refers to the width and height of a region, with distances as degrees of latitude and longitude.

## Topics

### Creating a coordinate span
- [mapkit.CoordinateSpan](mapkit.coordinatespan/mapkit.coordinatespan.md)
  Creates a new coordinate span object with the specified latitude and longitude deltas.
### Defining the span
- [latitudeDelta](mapkit.coordinatespan/latitudedelta.md)
  The amount of north-to-south distance (in degrees) to display for the map region.
- [longitudeDelta](mapkit.coordinatespan/longitudedelta.md)
  The amount of east-to-west distance (in degrees) to display for the map region.
### Copying and comparing spans
- [copy](mapkit.coordinatespan/copy.md)
  Returns a copy of the coordinate span.
- [equals](mapkit.coordinatespan/equals.md)
  Returns a Boolean value that indicates whether two spans are equal.

## See Also

- [mapkit.Coordinate](mapkit.coordinate.md)
  An object representing the latitude and longitude for a point on the Earth’s surface.
- [mapkit.CoordinateRegion](mapkit.coordinateregion.md)
  A rectangular area on a map that a center coordinate and a span define, in degrees of latitude and longitude.
- [mapkit.BoundingRegion](mapkit.boundingregion.md)
  A rectangular area on a map, which coordinates of the rectangle’s northeast and southwest corners define.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/mapkit.coordinatespan)*