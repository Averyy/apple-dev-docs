# BoundingRegion

**Framework**: MapKit JS  
**Kind**: class

A rectangular area on a map, which coordinates of the rectangle’s northeast and southwest corners define.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
class BoundingRegion
```

#### Overview

Similar to a [`CoordinateRegion`](coordinateregion.md), [`BoundingRegion`](boundingregion.md) represents a rectangular area on the 2D-projected surface. However, instead of describing a center coordinate and a span, MapKit JS defines a bounding region by the coordinates of the rectangle’s northeast and southwest corners.

## Topics

### Creating a bounding region
- [new BoundingRegion(northLatitude, eastLongitude, southLatitude, westLongitude)](boundingregion/boundingregionconstructor.md)
  Creates a rectangular bounding region, which the latitude and longitude coordinates of the rectangle’s northeast and southwest corners define.
### Defining a bounding region
- [eastLongitude](boundingregion/eastlongitude.md)
  The east longitude of the bounding region.
- [northLatitude](boundingregion/northlatitude.md)
  The north latitude of the bounding region.
- [southLatitude](boundingregion/southlatitude.md)
  The south latitude of the bounding region.
- [westLongitude](boundingregion/westlongitude.md)
  The west longitude of the bounding region.
### Copying and converting regions
- [copy()](boundingregion/copy.md)
  Returns a copy of the calling bounding region.
- [toCoordinateRegion()](boundingregion/tocoordinateregion.md)
  Returns the coordinate region that corresponds to the calling bounding region.
### Instance Methods
- [toString()](boundingregion/tostring.md)
  Returns a string representation of the bounding region object.

## See Also

- [class Coordinate](coordinate.md)
  An object representing the latitude and longitude for a point on the Earth’s surface.
- [class CoordinateRegion](coordinateregion.md)
  A rectangular area on a map that a center coordinate and a span define, in degrees of latitude and longitude.
- [class CoordinateSpan](coordinatespan.md)
  The width and height of a map region.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/boundingregion)*