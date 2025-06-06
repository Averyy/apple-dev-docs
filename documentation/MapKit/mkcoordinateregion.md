# MKCoordinateRegion

**Framework**: MapKit  
**Kind**: struct

A rectangular geographic region that centers around a specific latitude and longitude.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
struct MKCoordinateRegion
```

## Topics

### Creating a region
- [init()](mkcoordinateregion/init.md)
  Creates a coordinate region.
- [init(center: CLLocationCoordinate2D, latitudinalMeters: CLLocationDistance, longitudinalMeters: CLLocationDistance)](mkcoordinateregion/init(center:latitudinalmeters:longitudinalmeters:).md)
  Creates a new coordinate region from the specified coordinate and distance values.
- [init(MKMapRect)](mkcoordinateregion/init(_:).md)
  Returns the region that corresponds to the specified map rectangle.
- [init(center: CLLocationCoordinate2D, span: MKCoordinateSpan)](mkcoordinateregion/init(center:span:).md)
  Creates a coordinate region with a span around the specified center coordinate.
### Getting the region coordinates
- [var center: CLLocationCoordinate2D](mkcoordinateregion/center.md)
  The center point of the region.
- [var span: MKCoordinateSpan](mkcoordinateregion/span.md)
  The horizontal and vertical span representing the amount of map to display.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [struct MKCoordinateSpan](mkcoordinatespan.md)
  The width and height of a map region.
- [struct MKMapRect](mkmaprect.md)
  A rectangular area on a two-dimensional map projection.
- [struct MKMapPoint](mkmappoint.md)
  A point on a two-dimensional map projection.
- [struct MKMapSize](mkmapsize.md)
  Width and height information on a two-dimensional map projection.
- [class MKDistanceFormatter](mkdistanceformatter.md)
  A utility object that converts between a geographic distance and a string-based expression of that distance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkcoordinateregion)*