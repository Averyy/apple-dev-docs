# overlays(in:)

**Framework**: MapKit  
**Kind**: method  
**Role**: Instance Method

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
func overlays(in level: MKOverlayLevel) -> [any MKOverlay]
```

```objc
- (NSArray<id<MKOverlay>> *) overlaysInLevel:(MKOverlayLevel) level;
```

## Return Value

An array of objects conforming to the [`MKOverlay`](../mkoverlay.md) protocol that display in the specified map level. If there are no overlays at the specified level, this method returns an empty array.

## Discussion

You can use this method to get all of the overlays assigned to a specific map level, which might be a subset of the complete set of overlay objects. For overlapping overlay objects, the order of objects in the array represents their visual order when displayed on the map, with objects in the beginning of the array located behind those at later indexes.

## Parameters

- `level`: The map level whose overlays you want. For a list of possible values for this parameter, see [`MKOverlayLevel`](../mkoverlaylevel.md).

## See Also

### Related Documentation
- [func addOverlays([any MKOverlay], level: MKOverlayLevel)](./addoverlays%28_,level%29.md)
  Adds an array of overlay objects to the map at the specified level.
- [func addOverlay(any MKOverlay, level: MKOverlayLevel)](./addoverlay%28_,level%29.md)
  Adds the overlay object to the map at the specified level.
### Accessing overlays
- [var overlays: [any MKOverlay]](./overlays.md)
  The overlay objects associated with the map view.
- [func renderer(for: any MKOverlay) -> MKOverlayRenderer?](./renderer%28for%29.md)
  Returns the renderer object for drawing the contents of the specified overlay object.
- [enum MKOverlayLevel](../mkoverlaylevel.md)
  Constants that indicate the position of overlays relative to other content.
- [func view(for: any MKOverlay) -> MKOverlayView](./view%28for%29-38z60.md)
  Returns the view associated with the overlay object, if any.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkmapview/overlays(in:))*