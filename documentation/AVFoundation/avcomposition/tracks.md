# tracks

**Framework**: AVFoundation  
**Kind**: property

The tracks that a composition contains.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
var tracks: [AVCompositionTrack] { get }
```

## See Also

- [func track(withTrackID: CMPersistentTrackID) -> AVCompositionTrack?](avcomposition/track(withtrackid:).md)
  Returns a track that contains the specified identifier.
- [func tracks(withMediaType: AVMediaType) -> [AVCompositionTrack]](avcomposition/tracks(withmediatype:).md)
  Returns tracks that contain media of a specified type.
- [func tracks(withMediaCharacteristic: AVMediaCharacteristic) -> [AVCompositionTrack]](avcomposition/tracks(withmediacharacteristic:).md)
  Returns tracks that contain media of a specified characteristic.
- [func unusedTrackID() -> CMPersistentTrackID](avcomposition/unusedtrackid.md)
  Returns an identifier that no other tracks in the asset use.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcomposition/tracks)*