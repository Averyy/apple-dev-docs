# addOverlay(_:)

**Framework**: MapKit  
**Kind**: method  
**Role**: Instance Method

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
func addOverlay(_ overlay: any MKOverlay)
```

```objc
- (void) addOverlay:(id<MKOverlay>) overlay;
```

## Discussion

The map view adds the specified object to the group of overlay objects in the [`MKOverlayLevel.aboveLabels`](../mkoverlaylevel/abovelabels.md) level. Adding an overlay causes the map view to begin monitoring the area that the overlay represents. As soon as the bounding rectangle of an overlay intersects the visible portion of the map, the map view adds a corresponding overlay view to the map. Implement the [`mapView(_:rendererFor:)`](../mkmapviewdelegate/mapview%28_,rendererfor%29.md) method of the map view’s delegate object to provide the overlay view.

To remove an overlay from a map, use the [`removeOverlay(_:)`](./removeoverlay%28_%29.md) method.

## Parameters

- `overlay`: The overlay object to add. This object needs to conform to the [`MKOverlay`](../mkoverlay.md) protocol.

## See Also

### Related Documentation
- [func removeOverlay(any MKOverlay)](./removeoverlay%28_%29.md)
  Removes a single overlay object from the map.
- [func removeOverlays([any MKOverlay])](./removeoverlays%28_%29.md)
  Removes one or more overlay objects from the map.
### Adding and inserting overlays
- [func addOverlay(any MKOverlay, level: MKOverlayLevel)](./addoverlay%28_,level%29.md)
  Adds the overlay object to the map at the specified level.
- [func addOverlays([any MKOverlay], level: MKOverlayLevel)](./addoverlays%28_,level%29.md)
  Adds an array of overlay objects to the map at the specified level.
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
- [func exchangeOverlay(at: Int, withOverlayAt: Int)](./exchangeoverlay%28at,withoverlayat%29.md)
  Exchanges the position of two overlay objects at the specified index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkmapview/addoverlay(_:))*