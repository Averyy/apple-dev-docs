# init(coordinates:contourStyle:)

**Framework**: MapKit  
**Kind**: init  
**Role**: Initializer

Creates a polyline that traces a path between the given coordinates using the specifed contour style.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS
- watchOS 10.0+

## Declaration

```swift
init(coordinates: [CLLocationCoordinate2D], contourStyle: MapPolyline.ContourStyle = .straight)
```

## Parameters

- `coordinates`: The coordinates to trace the path between.
- `contourStyle`: The [`MapPolyline.ContourStyle`](./contourstyle.md) to use.

## See Also

### Creating a polyline
- [init(MKPolyline)](./init%28_%29-93u7w.md)
  Creates a polyline from polyline you provide.
- [init(MKRoute)](./init%28_%29-5p2kx.md)
  Creates a polyline that traces the route you provide.
- [init(points: [MKMapPoint], contourStyle: MapPolyline.ContourStyle)](./init%28points,contourstyle%29.md)
  Creates a new polyline that traces a path between the provided points using the specifed contour style.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mappolyline/init(coordinates:contourstyle:))*