# MapCameraBounds

**Framework**: MapKit  
**Kind**: struct

Defines an optional boundary of an area within which the map’s center needs to remain.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst ?+
- macOS 14.0+
- tvOS 17.0+
- visionOS ?+
- watchOS 10.0+

## Declaration

```swift
struct MapCameraBounds
```

#### Overview

Using the `MapCameraBounds` initializers you can also define an optional camera zoom range that limits the distances that a person can zoom the map camera to.

## Topics

### Creating a map camera bounds
- [init(centerCoordinateBounds: MKCoordinateRegion, minimumDistance: Double?, maximumDistance: Double?)](mapcamerabounds/init(centercoordinatebounds:minimumdistance:maximumdistance:)-97kis.md)
  Creates a camera bounds with the specified region boundary and zoom ranges.
- [init(centerCoordinateBounds: MKMapRect, minimumDistance: Double?, maximumDistance: Double?)](mapcamerabounds/init(centercoordinatebounds:minimumdistance:maximumdistance:)-27z4p.md)
  Creates a camera bounds with the specified map rectangle boundary and zoom ranges.
- [init(minimumDistance: Double?, maximumDistance: Double?)](mapcamerabounds/init(minimumdistance:maximumdistance:).md)
  Creates a camera bounds with the zoom ranges you specify.

## See Also

- [struct MapCamera](mapcamera.md)
  Defines a virtual viewpoint above the map surface.
- [struct MapCameraPosition](mapcameraposition.md)
  A structure that describes how to position the map’s camera within the map.
- [struct MapCameraUpdateContext](mapcameraupdatecontext.md)
  A structure that defines additional information about the map camera.
- [struct MapCameraUpdateFrequency](mapcameraupdatefrequency.md)
  A structure that describes when the map camera updates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mapcamerabounds)*