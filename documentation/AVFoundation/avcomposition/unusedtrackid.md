# unusedTrackID()

**Framework**: AVFoundation  
**Kind**: method

Returns an identifier that no other tracks in the asset use.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
func unusedTrackID() -> CMPersistentTrackID
```

#### Return Value

An unused [`CMPersistentTrackID`](https://developer.apple.com/documentation/CoreMedia/CMPersistentTrackID) value.

## See Also

- [var tracks: [AVCompositionTrack]](avcomposition/tracks.md)
  The tracks that a composition contains.
- [func track(withTrackID: CMPersistentTrackID) -> AVCompositionTrack?](avcomposition/track(withtrackid:).md)
  Returns a track that contains the specified identifier.
- [func tracks(withMediaType: AVMediaType) -> [AVCompositionTrack]](avcomposition/tracks(withmediatype:).md)
  Returns tracks that contain media of a specified type.
- [func tracks(withMediaCharacteristic: AVMediaCharacteristic) -> [AVCompositionTrack]](avcomposition/tracks(withmediacharacteristic:).md)
  Returns tracks that contain media of a specified characteristic.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcomposition/unusedtrackid())*