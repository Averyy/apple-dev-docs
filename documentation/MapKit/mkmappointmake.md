# MKMapPointMake

**Framework**: MapKit  
**Kind**: func  
**Role**: Function

Creates a new map point structure from the specified values.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```c
static MKMapPoint MKMapPointMake(double x, double y);
```

## Return Value

A map point with the specified values.

## Parameters

- `x`: The point along the east-west axis of the map projection.
- `y`: The point along the north-south axis of the map projection.

## See Also

### Functions
- [MKCoordinateRegionMake](./mkcoordinateregionmake.md)
  Creates a new coordinate region from the specified coordinate and span values.
- [init(center: CLLocationCoordinate2D, latitudinalMeters: CLLocationDistance, longitudinalMeters: CLLocationDistance)](./mkcoordinateregion/init%28center,latitudinalmeters,longitudinalmeters%29.md)
  Creates a new coordinate region from the specified coordinate and distance values.
- [MKCoordinateSpanMake](./mkcoordinatespanmake.md)
  Creates a new [`MKCoordinateSpan`](./mkcoordinatespan.md) from the specified values.
- [init(CLLocationCoordinate2D)](./mkmappoint/init%28_%29.md)
  Creates the map point data structure that corresponds to the specified coordinate.
- [MKMapSizeMake](./mkmapsizemake.md)
  Creates a new map size structure from the specified values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkmappointmake)*