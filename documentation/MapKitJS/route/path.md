# path

**Framework**: MapKit JS  
**Kind**: property

An array of coordinate objects representing the path of the route.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
attribute mapkit.Coordinate[][] path;
```

#### Discussion

An array of coordinates that reflect the complete path of the route, including all of its steps. To render this route on a map, set the [`points`](mapkit.polylineoverlay/points.md) property of a [`mapkit.PolylineOverlay`](mapkit.polylineoverlay/mapkit.polylineoverlay.md) to this array.

## See Also

- [polyline](route/polyline.md)
  An instance of a polyline overlay that represents the path of a route.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/route/path)*