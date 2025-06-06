# renderer(for:)

**Framework**: MapKit  
**Kind**: method

Returns the renderer object for drawing the contents of the specified overlay object.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.2+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func renderer(for overlay: any MKOverlay) -> MKOverlayRenderer?
```

#### Return Value

The renderer object in use for the specified overlay or `nil` if the overlay is not onscreen.

#### Discussion

This method returns the renderer object that your map delegate provided in its [`mapView(_:rendererFor:)`](mkmapviewdelegate/mapview(_:rendererfor:).md) method.

## Parameters

- `overlay`: The overlay object whose renderer you want.

## See Also

- [var overlays: [any MKOverlay]](mkmapview/overlays.md)
  The overlay objects associated with the map view.
- [func overlays(in: MKOverlayLevel) -> [any MKOverlay]](mkmapview/overlays(in:).md)
  Returns overlay objects in the specified level of the map.
- [enum MKOverlayLevel](mkoverlaylevel.md)
  Constants that indicate the position of overlays relative to other content.
- [func view(for: any MKOverlay) -> MKOverlayView](mkmapview/view(for:)-38z60.md)
  Returns the view associated with the overlay object, if any.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkmapview/renderer(for:))*