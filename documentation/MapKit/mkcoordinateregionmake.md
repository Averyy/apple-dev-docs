# MKCoordinateRegionMake

**Framework**: MapKit  
**Kind**: func  
**Role**: Function

Creates a new coordinate region from the specified coordinate and span values.

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
static MKCoordinateRegion MKCoordinateRegionMake(CLLocationCoordinate2D centerCoordinate, MKCoordinateSpan span);
```

## Return Value

A region with the specified values.

## Parameters

- `centerCoordinate`: The center point of the region.
- `span`: The horizontal and vertical span representing the amount of map to display. The size of the span also reflects the current zoom level.

## See Also

### Functions
- [init(center: CLLocationCoordinate2D, latitudinalMeters: CLLocationDistance, longitudinalMeters: CLLocationDistance)](./mkcoordinateregion/init%28center,latitudinalmeters,longitudinalmeters%29.md)
  Creates a new coordinate region from the specified coordinate and distance values.
- [MKCoordinateSpanMake](./mkcoordinatespanmake.md)
  Creates a new [`MKCoordinateSpan`](./mkcoordinatespan.md) from the specified values.
- [init(CLLocationCoordinate2D)](./mkmappoint/init%28_%29.md)
  Creates the map point data structure that corresponds to the specified coordinate.
- [MKMapPointMake](./mkmappointmake.md)
  Creates a new map point structure from the specified values.
- [MKMapSizeMake](./mkmapsizemake.md)
  Creates a new map size structure from the specified values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkcoordinateregionmake)*