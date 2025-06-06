# MKCoordinateSpan

**Framework**: MapKit  
**Kind**: struct

The width and height of a map region.

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
struct MKCoordinateSpan
```

#### Overview

You use the delta values in this structure to indicate the desired zoom level of the map, with smaller delta values corresponding to a higher zoom level.

## Topics

### Creating a coordinate span
- [init()](mkcoordinatespan/init.md)
  Creates a coordinate span that represents a width and height on a map.
- [init(latitudeDelta: CLLocationDegrees, longitudeDelta: CLLocationDegrees)](mkcoordinatespan/init(latitudedelta:longitudedelta:).md)
  Creates a new [`MKCoordinateSpan`](mkcoordinatespan.md) from the specified values.
### Getting the span coordinates
- [var latitudeDelta: CLLocationDegrees](mkcoordinatespan/latitudedelta.md)
  The amount of north-to-south distance (measured in degrees) to display on the map.
- [var longitudeDelta: CLLocationDegrees](mkcoordinatespan/longitudedelta.md)
  The amount of east-to-west distance (measured in degrees) to display for the map region.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Copyable](../Swift/Copyable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [struct MKCoordinateRegion](mkcoordinateregion.md)
  A rectangular geographic region that centers around a specific latitude and longitude.
- [struct MKMapRect](mkmaprect.md)
  A rectangular area on a two-dimensional map projection.
- [struct MKMapPoint](mkmappoint.md)
  A point on a two-dimensional map projection.
- [struct MKMapSize](mkmapsize.md)
  Width and height information on a two-dimensional map projection.
- [class MKDistanceFormatter](mkdistanceformatter.md)
  A utility object that converts between a geographic distance and a string-based expression of that distance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkcoordinatespan)*