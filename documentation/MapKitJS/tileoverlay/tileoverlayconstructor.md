# new TileOverlay(urlTemplate, options)

**Framework**: MapKit JS  
**Kind**: init

Creates a tile overlay with a URL template and style options.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
constructor(
        urlTemplate: TileOverlayUrlTemplate,
        options?: TileOverlayConstructorOptions,
    );
```

## Parameters

- `urlTemplate`: The   value can be in the format of a template URL string or a function that returns a URL string from a set of tile parameters. MapKit JS requests new tiles when the map zooms or pans, the display changes, or the custom   properties change.
- `options`: An optional   object literal of properties for initializing the tile overlay.

## See Also

- [interface TileOverlayConstructorOptions](tileoverlayconstructoroptions.md)
  Attributes for initializing a tile overlay, including minimum and maximum zoom, opacity, and custom data.
- [type TileOverlayUrlTemplate](tileoverlayurltemplate.md)
  A type that specifies the URL template for a tile overlay.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/tileoverlay/tileoverlayconstructor)*