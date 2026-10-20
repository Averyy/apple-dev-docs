# exchangeOverlay(_:with:)

**Framework**: MapKit  
**Kind**: method  
**Role**: Instance Method

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
func exchangeOverlay(_ overlay1: any MKOverlay, with overlay2: any MKOverlay)
```

```objc
- (void) exchangeOverlay:(id<MKOverlay>) overlay1 withOverlay:(id<MKOverlay>) overlay2;
```

#### Discussion

If the overlays are in the same map level, they exchange positions within that level’s array of overlay objects. If they’re in different map levels, the two objects also swap levels. Swapping the position of the overlays affects their visibility in the map view.

## Parameters

- `overlay1`: The first overlay object.
- `overlay2`: The second overlay object.

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
- [func exchangeOverlay(at: Int, withOverlayAt: Int)](./exchangeoverlay%28at,withoverlayat%29.md)
  Exchanges the position of two overlay objects at the specified index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkmapview/exchangeoverlay(_:with:))*