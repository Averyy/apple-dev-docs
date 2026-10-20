# removeOverlays(_:)

**Framework**: MapKit  
**Kind**: method  
**Role**: Instance Method

Removes one or more overlay objects from the map.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.2+
- visionOS 1.0+

## Declaration

```swift
func removeOverlays(_ overlays: [any MKOverlay])
```

```objc
- (void) removeOverlays:(NSArray<id<MKOverlay>> *) overlays;
```

#### Discussion

This method removes the specified overlays regardless of which level each one is in. Removing an overlay also removes its corresponding renderer, if one is in use. The method ignores an overlay object if it isn’t associated with the map view.

## Parameters

- `overlays`: An array of objects, each of which conforms to the [`MKOverlay`](../mkoverlay.md) protocol.

## See Also

### Related Documentation
- [func addOverlay(any MKOverlay)](./addoverlay%28_%29.md)
  Adds a single overlay object to the map.
- [func addOverlays([any MKOverlay])](./addoverlays%28_%29.md)
  Adds an array of overlay objects to the map.
### Removing overlays
- [func removeOverlay(any MKOverlay)](./removeoverlay%28_%29.md)
  Removes a single overlay object from the map.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkmapview/removeoverlays(_:))*