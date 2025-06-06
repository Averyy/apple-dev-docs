# view(for:)

**Framework**: MapKit  
**Kind**: method

Returns the view associated with the overlay object, if any.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+

## Declaration

```swift
@MainActor
func view(for overlay: any MKOverlay) -> MKOverlayView
```

#### Return Value

The view associated with the overlay object or `nil` if the overlay is not onscreen.

## Parameters

- `overlay`: The overlay object whose view you want.

## See Also

- [var overlays: [any MKOverlay]](mkmapview/overlays.md)
  The overlay objects associated with the map view.
- [func overlays(in: MKOverlayLevel) -> [any MKOverlay]](mkmapview/overlays(in:).md)
  Returns overlay objects in the specified level of the map.
- [func renderer(for: any MKOverlay) -> MKOverlayRenderer?](mkmapview/renderer(for:).md)
  Returns the renderer object for drawing the contents of the specified overlay object.
- [enum MKOverlayLevel](mkoverlaylevel.md)
  Constants that indicate the position of overlays relative to other content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkmapview/view(for:)-38z60)*