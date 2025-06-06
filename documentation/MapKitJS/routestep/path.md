# path

**Framework**: MapKit JS  
**Kind**: property

An array of coordinate objects representing the path of the route segment.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
attribute mapkit.Coordinate[] path;
```

#### Discussion

An array of [`mapkit.Coordinate`](mapkit.coordinate.md) objects that traces the route segment. To render the route segment on a map, set the [`points`](mapkit.polylineoverlay/points.md) property of [`mapkit.PolylineOverlay`](mapkit.polylineoverlay/mapkit.polylineoverlay.md) to this array.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/routestep/path)*