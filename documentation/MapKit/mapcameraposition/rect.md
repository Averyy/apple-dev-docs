# rect

**Framework**: MapKit  
**Kind**: property

The position that frames the given map rectangle.

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
var rect: MKMapRect? { get }
```

## See Also

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
- [var region: MKCoordinateRegion?](mapcameraposition/region.md)
  The coordinate region to frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mapcameraposition/rect)*