# MKTileOverlay

**Framework**: MapKit  
**Kind**: class

An overlay that covers an area of the map with tiles of bitmap images.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.2+
- visionOS 1.0+

## Declaration

```swift
class MKTileOverlay
```

#### Overview

You use tile overlay objects to represent your own tile-based content and to coordinate the display of that content in a map view. Your tiles can supplement the underlying map content or replace it completely. A tile overlay object coordinates the loading and management of the tiles, and a corresponding [`MKTileOverlayRenderer`](mktileoverlayrenderer.md) object handles the actual drawing of the tiles on the map.

You can use a single tile overlay object to represent all of the tiles at one or more zoom levels of the map. The default tile overlay object uses a template string to build URLs so that it can locate the map tiles it needs. Each URL incorporates the x and y index of the map tile, the zoom level it’s intended for, and the scale factor corresponding to the screen resolution on which to display the tile. The default class lets you specify map tiles with indexes that start in either the upper-left corner or lower-left corner of the map. If you use a different indexing scheme for your tiles, you can also subclass and override the [`url(forTilePath:)`](mktileoverlay/url(fortilepath:).md) or [`loadTile(at:result:)`](mktileoverlay/loadtile(at:result:).md) methods to map between the requested tile and your custom indexing scheme.

## Topics

### Creating a tile overlay
- [init(urlTemplate: String?)](mktileoverlay/init(urltemplate:).md)
  Creates and returns a tile overlay object using the specified tile-access template.
### Accessing the tile attributes
- [var tileSize: CGSize](mktileoverlay/tilesize.md)
  The size (in pixels) of your tile images.
- [var isGeometryFlipped: Bool](mktileoverlay/isgeometryflipped.md)
  A Boolean value that indicates the orientation of tile indexes along the y-axis.
- [var minimumZ: Int](mktileoverlay/minimumz.md)
  The minimum zoom level that the tiles of this overlay object support.
- [var maximumZ: Int](mktileoverlay/maximumz.md)
  The maximum zoom level that the tiles of this overlay object support.
- [var canReplaceMapContent: Bool](mktileoverlay/canreplacemapcontent.md)
  A Boolean value that indicates whether the tile content is fully opaque.
### Customizing the loading of tiles
- [var urlTemplate: String?](mktileoverlay/urltemplate.md)
  The template for generating tile image URLs.
- [func url(forTilePath: MKTileOverlayPath) -> URL](mktileoverlay/url(fortilepath:).md)
  Returns the URL to use to access the specified tile.
- [func loadTile(at: MKTileOverlayPath, result: (Data?, (any Error)?) -> Void)](mktileoverlay/loadtile(at:result:).md)
  Loads the specified tile asynchronously.
- [struct MKTileOverlayPath](mktileoverlaypath.md)
  Values that specify the path indexes for a single overlay tile.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [MKAnnotation](mkannotation.md)
- [MKOverlay](mkoverlay.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class MKTileOverlayRenderer](mktileoverlayrenderer.md)
  The renderer for a tile overlay that handles the drawing of bitmap images on the map surface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mktileoverlay)*