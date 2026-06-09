# new TileOverlay(imageForTile, options)

**Framework**: MapKit JS  
**Kind**: init

Creates a tile overlay with a URL template or image callback and style options.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
constructor(
    imageForTile: TileOverlayUrlTemplate | TileOverlayImageCallback,
    options?: TileOverlayConstructorOptions,
);
```

## Parameters

- `imageForTile`: A [`TileOverlayUrlTemplate`](tileoverlayurltemplate.md) string or URL callback, or a [`TileOverlayImageCallback`](tileoverlayimagecallback.md) that returns image sources directly. MapKit JS requests new tiles when the map zooms or pans, the display changes, or the custom [`data`](tileoverlay/data.md) properties change.
- `options`: An optional [`TileOverlayConstructorOptions`](tileoverlayconstructoroptions.md) object literal of properties for initializing the tile overlay.

## See Also

- [interface TileOverlayConstructorOptions](tileoverlayconstructoroptions.md)
  Attributes for initializing a tile overlay, including minimum and maximum zoom, opacity, and custom data.
- [type TileOverlayUrlTemplate](tileoverlayurltemplate.md)
  A type that specifies the URL template for a tile overlay.
- [type TileOverlayImageCallback](tileoverlayimagecallback.md)
  A callback function that provides tile images for a tile overlay.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/tileoverlay/tileoverlayconstructor)*