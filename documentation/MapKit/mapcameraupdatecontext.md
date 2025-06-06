# MapCameraUpdateContext

**Framework**: MapKit  
**Kind**: struct

A structure that defines additional information about the map camera.

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
struct MapCameraUpdateContext
```

## Topics

### Accessing information about the camera
- [let camera: MapCamera](mapcameraupdatecontext/camera.md)
  The current map camera.
- [let rect: MKMapRect](mapcameraupdatecontext/rect.md)
  A map rectangle that approximates the view of the map’s camera.
- [let region: MKCoordinateRegion](mapcameraupdatecontext/region.md)
  A map region that approximates the view of the map’s camera.

## See Also

- [struct MapCamera](mapcamera.md)
  Defines a virtual viewpoint above the map surface.
- [struct MapCameraBounds](mapcamerabounds.md)
  Defines an optional boundary of an area within which the map’s center needs to remain.
- [struct MapCameraPosition](mapcameraposition.md)
  A structure that describes how to position the map’s camera within the map.
- [struct MapCameraUpdateFrequency](mapcameraupdatefrequency.md)
  A structure that describes when the map camera updates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mapcameraupdatecontext)*