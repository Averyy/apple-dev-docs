# mapkit.MapRect

**Framework**: MapKit JS  
**Kind**: class

A rectangular region, in map units, of a two-dimensional map projection.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
interface mapkit.MapRect
```

#### Overview

Use a `mapkit.MapRect` to represent a rectangular region within a map projection. Map units are a value from `0` to `1` that represent an interpolated location within the height or width of the full map projection.

## Topics

### Creating a map rectangle
- [mapkit.MapRect](mapkit.maprect/mapkit.maprect.md)
  Creates an object that represents a rectangular region of the map projection.
### Defining a map rectangle
- [origin](mapkit.maprect/origin.md)
  The origin point of a rectangle.
- [size](mapkit.maprect/size.md)
  The width and height of a rectangle, starting from the origin point.
### Obtaining rectangle metrics
- [maxX](mapkit.maprect/maxx.md)
  Returns the maximum x-axis value of a rectangle.
- [maxY](mapkit.maprect/maxy.md)
  Returns the maximum y-axis value of a rectangle.
- [midX](mapkit.maprect/midx.md)
  Returns the midpoint along the x-axis of a rectangle.
- [midY](mapkit.maprect/midy.md)
  Returns the midpoint along the y-axis of a rectangle.
- [minX](mapkit.maprect/minx.md)
  Returns the minimum x-axis value of a rectangle.
- [minY](mapkit.maprect/miny.md)
  Returns the minimum y-axis value of a rectangle.
### Working with map rectangles
- [copy](mapkit.maprect/copy.md)
  Returns a copy of a map rectangle.
- [equals](mapkit.maprect/equals.md)
  Compares whether two map rectangles are equal.
- [scale](mapkit.maprect/scale.md)
  Returns a scaled map rectangle for a map location.
- [toCoordinateRegion](mapkit.maprect/tocoordinateregion.md)
  Returns the region that corresponds to a map rectangle.

## See Also

- [mapkit.MapPoint](mapkit.mappoint.md)
  A location, in map units, of a point on the Earth’s surface projected onto a 2D map.
- [mapkit.MapSize](mapkit.mapsize.md)
  A pair of values, in map units, that define the width and height of a rectangular area of a map projection.
- [mapkit.CameraZoomRange](mapkit.camerazoomrange.md)
  A minimum and maximum camera distance, in meters, from the center of the map.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/mapkit.maprect)*