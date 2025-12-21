# MapPoint

**Framework**: MapKit JS  
**Kind**: class

A location, in map units, of a point on the Earth’s surface projected onto a 2D map.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
class MapPoint
```

#### Overview

Map units are a value from `0` to `1` that represent an interpolated location within the height or width of the full map projection. On a two-dimensional map, the upper-left corner of the map projection has the coordinate (`0,` `0`), and the lower-right corner of the map projection has the coordinate (`1,` `1`).

As another point of reference, `mapkit.MapPoint(0.5,` `0.5)` corresponds to the center of the map, which MapKit JS also represents as the coordinate `mapkit.Coordinate(0,` `0)`.

## Topics

### Creating a map point
- [new MapPoint(x, y)](mappoint/mappointconstructor.md)
  Creates a map location.
### Defining a map point
- [x](mappoint/x.md)
  The location of the map point along the map’s x-axis.
- [y](mappoint/y.md)
  The location of the map point along the map’s y-axis.
- [z](mappoint/z.md)
  The z component of a map point.
- [w](mappoint/w.md)
  The w component of a map point.
### Working with map points
- [copy()](mappoint/copy.md)
  Returns a copy of the location.
- [equals(anotherPoint)](mappoint/equals.md)
  Indicates whether two map points are equal.
- [toCoordinate()](mappoint/tocoordinate.md)
  Converts a map point into a coordinate with latitude and longitude.
### Instance Methods
- [toString()](mappoint/tostring.md)
  Returns a string representation of the map point object.

## See Also

- [class MapRect](maprect.md)
  A rectangular region, in map units, of a two-dimensional map projection.
- [class MapSize](mapsize.md)
  A pair of values, in map units, that define the width and height of a rectangular area of a map projection.
- [class CameraZoomRange](camerazoomrange.md)
  A minimum and maximum camera distance, in meters, from the center of the map.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/mappoint)*