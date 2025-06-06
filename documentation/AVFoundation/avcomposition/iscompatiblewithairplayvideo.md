# isCompatibleWithAirPlayVideo

**Framework**: AVFoundation  
**Kind**: property

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

This property value is [`true`](https://developer.apple.com/documentation/swift/true) if you can play this composition’s content to an external AirPlay device, like an Apple TV.

## See Also

- [var isPlayable: Bool](avcomposition/isplayable.md)
  A Boolean value that indicates whether the asset has playable content.
- [var isReadable: Bool](avcomposition/isreadable.md)
  A Boolean value that indicates whether you can extract the asset’s media data using an asset reader.
- [var isExportable: Bool](avcomposition/isexportable.md)
  A Boolean value that indicates whether you can export this asset using an export session.
- [var isComposable: Bool](avcomposition/iscomposable.md)
  A Boolean value that indicates whether you can use the asset as a segment of a composition track.
- [var isCompatibleWithSavedPhotosAlbum: Bool](avcomposition/iscompatiblewithsavedphotosalbum.md)
  A Boolean value that indicates whether you can write the composition to the Saved Photos album.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcomposition/iscompatiblewithairplayvideo)*