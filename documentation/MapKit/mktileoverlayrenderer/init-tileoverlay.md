# init(tileOverlay:)

**Framework**: MapKit  
**Kind**: init

Initializes and returns a tile renderer with the specified overlay object.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.2+
- visionOS 1.0+

## Declaration

```swift
init(tileOverlay overlay: MKTileOverlay)
```

#### Return Value

An initialized tile renderer object.

#### Discussion

The returned renderer object works with the tile overlay object to coordinate the loading and display of its map tiles.

## Parameters

- `overlay`: The tile overlay object whose contents you want to draw.

## See Also

- [Location and Maps Programming Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/LocationAwarenessPG/Introduction/Introduction.html#//apple_ref/doc/uid/TP40009497)


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mktileoverlayrenderer/init(tileoverlay:))*