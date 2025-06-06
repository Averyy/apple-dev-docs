# urlTemplate

**Framework**: MapKit JS  
**Kind**: property

A string, or callback function that returns a string, with a URL that provides the requested tile.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
attribute string|Function urlTemplate;
```

#### Discussion

MapKit JS sets the `urlTemplate` in the tile overlay constructor, and accesses or overrides it on the [`mapkit.TileOverlay`](mapkit.tileoverlay/mapkit.tileoverlay.md) object directly.

## See Also

- [data](mapkit.tileoverlay/data.md)
  A dictionary of custom properties to use with the URL template.
- [reload](mapkit.tileoverlay/reload.md)
  Reloads the tile overlay for the displayed map region with the latest data values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/mapkit.tileoverlay/urltemplate)*