# addOverlay(_:)

**Framework**: MapKit  
**Kind**: method

Adds a single overlay object to the map.

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
func addOverlay(_ overlay: any MKOverlay)
```

#### Discussion

The map view adds the specified object to the group of overlay objects in the [`MKOverlayLevel.aboveLabels`](mkoverlaylevel/abovelabels.md) level. Adding an overlay causes the map view to begin monitoring the area that the overlay represents. As soon as the bounding rectangle of an overlay intersects the visible portion of the map, the map view adds a corresponding overlay view to the map. Implement the [`mapView(_:rendererFor:)`](mkmapviewdelegate/mapview(_:rendererfor:).md) method of the map view’s delegate object to provide the overlay view.

To remove an overlay from a map, use the [`removeOverlay(_:)`](mkmapview/removeoverlay(_:).md) method.

## Parameters

- `overlay`: The overlay object to add. This object needs to conform to the   protocol.

## See Also

- [func removeOverlay(any MKOverlay)](mkmapview/removeoverlay(_:).md)
  Removes a single overlay object from the map.
- [func removeOverlays([any MKOverlay])](mkmapview/removeoverlays(_:).md)
  Removes one or more overlay objects from the map.
- [func addOverlay(any MKOverlay, level: MKOverlayLevel)](mkmapview/addoverlay(_:level:).md)
  Adds the overlay object to the map at the specified level.
- [func addOverlays([any MKOverlay], level: MKOverlayLevel)](mkmapview/addoverlays(_:level:).md)
  Adds an array of overlay objects to the map at the specified level.
- [func addOverlays([any MKOverlay])](mkmapview/addoverlays(_:).md)
  Adds an array of overlay objects to the map.
- [func insertOverlay(any MKOverlay, at: Int, level: MKOverlayLevel)](mkmapview/insertoverlay(_:at:level:).md)
  Inserts an overlay object into the level at the specified index.
- [func insertOverlay(any MKOverlay, at: Int)](mkmapview/insertoverlay(_:at:).md)
  Inserts an overlay object into the list associated with the map.
- [func insertOverlay(any MKOverlay, above: any MKOverlay)](mkmapview/insertoverlay(_:above:).md)
  Inserts one overlay object above another.
- [func insertOverlay(any MKOverlay, below: any MKOverlay)](mkmapview/insertoverlay(_:below:).md)
  Inserts one overlay object below another.
- [func exchangeOverlay(any MKOverlay, with: any MKOverlay)](mkmapview/exchangeoverlay(_:with:).md)
  Exchanges the positions of two overlay objects.
- [func exchangeOverlay(at: Int, withOverlayAt: Int)](mkmapview/exchangeoverlay(at:withoverlayat:).md)
  Exchanges the position of two overlay objects at the specified index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkmapview/addoverlay(_:))*