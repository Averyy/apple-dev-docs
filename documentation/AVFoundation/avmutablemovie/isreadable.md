# isReadable

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether you can extract the asset’s media data using an asset reader.

**Availability**:
- iOS 4.3+
- iPadOS 4.3+
- Mac Catalyst 13.1+
- macOS 10.7+
- visionOS 1.0+

## Declaration

```swift
var isReadable: Bool { get }
```

#### Discussion

This property value is [`true`](../../Swift/true.md) if you can use [`AVAssetReader`](../avassetreader.md) to extract the composition’s media data.

## See Also

### Determining suitability
- [var isPlayable: Bool](./isplayable.md)
  A Boolean value that indicates whether the asset has playable content.
- [var isExportable: Bool](./isexportable.md)
  A Boolean value that indicates whether you can export this asset using an export session.
- [var isComposable: Bool](./iscomposable.md)
  A Boolean value that indicates whether you can use the asset as a segment of a composition track.
- [var isCompatibleWithAirPlayVideo: Bool](./iscompatiblewithairplayvideo.md)
  A Boolean value that indicates whether the asset is compatible with AirPlay Video.
- [var isCompatibleWithSavedPhotosAlbum: Bool](./iscompatiblewithsavedphotosalbum.md)
  A Boolean value that indicates whether you can write the composition to the Saved Photos album.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmutablemovie/isreadable)*