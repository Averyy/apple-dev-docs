# path

**Framework**: MapKit JS  
**Kind**: property  
**Role**: Instance Property

An array of coordinate objects representing the path of the route.

**Availability**:
- MapKit JS 5.0+ - Deprecated in 5.4

> **Deprecated**: Removed in MapKit JS 6.0.0. Use [`polyline`](./polyline.md) instead of [`path`](./path.md).

## Declaration

```
get path(): Coordinate[][];
```

## Discussion

An array of coordinates that reflect the complete path of the route, including all of its steps. To render this route on a map, set the [`points`](../polylineoverlay/points.md) property of a [`PolylineOverlay`](../polylineoverlay.md) to this array.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/route/path)*