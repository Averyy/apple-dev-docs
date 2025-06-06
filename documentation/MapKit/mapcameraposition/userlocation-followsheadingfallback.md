# userLocation(followsHeading:fallback:)

**Framework**: MapKit  
**Kind**: method

Creates a camera position with the specific fallback position and optionally follows the user’s heading.

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
static func userLocation(followsHeading: Bool = false, fallback: MapCameraPosition) -> MapCameraPosition
```

#### Return Value

A new [`MapCameraPosition`](mapcameraposition.md).

## Parameters

- `followsHeading`: A Boolean value that indicates whether the camera follows the person’s heading.
- `fallback`: A fallback position to use if the map hasn’t resolved the person’s location.

## See Also

- [static func camera(MapCamera) -> MapCameraPosition](mapcameraposition/camera(_:).md)
  Creates a new camera position from an existing map camera you provide.
- [static func item(MKMapItem, allowsAutomaticPitch: Bool) -> MapCameraPosition](mapcameraposition/item(_:allowsautomaticpitch:).md)
  Creates a new camera position centered on a map item and automatic pitch selection you provide.
- [static func rect(MKMapRect) -> MapCameraPosition](mapcameraposition/rect(_:).md)
  Creates a new camera position with the map boundaries you provide.
- [static func region(MKCoordinateRegion) -> MapCameraPosition](mapcameraposition/region(_:).md)
  Creates a new camera position the coordinate region you provide.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mapcameraposition/userlocation(followsheading:fallback:))*