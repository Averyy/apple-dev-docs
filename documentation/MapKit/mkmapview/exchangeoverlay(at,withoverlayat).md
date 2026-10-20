# exchangeOverlay(at:withOverlayAt:)

**Framework**: MapKit  
**Kind**: method  
**Role**: Instance Method

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
func exchangeOverlay(at index1: Int, withOverlayAt index2: Int)
```

```objc
- (void) exchangeOverlayAtIndex:(NSUInteger) index1 withOverlayAtIndex:(NSUInteger) index2;
```

#### Discussion

If you need to exchange overlays in other map levels, use the [`exchangeOverlay(_:with:)`](./exchangeoverlay%28_,with%29.md) method.

## Parameters

- `index1`: The index of an overlay in the [`MKOverlayLevel.aboveLabels`](../mkoverlaylevel/abovelabels.md) map level.
- `index2`: The index of another overlay in the [`MKOverlayLevel.aboveLabels`](../mkoverlaylevel/abovelabels.md) map level.

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
- [func insertOverlay(any MKOverlay, at: Int)](./insertoverlay%28_,at%29.md)
  Inserts an overlay object into the list associated with the map.
- [func insertOverlay(any MKOverlay, above: any MKOverlay)](./insertoverlay%28_,above%29.md)
  Inserts one overlay object above another.
- [func insertOverlay(any MKOverlay, below: any MKOverlay)](./insertoverlay%28_,below%29.md)
  Inserts one overlay object below another.
- [func exchangeOverlay(any MKOverlay, with: any MKOverlay)](./exchangeoverlay%28_,with%29.md)
  Exchanges the positions of two overlay objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkmapview/exchangeoverlay(at:withoverlayat:))*