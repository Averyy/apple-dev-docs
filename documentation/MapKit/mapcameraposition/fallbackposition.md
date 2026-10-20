# fallbackPosition

**Framework**: MapKit  
**Kind**: property  
**Role**: Instance Property

The position to use if the framework hasn’t resolved the person’s location.

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
var fallbackPosition: MapCameraPosition? { get }
```

## See Also

### Information about camera position and framing
- [static var automatic: MapCameraPosition](./automatic.md)
  The position that frames the map’s content.
- [var allowsAutomaticPitch: Bool](./allowsautomaticpitch.md)
  The setting that allows the map’s camera to automatically set the pitch when framing the item.
- [var camera: MapCamera?](./camera.md)
  A map camera that defines the camera positioning.
- [var item: MKMapItem?](./item.md)
  The item the map is framing.
- [var positionedByUser: Bool](./positionedbyuser.md)
  A Boolean value that indicates whether the person specified the camera position by interacting with the map.
- [var rect: MKMapRect?](./rect.md)
  The position that frames the given map rectangle.
- [var region: MKCoordinateRegion?](./region.md)
  The coordinate region to frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mapcameraposition/fallbackposition)*