# isCompatibleWithAirPlayVideo

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the asset is compatible with AirPlay Video.

**Availability**:
- iOS 9.0+ - Deprecated in 16.0
- iPadOS 9.0+ - Deprecated in 16.0
- Mac Catalyst 13.1+ - Deprecated in 16.0
- macOS 10.11+ - Deprecated in 13.0
- tvOS 9.0+ - Deprecated in 16.0

> **Deprecated**: Load the value of [`isCompatibleWithAirPlayVideo`](../avpartialasyncproperty/iscompatiblewithairplayvideo.md) asynchronously instead.

## Declaration

```swift
var isCompatibleWithAirPlayVideo: Bool { get }
```

```objc
@property (nonatomic, readonly, getter=isCompatibleWithAirPlayVideo) BOOL compatibleWithAirPlayVideo;
```

## Discussion

This property value is [`true`](../../Swift/true.md) if you can play this asset’s content to an external AirPlay device, like an Apple TV.

## See Also

### Accessing suitability
- [playable](./isplayable.md)
  A Boolean value that indicates whether the asset has playable content.
- [exportable](./isexportable.md)
  A Boolean value that indicates whether you can export this asset using an export session.
- [readable](./isreadable.md)
  A Boolean value that indicates whether you can extract the asset’s media data using an asset reader.
- [composable](./iscomposable.md)
  A Boolean value that indicates whether you can use the asset as a segment of a composition track.
- [compatibleWithSavedPhotosAlbum](./iscompatiblewithsavedphotosalbum.md)
  A Boolean value that indicates whether you can write the asset to the Saved Photos album.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avasset/iscompatiblewithairplayvideo)*