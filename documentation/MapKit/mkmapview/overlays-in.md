# overlays(in:)

**Framework**: MapKit  
**Kind**: method

Returns overlay objects in the specified level of the map.

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
func overlays(in level: MKOverlayLevel) -> [any MKOverlay]
```

#### Return Value

An array of objects conforming to the [`MKOverlay`](mkoverlay.md) protocol that display in the specified map level. If there are no overlays at the specified level, this method returns an empty array.

#### Discussion

You can use this method to get all of the overlays assigned to a specific map level, which might be a subset of the complete set of overlay objects. For overlapping overlay objects, the order of objects in the array represents their visual order when displayed on the map, with objects in the beginning of the array located behind those at later indexes.

## Parameters

- `level`: The map level whose overlays you want. For a list of possible values for this parameter, see  .

## See Also

- [func addOverlays([any MKOverlay], level: MKOverlayLevel)](mkmapview/addoverlays(_:level:).md)
  Adds an array of overlay objects to the map at the specified level.
- [func addOverlay(any MKOverlay, level: MKOverlayLevel)](mkmapview/addoverlay(_:level:).md)
  Adds the overlay object to the map at the specified level.
- [var overlays: [any MKOverlay]](mkmapview/overlays.md)
  The overlay objects associated with the map view.
- [func renderer(for: any MKOverlay) -> MKOverlayRenderer?](mkmapview/renderer(for:).md)
  Returns the renderer object for drawing the contents of the specified overlay object.
- [enum MKOverlayLevel](mkoverlaylevel.md)
  Constants that indicate the position of overlays relative to other content.
- [func view(for: any MKOverlay) -> MKOverlayView](mkmapview/view(for:)-38z60.md)
  Returns the view associated with the overlay object, if any.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkmapview/overlays(in:))*