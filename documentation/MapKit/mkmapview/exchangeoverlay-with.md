# exchangeOverlay(_:with:)

**Framework**: MapKit  
**Kind**: method

Exchanges the positions of two overlay objects.

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
func exchangeOverlay(_ overlay1: any MKOverlay, with overlay2: any MKOverlay)
```

#### Discussion

If the overlays are in the same map level, they exchange positions within that level’s array of overlay objects. If they’re in different map levels, the two objects also swap levels. Swapping the position of the overlays affects their visibility in the map view.

## Parameters

- `overlay1`: The first overlay object.
- `overlay2`: The second overlay object.

## See Also

- [func addOverlay(any MKOverlay, level: MKOverlayLevel)](mkmapview/addoverlay(_:level:).md)
  Adds the overlay object to the map at the specified level.
- [func addOverlays([any MKOverlay], level: MKOverlayLevel)](mkmapview/addoverlays(_:level:).md)
  Adds an array of overlay objects to the map at the specified level.
- [func addOverlay(any MKOverlay)](mkmapview/addoverlay(_:).md)
  Adds a single overlay object to the map.
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
- [func exchangeOverlay(at: Int, withOverlayAt: Int)](mkmapview/exchangeoverlay(at:withoverlayat:).md)
  Exchanges the position of two overlay objects at the specified index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkmapview/exchangeoverlay(_:with:))*