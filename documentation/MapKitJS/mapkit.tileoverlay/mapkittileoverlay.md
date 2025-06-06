# mapkit.TileOverlay

**Framework**: MapKit JS  
**Kind**: init

Creates a tile overlay with a URL template and style options.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
new mapkit.TileOverlay(
	string|function urlTemplate,
	optional TileOverlayConstructorOptions options
);
```

## Parameters

- `urlTemplate`: The   can be in the format of a template URL string or a function that returns a URL string from a set of tile parameters. MapKit JS requests new tiles when the map zooms or pans, the display changes, or the custom   properties change.
- `options`: An optional object literal of properties for initializing the tile overlay. These properties include  ,  ,  , and  .

## See Also

- [TileOverlayConstructorOptions](tileoverlayconstructoroptions.md)
  Attributes for initializing a tile overlay, including minimum and maximum zoom, opacity, and custom data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/mapkit.tileoverlay/mapkit.tileoverlay)*