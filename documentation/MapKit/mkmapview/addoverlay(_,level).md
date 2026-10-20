# addOverlay(_:level:)

**Framework**: MapKit  
**Kind**: method  
**Role**: Instance Method

Adds the overlay object to the map at the specified level.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.2+
- visionOS 1.0+

## Declaration

```swift
func addOverlay(_ overlay: any MKOverlay, level: MKOverlayLevel)
```

```objc
- (void) addOverlay:(id<MKOverlay>) overlay level:(MKOverlayLevel) level;
```

#### Discussion

Positioning an overlay at a specific level places that overlay’s visual representation in front of or behind other map content such as map labels and point-of-interest icons.

This method adds the specified overlay to the end of the list of overlay objects at the given level. Adding an overlay also causes the map view to begin monitoring the area they represent. As soon as the bounding rectangle of the overlay intersects the visible portion of the map, the map view calls your delegate’s [`mapView(_:rendererFor:)`](../mkmapviewdelegate/mapview%28_,rendererfor%29.md) method to get the renderer object to use when drawing the overlay.

To remove an overlay from a map, use the [`removeOverlay(_:)`](./removeoverlay%28_%29.md) method.

## Parameters

- `overlay`: The overlay object to add. This object needs to conform to the [`MKOverlay`](../mkoverlay.md) protocol.
- `level`: The map level at which to place the overlay. For a list of possible values for this parameter, see [`MKOverlayLevel`](../mkoverlaylevel.md).

## See Also

### Adding and inserting overlays
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
- [func exchangeOverlay(at: Int, withOverlayAt: Int)](./exchangeoverlay%28at,withoverlayat%29.md)
  Exchanges the position of two overlay objects at the specified index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkmapview/addoverlay(_:level:))*