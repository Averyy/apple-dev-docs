# minimumZ

**Framework**: MapKit  
**Kind**: property

The minimum zoom level that the tiles of this overlay object support.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.2+
- visionOS 1.0+

## Declaration

```swift
var minimumZ: Int { get set }
```

#### Discussion

If you use different overlay objects to represent different tiles at different zoom levels, use this property to specify the minimum zoom level supported by this overlay’s tiles. At zoom level 0, tiles cover the entire world map; at zoom level 1, tiles cover 1/4 of the world; at zoom level 2, tiles cover 1/16 of the world, and so on. The map never tries to load tiles for a zoom level less than the value specified by this property.

The default value of this property is `0`.

## See Also

- [var tileSize: CGSize](mktileoverlay/tilesize.md)
  The size (in pixels) of your tile images.
- [var isGeometryFlipped: Bool](mktileoverlay/isgeometryflipped.md)
  A Boolean value that indicates the orientation of tile indexes along the y-axis.
- [var maximumZ: Int](mktileoverlay/maximumz.md)
  The maximum zoom level that the tiles of this overlay object support.
- [var canReplaceMapContent: Bool](mktileoverlay/canreplacemapcontent.md)
  A Boolean value that indicates whether the tile content is fully opaque.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mktileoverlay/minimumz)*