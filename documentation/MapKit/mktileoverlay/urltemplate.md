# urlTemplate

**Framework**: MapKit  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (atomic, readonly, nullable) NSString * URLTemplate;
```

## Discussion

You specify this string at initialization time.

## See Also

### Related Documentation
- [init(urlTemplate: String?)](./init%28urltemplate%29-9s8h7.md)
  Creates and returns a tile overlay object using the specified tile-access template.
### Customizing the loading of tiles
- [func url(forTilePath: MKTileOverlayPath) -> URL](./url%28fortilepath%29.md)
  Returns the URL to use to access the specified tile.
- [func loadTile(at: MKTileOverlayPath, result: (Data?, (any Error)?) -> Void)](./loadtile%28at,result%29.md)
  Loads the specified tile asynchronously.
- [struct MKTileOverlayPath](../mktileoverlaypath.md)
  Values that specify the path indexes for a single overlay tile.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mktileoverlay/urltemplate)*