# MapCameraUpdateFrequency

**Framework**: MapKit  
**Kind**: struct

A structure that describes when the map camera updates.

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
struct MapCameraUpdateFrequency
```

## Topics

### Timing of camera updates
- [static var continuous: MapCameraUpdateFrequency](mapcameraupdatefrequency/continuous.md)
  A value that indicates that all camera updates are continuous, including while interactions are taking place.
- [static var onEnd: MapCameraUpdateFrequency](mapcameraupdatefrequency/onend.md)
  A value that indicates the camera updates when map interactions are complete.

## See Also

- [struct MapCamera](mapcamera.md)
  Defines a virtual viewpoint above the map surface.
- [struct MapCameraBounds](mapcamerabounds.md)
  Defines an optional boundary of an area within which the map’s center needs to remain.
- [struct MapCameraPosition](mapcameraposition.md)
  A structure that describes how to position the map’s camera within the map.
- [struct MapCameraUpdateContext](mapcameraupdatecontext.md)
  A structure that defines additional information about the map camera.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mapcameraupdatefrequency)*