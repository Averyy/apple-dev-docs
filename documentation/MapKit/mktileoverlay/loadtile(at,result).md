# loadTile(at:result:)

**Framework**: MapKit  
**Kind**: method  
**Role**: Instance Method

Loads the specified tile asynchronously.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS

## Declaration

```swift
func loadTile(at path: MKTileOverlayPath, result: @escaping @Sendable (Data?, (any Error)?) -> Void)
```

```swift
func loadTile(at path: MKTileOverlayPath) async throws -> Data
```

```objc
- (void) loadTileAtPath:(MKTileOverlayPath) path result:(void (^)(NSData *tileData, NSError *error)) result;
```

## Discussion

The default implementation of this method uses the [`url(forTilePath:)`](./url%28fortilepath%29.md) method to retrieve the URL for the specified tile and then loads that tile into memory asynchronously using a [`URLSession`](../../Foundation/urlsession.md) object. The specified tile may be located either on the local file system or on a remote server. Subclasses may override this method and implement their own custom tile-loading behavior.

When a tile overlay renderer (that is, an instance of [`MKTileOverlayRenderer`](../mktileoverlayrenderer.md)) needs to display tiles, it uses this method to request the data for each tile.

## Parameters

- `path`: The path structure that identifies the specific tile you want. This structure incorporates the tile’s x-y coordinate at a given zoom level and scale factor.
- `result`: The completion block to call when the tile data is available. The method can execute this block on any queue and takes the following parameters:

  - The `tileData` parameter contains the raw data that loads from the corresponding image file. You can use this data to initialize an image object. If an error occurs, this parameter is `nil`.
  - The `error` parameter contains an error object if there is a problem loading the tile image. If no errors occur, this parameter is `nil`.

## See Also

### Customizing the loading of tiles
- [var urlTemplate: String?](./urltemplate.md)
  The template for generating tile image URLs.
- [func url(forTilePath: MKTileOverlayPath) -> URL](./url%28fortilepath%29.md)
  Returns the URL to use to access the specified tile.
- [struct MKTileOverlayPath](../mktileoverlaypath.md)
  Values that specify the path indexes for a single overlay tile.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mktileoverlay/loadtile(at:result:))*