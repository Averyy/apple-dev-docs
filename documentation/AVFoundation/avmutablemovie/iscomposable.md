# isComposable

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether you can use the asset as a segment of a composition track.

**Availability**:
- iOS 4.3+
- iPadOS 4.3+
- Mac Catalyst 13.1+
- macOS 10.7+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
var isComposable: Bool { get }
```

#### Discussion

This property value is [`true`](../../Swift/true.md) if you can use the composition as a segment within an [`AVCompositionTrack`](../avcompositiontrack.md) object.

## See Also

### Determining suitability
- [var isPlayable: Bool](./isplayable.md)
  A Boolean value that indicates whether the asset has playable content.
- [var isReadable: Bool](./isreadable.md)
  A Boolean value that indicates whether you can extract the asset’s media data using an asset reader.
- [var isExportable: Bool](./isexportable.md)
  A Boolean value that indicates whether you can export this asset using an export session.
- [var isCompatibleWithAirPlayVideo: Bool](./iscompatiblewithairplayvideo.md)
  A Boolean value that indicates whether the asset is compatible with AirPlay Video.
- [var isCompatibleWithSavedPhotosAlbum: Bool](./iscompatiblewithsavedphotosalbum.md)
  A Boolean value that indicates whether you can write the composition to the Saved Photos album.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmutablemovie/iscomposable)*