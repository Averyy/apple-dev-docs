# isGeometryFlipped

**Framework**: MapKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates the orientation of tile indexes along the y-axis.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.2+
- visionOS 1.0+

## Declaration

```swift
var isGeometryFlipped: Bool { get set }
```

```objc
@property (atomic, getter=isGeometryFlipped) BOOL geometryFlipped;
```

#### Discussion

When set to [`false`](../../Swift/false.md), tile indexes start in the upper-left corner of the map and proceed down and to the right. Thus, the tile at `(0, 0)`is in the upper-left corner of the map, the tile at `(1, 0)` is to its immediate right and the tile at `(0, 1)` is immediately below it. Setting this property to [`true`](../../Swift/true.md) causes the map to start indexes at the lower-left corner of the map and proceed up and to the right.

The default value of this property is [`false`](../../Swift/false.md).

## See Also

### Accessing the tile attributes
- [var tileSize: CGSize](./tilesize.md)
  The size (in pixels) of your tile images.
- [var minimumZ: Int](./minimumz.md)
  The minimum zoom level that the tiles of this overlay object support.
- [var maximumZ: Int](./maximumz.md)
  The maximum zoom level that the tiles of this overlay object support.
- [var canReplaceMapContent: Bool](./canreplacemapcontent.md)
  A Boolean value that indicates whether the tile content is fully opaque.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mktileoverlay/isgeometryflipped)*