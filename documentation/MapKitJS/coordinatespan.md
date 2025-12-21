# CoordinateSpan

**Framework**: MapKit JS  
**Kind**: class

The width and height of a map region.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
class CoordinateSpan
```

#### Overview

You use the delta values in a coordinate span to indicate the desired zoom level of the map. Smaller delta values correspond to a higher zoom level. The  in this class refers to the width and height of a region, with distances as degrees of latitude and longitude.

## Topics

### Creating a coordinate span
- [new CoordinateSpan(latitudeDelta, longitudeDelta)](coordinatespan/coordinatespanconstructor.md)
  Creates a new coordinate span object with the specified latitude and longitude deltas.
### Defining the span
- [latitudeDelta](coordinatespan/latitudedelta.md)
  The amount of north-to-south distance (in degrees) to display for the map region.
- [longitudeDelta](coordinatespan/longitudedelta.md)
  The amount of east-to-west distance (in degrees) to display for the map region.
### Copying and comparing spans
- [copy()](coordinatespan/copy.md)
  Returns a copy of the coordinate span.
- [equals(anotherSpan)](coordinatespan/equals.md)
  Returns a Boolean value that indicates whether two spans are equal.
### Instance Methods
- [toString()](coordinatespan/tostring.md)
  Returns a string representation of the coordinate span object.

## See Also

- [class Coordinate](coordinate.md)
  An object representing the latitude and longitude for a point on the Earth’s surface.
- [class CoordinateRegion](coordinateregion.md)
  A rectangular area on a map that a center coordinate and a span define, in degrees of latitude and longitude.
- [class BoundingRegion](boundingregion.md)
  A rectangular area on a map, which coordinates of the rectangle’s northeast and southwest corners define.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/coordinatespan)*