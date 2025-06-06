# url(forTilePath:)

**Framework**: MapKit  
**Kind**: method

Returns the URL to use to access the specified tile.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
func url(forTilePath path: MKTileOverlayPath) -> URL
```

#### Return Value

The URL to use to retrieve the tile.

#### Discussion

The default implementation of this method uses the template string you provide at initialization time to build a URL to the specified tile image. Subclasses can override this method and use a different scheme to provide URLs for tiles. You can locate the tiles either on a local file system or on a remote server.

## Parameters

- `path`: The path structure that identifies the specific tile you want. This structure incorporates the tile’s x-y coordinate at a given zoom level and scale factor.

## See Also

- [init(urlTemplate: String?)](mktileoverlay/init(urltemplate:).md)
  Creates and returns a tile overlay object using the specified tile-access template.
- [var urlTemplate: String?](mktileoverlay/urltemplate.md)
  The template for generating tile image URLs.
- [func loadTile(at: MKTileOverlayPath, result: (Data?, (any Error)?) -> Void)](mktileoverlay/loadtile(at:result:).md)
  Loads the specified tile asynchronously.
- [struct MKTileOverlayPath](mktileoverlaypath.md)
  Values that specify the path indexes for a single overlay tile.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mktileoverlay/url(fortilepath:))*