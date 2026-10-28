# MapKit Functions

**Framework**: MapKit  
**Role**: API Collection

The functions of the MapKit framework provide convenient ways to package map-related data structures.

## Overview

> ❗ **Important**:  In iOS 5.1 and earlier, the MapKit framework uses the Google Mobile Maps (GMM) service to provide map data. For apps that run in iOS 5.1 and earlier, use of specific classes of this framework (and their associated interfaces) is subject to the Google Mobile Maps terms of service. You can find these terms of service at [http://code.google.com/apis/maps/iphone/terms.html](http://code.google.com/apis/maps/iphone/terms.html).

## Topics

### Functions
- [init(center: CLLocationCoordinate2D, latitudinalMeters: CLLocationDistance, longitudinalMeters: CLLocationDistance)](./mkcoordinateregion/init%28center,latitudinalmeters,longitudinalmeters%29.md)
  Creates a new coordinate region from the specified coordinate and distance values.
- [init(CLLocationCoordinate2D)](./mkmappoint/init%28_%29.md)
  Creates the map point data structure that corresponds to the specified coordinate.
- [MKCoordinateRegionMake](./mkcoordinateregionmake.md)
  Creates a new coordinate region from the specified coordinate and span values.
- [MKCoordinateSpanMake](./mkcoordinatespanmake.md)
  Creates a new [`MKCoordinateSpan`](./mkcoordinatespan.md) from the specified values.
- [MKMapPointMake](./mkmappointmake.md)
  Creates a new map point structure from the specified values.
- [MKMapSizeMake](./mkmapsizemake.md)
  Creates a new map size structure from the specified values.

## See Also

### Related Documentation
- [Location and Maps Programming Guide](https://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/LocationAwarenessPG/Introduction/Introduction.html#//apple_ref/doc/uid/TP40009497)


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mapkit-functions)*