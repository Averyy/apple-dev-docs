# urlTemplate

**Framework**: MapKit JS  
**Kind**: property

A string, or callback function that returns a string, with a URL that provides the requested tile.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
get urlTemplate(): TileOverlayUrlTemplate;
set urlTemplate(urlTemplate: TileOverlayUrlTemplate);
```

#### Discussion

MapKit JS sets the `urlTemplate` in the tile overlay constructor, and accesses or overrides it on the [`TileOverlay`](tileoverlay.md) object directly.

## Topics

- [type TileOverlayUrlTemplate](tileoverlayurltemplate.md)
  A type that specifies the URL template for a tile overlay.

## See Also

- [data](tileoverlay/data.md)
  A dictionary of custom properties to use with the URL template.
- [reload()](tileoverlay/reload.md)
  Reloads the tile overlay for the displayed map region with the latest data values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/tileoverlay/urltemplate)*