# isPlayable

**Framework**: AVFoundation  
**Kind**: property

A Boolean value that indicates whether the asset has playable content.

**Availability**:
- iOS 4.3+
- iPadOS 4.3+
- Mac Catalyst 13.1+
- macOS 10.7+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
var isPlayable: Bool { get }
```

#### Discussion

This property value is [`true`](https://developer.apple.com/documentation/Swift/true) if you can use the movie to create an [`AVPlayerItem`](avplayeritem.md).

## See Also

- [var isReadable: Bool](avmutablemovie/isreadable.md)
  A Boolean value that indicates whether you can extract the asset’s media data using an asset reader.
- [var isExportable: Bool](avmutablemovie/isexportable.md)
  A Boolean value that indicates whether you can export this asset using an export session.
- [var isComposable: Bool](avmutablemovie/iscomposable.md)
  A Boolean value that indicates whether you can use the asset as a segment of a composition track.
- [var isCompatibleWithAirPlayVideo: Bool](avmutablemovie/iscompatiblewithairplayvideo.md)
  A Boolean value that indicates whether the asset is compatible with AirPlay Video.
- [var isCompatibleWithSavedPhotosAlbum: Bool](avmutablemovie/iscompatiblewithsavedphotosalbum.md)
  A Boolean value that indicates whether you can write the composition to the Saved Photos album.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmutablemovie/isplayable)*