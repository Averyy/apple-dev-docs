# TileOverlayErrorEvent

**Framework**: MapKit JS  
**Kind**: class

An event object that notifies the developer of an error that occurred while loading tiles.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
class TileOverlayErrorEvent extends MapKitEvent
```

#### Discussion

[`TileOverlay`](tileoverlay.md) dispatches a `tile-error` event when an error occurs while loading tiles.

## Topics

### Instance Properties
- [tileOverlay](tileoverlayerrorevent/tileoverlay.md)
  The tile overlay object that dispatched the tile error event.
- [tileUrl](tileoverlayerrorevent/tileurl.md)
  The URL of the tile that failed to load.

## Relationships

### Inherits From
- [MapKitEvent](mapkitevent.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/tileoverlayerrorevent)*