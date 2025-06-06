# insertOverlay(_:at:)

**Framework**: MapKit  
**Kind**: method

Inserts an overlay object into the list associated with the map.

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
func insertOverlay(_ overlay: any MKOverlay, at index: Int)
```

#### Discussion

This method inserts the overlay into the [`MKOverlayLevel.aboveLabels`](mkoverlaylevel/abovelabels.md) level.

## Parameters

- `overlay`: The overlay object to insert.
- `index`: The index at which to insert the overlay object. If this value is greater than the number of objects in the   property, this method appends the object to the end of the array.

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
- [func insertOverlay(any MKOverlay, above: any MKOverlay)](mkmapview/insertoverlay(_:above:).md)
  Inserts one overlay object above another.
- [func insertOverlay(any MKOverlay, below: any MKOverlay)](mkmapview/insertoverlay(_:below:).md)
  Inserts one overlay object below another.
- [func exchangeOverlay(any MKOverlay, with: any MKOverlay)](mkmapview/exchangeoverlay(_:with:).md)
  Exchanges the positions of two overlay objects.
- [func exchangeOverlay(at: Int, withOverlayAt: Int)](mkmapview/exchangeoverlay(at:withoverlayat:).md)
  Exchanges the position of two overlay objects at the specified index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkmapview/insertoverlay(_:at:))*