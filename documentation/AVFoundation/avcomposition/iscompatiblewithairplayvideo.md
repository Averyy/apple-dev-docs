# isCompatibleWithAirPlayVideo

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the asset is compatible with AirPlay Video.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var isCompatibleWithAirPlayVideo: Bool { get }
```

#### Discussion

This property value is [`true`](../../Swift/true.md) if you can play this composition’s content to an external AirPlay device, like an Apple TV.

## See Also

### Determining suitability
- [var isPlayable: Bool](./isplayable.md)
  A Boolean value that indicates whether the asset has playable content.
- [var isReadable: Bool](./isreadable.md)
  A Boolean value that indicates whether you can extract the asset’s media data using an asset reader.
- [var isExportable: Bool](./isexportable.md)
  A Boolean value that indicates whether you can export this asset using an export session.
- [var isComposable: Bool](./iscomposable.md)
  A Boolean value that indicates whether you can use the asset as a segment of a composition track.
- [var isCompatibleWithSavedPhotosAlbum: Bool](./iscompatiblewithsavedphotosalbum.md)
  A Boolean value that indicates whether you can write the composition to the Saved Photos album.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcomposition/iscompatiblewithairplayvideo)*