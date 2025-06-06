# overlays

**Framework**: MapKit  
**Kind**: property

The overlay objects associated with the map view.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.2+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var overlays: [any MKOverlay] { get }
```

#### Discussion

This property contains the union of all overlays at the different levels of the map. The objects in this array adopt the [`MKOverlay`](mkoverlay.md) protocol. If the map view has no associated no overlays, the value of this property is an empty array.

The order of the objects in this array doesn’t necessarily reflect their visual order on the map.

## See Also

- [func overlays(in: MKOverlayLevel) -> [any MKOverlay]](mkmapview/overlays(in:).md)
  Returns overlay objects in the specified level of the map.
- [func renderer(for: any MKOverlay) -> MKOverlayRenderer?](mkmapview/renderer(for:).md)
  Returns the renderer object for drawing the contents of the specified overlay object.
- [enum MKOverlayLevel](mkoverlaylevel.md)
  Constants that indicate the position of overlays relative to other content.
- [func view(for: any MKOverlay) -> MKOverlayView](mkmapview/view(for:)-38z60.md)
  Returns the view associated with the overlay object, if any.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkmapview/overlays)*