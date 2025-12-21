# loadTile(at:result:)

**Framework**: MapKit  
**Kind**: method

Loads the specified tile asynchronously.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
func loadTile(at path: MKTileOverlayPath) async throws -> Data
```

#### Discussion

The default implementation of this method uses the [`url(forTilePath:)`](mktileoverlay/url(fortilepath:).md) method to retrieve the URL for the specified tile and then loads that tile into memory asynchronously using a [`URLSession`](https://developer.apple.com/documentation/Foundation/URLSession) object. The specified tile may be located either on the local file system or on a remote server. Subclasses may override this method and implement their own custom tile-loading behavior.

When a tile overlay renderer (that is, an instance of [`MKTileOverlayRenderer`](mktileoverlayrenderer.md)) needs to display tiles, it uses this method to request the data for each tile.

## Parameters

- `path`: The path structure that identifies the specific tile you want. This structure incorporates the tile’s x-y coordinate at a given zoom level and scale factor.
- `result`: The completion block to call when the tile data is available. The method can execute this block on any queue and takes the following parameters:

## See Also

- [var urlTemplate: String?](mktileoverlay/urltemplate.md)
  The template for generating tile image URLs.
- [func url(forTilePath: MKTileOverlayPath) -> URL](mktileoverlay/url(fortilepath:).md)
  Returns the URL to use to access the specified tile.
- [struct MKTileOverlayPath](mktileoverlaypath.md)
  Values that specify the path indexes for a single overlay tile.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mktileoverlay/loadtile(at:result:))*