# region(_:)

**Framework**: MapKit  
**Kind**: method  
**Role**: Type Method

Creates a new camera position the coordinate region you provide.

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
static func region(_ region: MKCoordinateRegion) -> MapCameraPosition
```

## Parameters

- `region`: An [`MKCoordinateRegion`](../mkcoordinateregion.md) that describes the camera boundaries.

## See Also

### Creating a camera position
- [static func camera(MapCamera) -> MapCameraPosition](./camera%28_%29.md)
  Creates a new camera position from an existing map camera you provide.
- [static func item(MKMapItem, allowsAutomaticPitch: Bool) -> MapCameraPosition](./item%28_,allowsautomaticpitch%29.md)
  Creates a new camera position centered on a map item and automatic pitch selection you provide.
- [static func rect(MKMapRect) -> MapCameraPosition](./rect%28_%29.md)
  Creates a new camera position with the map boundaries you provide.
- [static func userLocation(followsHeading: Bool, fallback: MapCameraPosition) -> MapCameraPosition](./userlocation%28followsheading,fallback%29.md)
  Creates a camera position with the specific fallback position and optionally follows the user’s heading.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mapcameraposition/region(_:))*