# mapkit.MapSize

**Framework**: MapKit JS  
**Kind**: class

A pair of values, in map units, that define the width and height of a rectangular area of a map projection.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
interface mapkit.MapSize
```

#### Overview

Use a map size to represent a subset of a map projection. Map units are a value from `0` to `1` that represent an interpolated location within the height or width of the full map projection.

## Topics

### Creating a map size
- [mapkit.MapSize](mapkit.mapsize/mapkit.mapsize.md)
  Creates an object containing the width and height of a projected coordinate span.
### Defining a map size
- [height](mapkit.mapsize/height.md)
  The height of the map size in map units.
- [width](mapkit.mapsize/width.md)
  The width of the map size in map units.
### Copying and comparing map sizes
- [copy](mapkit.mapsize/copy.md)
  Returns a copy of the map size object.
- [equals](mapkit.mapsize/equals.md)
  Compares the sizes of two maps and indicates whether they’re of equal value.

## See Also

- [mapkit.MapPoint](mapkit.mappoint.md)
  A location, in map units, of a point on the Earth’s surface projected onto a 2D map.
- [mapkit.MapRect](mapkit.maprect.md)
  A rectangular region, in map units, of a two-dimensional map projection.
- [mapkit.CameraZoomRange](mapkit.camerazoomrange.md)
  A minimum and maximum camera distance, in meters, from the center of the map.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/mapkit.mapsize)*