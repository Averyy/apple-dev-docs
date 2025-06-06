# isExportable

**Framework**: AVFoundation  
**Kind**: property

A Boolean value that indicates whether you can export an asset using an export session.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst ?+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
static var isExportable: AVAsyncProperty<Root, Bool> { get }
```

#### Discussion

Use the [`load(_:)`](avasynchronouskeyvalueloading/load(_:).md) method to retrieve the property value.

## See Also

- [static var isPlayable: AVAsyncProperty<Root, Bool>](avpartialasyncproperty/isplayable-45h5v.md)
  A Boolean value that indicates whether an asset contains playable content.
- [static var isReadable: AVAsyncProperty<Root, Bool>](avpartialasyncproperty/isreadable.md)
  A Boolean value that indicates whether you can extract the asset’s media data using an asset reader.
- [static var isComposable: AVAsyncProperty<Root, Bool>](avpartialasyncproperty/iscomposable.md)
  A Boolean value that indicates whether you can use the asset in a media composition.
- [static var isCompatibleWithAirPlayVideo: AVAsyncProperty<Root, Bool>](avpartialasyncproperty/iscompatiblewithairplayvideo.md)
  A Boolean value that indicates whether the asset is compatible with AirPlay Video.
- [static var isCompatibleWithSavedPhotosAlbum: AVAsyncProperty<Root, Bool>](avpartialasyncproperty/iscompatiblewithsavedphotosalbum.md)
  A Boolean value that indicates whether you can write the asset to the Saved Photos album.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avpartialasyncproperty/isexportable)*