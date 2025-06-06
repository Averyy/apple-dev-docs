# urlTemplate

**Framework**: MapKit  
**Kind**: property

The template for generating tile image URLs.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.2+
- visionOS 1.0+

## Declaration

```swift
var urlTemplate: String? { get }
```

#### Discussion

You specify this string at initialization time.

## See Also

- [init(urlTemplate: String?)](mktileoverlay/init(urltemplate:).md)
  Creates and returns a tile overlay object using the specified tile-access template.
- [func url(forTilePath: MKTileOverlayPath) -> URL](mktileoverlay/url(fortilepath:).md)
  Returns the URL to use to access the specified tile.
- [func loadTile(at: MKTileOverlayPath, result: (Data?, (any Error)?) -> Void)](mktileoverlay/loadtile(at:result:).md)
  Loads the specified tile asynchronously.
- [struct MKTileOverlayPath](mktileoverlaypath.md)
  Values that specify the path indexes for a single overlay tile.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mktileoverlay/urltemplate)*