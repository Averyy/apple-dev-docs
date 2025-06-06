# exchangeOverlay(at:withOverlayAt:)

**Framework**: MapKit  
**Kind**: method

Exchanges the position of two overlay objects at the specified index.

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
func exchangeOverlay(at index1: Int, withOverlayAt index2: Int)
```

#### Discussion

If you need to exchange overlays in other map levels, use the [`exchangeOverlay(_:with:)`](mkmapview/exchangeoverlay(_:with:).md) method.

## Parameters

- `index1`: The index of an overlay in the   map level.
- `index2`: The index of another overlay in the   map level.

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
- [func exchangeOverlay(any MKOverlay, with: any MKOverlay)](mkmapview/exchangeoverlay(_:with:).md)
  Exchanges the positions of two overlay objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkmapview/exchangeoverlay(at:withoverlayat:))*