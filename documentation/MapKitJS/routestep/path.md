# path

**Framework**: MapKit JS  
**Kind**: property

An array of coordinate objects representing the path of the route segment.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
path?: Coordinate[];
```

#### Discussion

An array of [`Coordinate`](coordinate.md) objects that traces the route segment. To render the route segment on a map, set the [`points`](polylineoverlay/points.md) property of [`PolylineOverlay`](polylineoverlay.md) to this array.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/routestep/path)*