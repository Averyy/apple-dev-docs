# isReadable

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether you can extract the asset’s media data using an asset reader.

**Availability**:
- iOS 4.3+ - Deprecated in 16.0
- iPadOS 4.3+ - Deprecated in 16.0
- Mac Catalyst 13.1+ - Deprecated in 16.0
- macOS 10.7+ - Deprecated in 13.0
- tvOS 9.0+ - Deprecated in 16.0

> **Deprecated**: Load the value of [`isReadable`](../avpartialasyncproperty/isreadable.md) asynchronously instead.

## Declaration

```swift
var isReadable: Bool { get }
```

```objc
@property (nonatomic, readonly, getter=isReadable) BOOL readable;
```

#### Discussion

This property value is [`true`](../../Swift/true.md) if you can use [`AVAssetReader`](../avassetreader.md) to extract the asset’s media data.

## See Also

### Accessing suitability
- [playable](./isplayable.md)
  A Boolean value that indicates whether the asset has playable content.
- [exportable](./isexportable.md)
  A Boolean value that indicates whether you can export this asset using an export session.
- [composable](./iscomposable.md)
  A Boolean value that indicates whether you can use the asset as a segment of a composition track.
- [compatibleWithAirPlayVideo](./iscompatiblewithairplayvideo.md)
  A Boolean value that indicates whether the asset is compatible with AirPlay Video.
- [compatibleWithSavedPhotosAlbum](./iscompatiblewithsavedphotosalbum.md)
  A Boolean value that indicates whether you can write the asset to the Saved Photos album.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avasset/isreadable)*