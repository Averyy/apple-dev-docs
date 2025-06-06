# tracks

**Framework**: AVFoundation  
**Kind**: property

The tracks an asset contains.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 12.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
var tracks: [AVFragmentedAssetTrack] { get }
```

## See Also

- [func track(withTrackID: CMPersistentTrackID) -> AVFragmentedAssetTrack?](avfragmentedasset/track(withtrackid:).md)
  Returns a track that contains the specified identifier.
- [func tracks(withMediaType: AVMediaType) -> [AVFragmentedAssetTrack]](avfragmentedasset/tracks(withmediatype:).md)
  Returns tracks that present media of a specified type.
- [func tracks(withMediaCharacteristic: AVMediaCharacteristic) -> [AVFragmentedAssetTrack]](avfragmentedasset/tracks(withmediacharacteristic:).md)
  Returns tracks that present media of a specified characteristic.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avfragmentedasset/tracks)*