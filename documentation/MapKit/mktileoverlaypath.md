# MKTileOverlayPath

**Framework**: MapKit  
**Kind**: struct  
**Role**: Structure

Values that specify the path indexes for a single overlay tile.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
struct MKTileOverlayPath
```

```c
typedef struct { ... } MKTileOverlayPath;
```

## Topics

### Creating a tile overlay path
- [init()](./mktileoverlaypath/init%28%29.md)
  Creates a new tile overlay path.
- [init(x: Int, y: Int, z: Int, contentScaleFactor: CGFloat)](./mktileoverlaypath/init%28x,y,z,contentscalefactor%29.md)
  Creates a new overlay path with the specified indexes and content scale factor.
### Instance properties
- [var x: Int](./mktileoverlaypath/x.md)
  The index of the tile along the x-axis of the map.
- [var y: Int](./mktileoverlaypath/y.md)
  The index of the tile along the y-axis of the map.
- [var z: Int](./mktileoverlaypath/z.md)
  The index of the tile along the z-axis of the map.
- [var contentScaleFactor: CGFloat](./mktileoverlaypath/contentscalefactor.md)
  The tile’s intended screen scale factor.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Sendable](../Swift/sendable.md)

## See Also

### Customizing the loading of tiles
- [var urlTemplate: String?](./mktileoverlay/urltemplate.md)
  The template for generating tile image URLs.
- [func url(forTilePath: MKTileOverlayPath) -> URL](./mktileoverlay/url%28fortilepath%29.md)
  Returns the URL to use to access the specified tile.
- [func loadTile(at: MKTileOverlayPath, result: (Data?, (any Error)?) -> Void)](./mktileoverlay/loadtile%28at,result%29.md)
  Loads the specified tile asynchronously.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mktileoverlaypath)*