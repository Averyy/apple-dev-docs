# insertOverlay(_:at:)

**Framework**: MapKit  
**Kind**: method  
**Role**: Instance Method

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
func insertOverlay(_ overlay: any MKOverlay, at index: Int)
```

```objc
- (void) insertOverlay:(id<MKOverlay>) overlay atIndex:(NSUInteger) index;
```

## Discussion

This method inserts the overlay into the [`MKOverlayLevel.aboveLabels`](../mkoverlaylevel/abovelabels.md) level.

## Parameters

- `overlay`: The overlay object to insert.
- `index`: The index at which to insert the overlay object. If this value is greater than the number of objects in the [`overlays`](./overlays.md) property, this method appends the object to the end of the array.

## See Also

### Adding and inserting overlays
- [func addOverlay(any MKOverlay, level: MKOverlayLevel)](./addoverlay%28_,level%29.md)
  Adds the overlay object to the map at the specified level.
- [func addOverlays([any MKOverlay], level: MKOverlayLevel)](./addoverlays%28_,level%29.md)
  Adds an array of overlay objects to the map at the specified level.
- [func addOverlay(any MKOverlay)](./addoverlay%28_%29.md)
  Adds a single overlay object to the map.
- [func addOverlays([any MKOverlay])](./addoverlays%28_%29.md)
  Adds an array of overlay objects to the map.
- [func insertOverlay(any MKOverlay, at: Int, level: MKOverlayLevel)](./insertoverlay%28_,at,level%29.md)
  Inserts an overlay object into the level at the specified index.
- [func insertOverlay(any MKOverlay, above: any MKOverlay)](./insertoverlay%28_,above%29.md)
  Inserts one overlay object above another.
- [func insertOverlay(any MKOverlay, below: any MKOverlay)](./insertoverlay%28_,below%29.md)
  Inserts one overlay object below another.
- [func exchangeOverlay(any MKOverlay, with: any MKOverlay)](./exchangeoverlay%28_,with%29.md)
  Exchanges the positions of two overlay objects.
- [func exchangeOverlay(at: Int, withOverlayAt: Int)](./exchangeoverlay%28at,withoverlayat%29.md)
  Exchanges the position of two overlay objects at the specified index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkmapview/insertoverlay(_:at:))*