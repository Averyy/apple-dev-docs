# MKMapSizeMake

**Framework**: MapKit  
**Kind**: func  
**Role**: Function

Creates a new map size structure from the specified values.

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
static MKMapSize MKMapSizeMake(double width, double height);
```

#### Return Value

A map size with the specified values.

## Parameters

- `width`: The distance (measured using map points) along the east-west axis of the map projection.
- `height`: The distance (measured using map points) along the north-south axis of the map projection.

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
- [MKMapPointMake](./mkmappointmake.md)
  Creates a new map point structure from the specified values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkmapsizemake)*