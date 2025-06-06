# mapkit.CoordinateRegion

**Framework**: MapKit JS  
**Kind**: class

A rectangular area on a map that a center coordinate and a span define, in degrees of latitude and longitude.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
interface mapkit.CoordinateRegion
```

## Mentions

- [MapKit JS 5](mapkit-js-5.md)

## Topics

### Creating a coordinate region
- [mapkit.CoordinateRegion](mapkit.coordinateregion/mapkit.coordinateregion.md)
  A rectangular geographic region that centers around a latitude and longitude coordinate.
### Defining the region
- [center](mapkit.coordinateregion/center.md)
  The center point of the region.
- [span](mapkit.coordinateregion/span.md)
  The horizontal and vertical span representing the amount of map to display.
### Inspecting the region
- [radius](mapkit.coordinateregion/radius.md)
  The distance provided in meters or the longest distance derived from the center point to the region’s bounding box.
### Comparing, copying, and converting regions
- [copy](mapkit.coordinateregion/copy.md)
  Returns a copy of the calling coordinate region.
- [equals](mapkit.coordinateregion/equals.md)
  Returns a Boolean value indicating whether two regions are equal.
- [toBoundingRegion](mapkit.coordinateregion/toboundingregion.md)
  Returns the bounding region that corresponds to the specified coordinate region.
- [toMapRect](mapkit.coordinateregion/tomaprect.md)
  Returns the map rectangle that corresponds to the calling coordinate region.

## See Also

- [mapkit.Coordinate](mapkit.coordinate.md)
  An object representing the latitude and longitude for a point on the Earth’s surface.
- [mapkit.CoordinateSpan](mapkit.coordinatespan.md)
  The width and height of a map region.
- [mapkit.BoundingRegion](mapkit.boundingregion.md)
  A rectangular area on a map, which coordinates of the rectangle’s northeast and southwest corners define.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/mapkit.coordinateregion)*