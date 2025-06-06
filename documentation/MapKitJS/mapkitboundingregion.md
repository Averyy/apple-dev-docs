# mapkit.BoundingRegion

**Framework**: MapKit JS  
**Kind**: class

A rectangular area on a map, which coordinates of the rectangle’s northeast and southwest corners define.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
interface mapkit.BoundingRegion
```

#### Overview

Similar to a [`mapkit.CoordinateRegion`](mapkit.coordinateregion.md), [`mapkit.BoundingRegion`](mapkit.boundingregion/mapkit.boundingregion.md) represents a rectangular area on the 2D-projected surface. However, instead of describing a center coordinate and a span, MapKit JS defines a bounding region by the coordinates of the rectangle’s northeast and southwest corners.

## Topics

### Creating a bounding region
- [mapkit.BoundingRegion](mapkit.boundingregion/mapkit.boundingregion.md)
  Creates a rectangular bounding region, which the latitude and longitude coordinates of the rectangle’s northeast and southwest corners define.
### Defining a bounding region
- [eastLongitude](mapkit.boundingregion/eastlongitude.md)
  The east longitude of the bounding region.
- [northLatitude](mapkit.boundingregion/northlatitude.md)
  The north latitude of the bounding region.
- [southLatitude](mapkit.boundingregion/southlatitude.md)
  The south latitude of the bounding region.
- [westLongitude](mapkit.boundingregion/westlongitude.md)
  The west longitude of the bounding region.
### Copying and converting regions
- [copy](mapkit.boundingregion/copy.md)
  Returns a copy of the calling bounding region.
- [toCoordinateRegion](mapkit.boundingregion/tocoordinateregion.md)
  Returns the coordinate region that corresponds to the calling bounding region.

## See Also

- [mapkit.Coordinate](mapkit.coordinate.md)
  An object representing the latitude and longitude for a point on the Earth’s surface.
- [mapkit.CoordinateRegion](mapkit.coordinateregion.md)
  A rectangular area on a map that a center coordinate and a span define, in degrees of latitude and longitude.
- [mapkit.CoordinateSpan](mapkit.coordinatespan.md)
  The width and height of a map region.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/mapkit.boundingregion)*