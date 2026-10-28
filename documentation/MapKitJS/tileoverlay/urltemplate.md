# urlTemplate

**Framework**: MapKit JS  
**Kind**: property  
**Role**: Instance Property

A string, or callback function, that provides the requested tile.

**Availability**:
- MapKit JS 5.0+ - Deprecated in 6.0

> **Deprecated**: Use [`imageForTile`](./imagefortile.md) instead, which supports both URL templates and [`TileOverlayImageCallback`](../tileoverlayimagecallback.md) functions.

## Declaration

```
get urlTemplate(): TileOverlayUrlTemplate | TileOverlayImageCallback;
set urlTemplate(
    urlTemplate: TileOverlayUrlTemplate | TileOverlayImageCallback,
);
```

## Discussion

MapKit JS sets the `urlTemplate` in the tile overlay constructor, and accesses or overrides it on the [`TileOverlay`](../tileoverlay.md) object directly.

## Topics

- [type TileOverlayUrlTemplate](../tileoverlayurltemplate.md)
  A type that specifies the URL template for a tile overlay.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/tileoverlay/urltemplate)*