# imageForTile

**Framework**: MapKit JS  
**Kind**: property

A string, or callback function, that provides the requested tile.

**Availability**:
- MapKit JS 6.0+

## Declaration

```swift
get imageForTile(): TileOverlayUrlTemplate | TileOverlayImageCallback;
set imageForTile(
    imageForTile: TileOverlayUrlTemplate | TileOverlayImageCallback,
);
```

## Mentions

- [MapKit JS 6](mapkit-js-6.md)
- [Migrating from Version 5 to Version 6](migrating-from-version-5-to-version-6.md)

#### Discussion

Set this property to a [`TileOverlayUrlTemplate`](tileoverlayurltemplate.md) to provide tiles by URL, or a [`TileOverlayImageCallback`](tileoverlayimagecallback.md) to provide tiles as image sources directly.

MapKit JS sets `imageForTile` in the tile overlay constructor, and accesses or overrides it on the [`TileOverlay`](tileoverlay.md) object directly.

## Topics

- [type TileOverlayUrlTemplate](tileoverlayurltemplate.md)
  A type that specifies the URL template for a tile overlay.
- [type TileOverlayImageCallback](tileoverlayimagecallback.md)
  A callback function that provides tile images for a tile overlay.

## See Also

- [data](tileoverlay/data.md)
  A dictionary of custom properties to use with the URL template.
- [reload()](tileoverlay/reload.md)
  Reloads the tile overlay for the displayed map region with the latest data values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/tileoverlay/imagefortile)*