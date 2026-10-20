# tracks

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The tracks an asset contains.

**Availability**:
- iOS 12.0+ - Deprecated in 16.0
- iPadOS 12.0+ - Deprecated in 16.0
- Mac Catalyst 13.1+ - Deprecated in 16.0
- macOS 10.11+ - Deprecated in 13.0
- tvOS 12.0+ - Deprecated in 16.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 6.0+ - Deprecated in 9.0

> **Deprecated**: Load the value of [`tracks`](../avpartialasyncproperty/tracks-9z3j9.md) asynchronously instead.

## Declaration

```swift
var tracks: [AVFragmentedAssetTrack] { get }
```

```objc
@property (nonatomic, readonly) NSArray<AVFragmentedAssetTrack *> * tracks;
```

## See Also

### Accessing tracks
- [func track(withTrackID: CMPersistentTrackID) -> AVFragmentedAssetTrack?](./track%28withtrackid%29.md)
  Returns a track that contains the specified identifier.
- [func tracks(withMediaType: AVMediaType) -> [AVFragmentedAssetTrack]](./tracks%28withmediatype%29.md)
  Returns tracks that present media of a specified type.
- [func tracks(withMediaCharacteristic: AVMediaCharacteristic) -> [AVFragmentedAssetTrack]](./tracks%28withmediacharacteristic%29.md)
  Returns tracks that present media of a specified characteristic.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avfragmentedasset/tracks)*