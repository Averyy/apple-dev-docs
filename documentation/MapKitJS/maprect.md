# MapRect

**Framework**: MapKit JS  
**Kind**: class

A rectangular region, in map units, of a two-dimensional map projection.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
class MapRect
```

#### Overview

Use a `mapkit.MapRect` to represent a rectangular region within a map projection. Map units are a value from `0` to `1` that represent an interpolated location within the height or width of the full map projection.

## Topics

### Creating a map rectangle
- [new MapRect(x, y, width, height)](maprect/maprectconstructor.md)
  Creates an object that represents a rectangular region of the map projection.
### Defining a map rectangle
- [origin](maprect/origin.md)
  The origin point of a rectangle.
- [size](maprect/size.md)
  The width and height of a rectangle, starting from the origin point.
### Obtaining rectangle metrics
- [maxX()](maprect/maxx.md)
  Returns the maximum x-axis value of a rectangle.
- [maxY()](maprect/maxy.md)
  Returns the maximum y-axis value of a rectangle.
- [midX()](maprect/midx.md)
  Returns the midpoint along the x-axis of a rectangle.
- [midY()](maprect/midy.md)
  Returns the midpoint along the y-axis of a rectangle.
- [minX()](maprect/minx.md)
  Returns the minimum x-axis value of a rectangle.
- [minY()](maprect/miny.md)
  Returns the minimum y-axis value of a rectangle.
### Working with map rectangles
- [copy()](maprect/copy.md)
  Returns a copy of a map rectangle.
- [equals(anotherRect)](maprect/equals.md)
  Compares whether two map rectangles are equal.
- [scale(scaleFactor, scaleCenter)](maprect/scale.md)
  Returns a scaled map rectangle for a map location.
- [toCoordinateRegion()](maprect/tocoordinateregion.md)
  Returns the region that corresponds to a map rectangle.
### Instance Methods
- [toString()](maprect/tostring.md)
  Returns a string representation of the map rectangle object.

## See Also

- [class MapPoint](mappoint.md)
  A location, in map units, of a point on the Earth’s surface projected onto a 2D map.
- [class MapSize](mapsize.md)
  A pair of values, in map units, that define the width and height of a rectangular area of a map projection.
- [class CameraZoomRange](camerazoomrange.md)
  A minimum and maximum camera distance, in meters, from the center of the map.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/maprect)*