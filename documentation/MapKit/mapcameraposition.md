# MapCameraPosition

**Framework**: MapKit  
**Kind**: struct

A structure that describes how to position the map’s camera within the map.

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
struct MapCameraPosition
```

#### Overview

`MapCameraPosition` contains a variety of properties that you can use to control the semantic framings of the camera in relation to its position to the map, such as [`automatic`](mapcameraposition/automatic.md), which frames the content of the map, and the [`camera`](mapcameraposition/camera.md) property, which allows you to specify an explicit camera position.

When you pass `MapCameraPosition` as a binding to a map, the map adjusts its camera to frame the requested content, or to exactly match the camera `MapCameraPosition` specifies. If a person interacts with the [`Map`](map.md) in a way that moves the map, the map resets the position to a value that specifies [`positionedByUser`](mapcameraposition/positionedbyuser.md).

## Topics

### Creating a camera position
- [static func camera(MapCamera) -> MapCameraPosition](mapcameraposition/camera(_:).md)
  Creates a new camera position from an existing map camera you provide.
- [static func item(MKMapItem, allowsAutomaticPitch: Bool) -> MapCameraPosition](mapcameraposition/item(_:allowsautomaticpitch:).md)
  Creates a new camera position centered on a map item and automatic pitch selection you provide.
- [static func rect(MKMapRect) -> MapCameraPosition](mapcameraposition/rect(_:).md)
  Creates a new camera position with the map boundaries you provide.
- [static func region(MKCoordinateRegion) -> MapCameraPosition](mapcameraposition/region(_:).md)
  Creates a new camera position the coordinate region you provide.
- [static func userLocation(followsHeading: Bool, fallback: MapCameraPosition) -> MapCameraPosition](mapcameraposition/userlocation(followsheading:fallback:).md)
  Creates a camera position with the specific fallback position and optionally follows the user’s heading.
### Information about camera position and framing
- [static var automatic: MapCameraPosition](mapcameraposition/automatic.md)
  The position that frames the map’s content.
- [var allowsAutomaticPitch: Bool](mapcameraposition/allowsautomaticpitch.md)
  The setting that allows the map’s camera to automatically set the pitch when framing the item.
- [var camera: MapCamera?](mapcameraposition/camera.md)
  A map camera that defines the camera positioning.
- [var fallbackPosition: MapCameraPosition?](mapcameraposition/fallbackposition.md)
  The position to use if the framework hasn’t resolved the person’s location.
- [var item: MKMapItem?](mapcameraposition/item.md)
  The item the map is framing.
- [var positionedByUser: Bool](mapcameraposition/positionedbyuser.md)
  A Boolean value that indicates whether the person specified the camera position by interacting with the map.
- [var rect: MKMapRect?](mapcameraposition/rect.md)
  The position that frames the given map rectangle.
- [var region: MKCoordinateRegion?](mapcameraposition/region.md)
  The coordinate region to frame.
### Accessing information about someone’s location
- [var followsUserHeading: Bool](mapcameraposition/followsuserheading.md)
  A Boolean value that indicates whether the map is following someone’s heading.
- [var followsUserLocation: Bool](mapcameraposition/followsuserlocation.md)
  A Boolean value that indicates whether the map is following someone’s location.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)

## See Also

- [struct MapCamera](mapcamera.md)
  Defines a virtual viewpoint above the map surface.
- [struct MapCameraBounds](mapcamerabounds.md)
  Defines an optional boundary of an area within which the map’s center needs to remain.
- [struct MapCameraUpdateContext](mapcameraupdatecontext.md)
  A structure that defines additional information about the map camera.
- [struct MapCameraUpdateFrequency](mapcameraupdatefrequency.md)
  A structure that describes when the map camera updates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mapcameraposition)*