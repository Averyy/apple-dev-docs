# CameraZoomRange

**Framework**: MapKit JS  
**Kind**: class

A minimum and maximum camera distance, in meters, from the center of the map.

**Availability**:
- MapKit JS 5.23+

## Declaration

```swift
class CameraZoomRange
```

## Topics

### Defining a zoom range
- [new CameraZoomRange()](camerazoomrange/camerazoomrangeconstructor.md)
  Constructs an instance of a camera zoom range object with no minimum or maximum camera distance.
- [new CameraZoomRange(rangeParams)](camerazoomrange/camerazoomrangeconstructor1.md)
  Creates an instance of a camera zoom range object with an object literal.
- [new CameraZoomRange(min, max)](camerazoomrange/camerazoomrangeconstructor2.md)
  Creates an instance of a camera zoom range object with the specified numeric arguments that specify minimum and maximum camera distances.
- [interface CameraZoomRangeConstructorOptions](camerazoomrangeconstructoroptions.md)
  Initialization options for the camera zoom range.
### Setting minimum and maximum distances
- [minCameraDistance](camerazoomrange/mincameradistance.md)
  The minimum allowed distance of the camera from the center of the map in meters.
- [maxCameraDistance](camerazoomrange/maxcameradistance.md)
  The maximum allowed distance of the camera from the center of the map in meters.
### Instance Methods
- [copy()](camerazoomrange/copy.md)
  Returns a copy of the camera zoom region.

## See Also

- [class MapPoint](mappoint.md)
  A location, in map units, of a point on the Earth’s surface projected onto a 2D map.
- [class MapRect](maprect.md)
  A rectangular region, in map units, of a two-dimensional map projection.
- [class MapSize](mapsize.md)
  A pair of values, in map units, that define the width and height of a rectangular area of a map projection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/camerazoomrange)*