# tracks(withMediaCharacteristic:)

**Framework**: AVFoundation  
**Kind**: method

Returns tracks that contain media of a specified characteristic.

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
func tracks(withMediaCharacteristic mediaCharacteristic: AVMediaCharacteristic) -> [AVMutableCompositionTrack]
```

#### Return Value

An array of composition tracks, which is empty if there are no matching tracks.

#### Discussion

Apple discourages using this method. Load tracks asynchronously using [`loadTracks(withMediaCharacteristic:completionHandler:)`](avmutablecomposition/loadtracks(withmediacharacteristic:completionhandler:).md) instead.

## Parameters

- `mediaCharacteristic`: The media characteristic of the tracks to return.

## See Also

- [var tracks: [AVMutableCompositionTrack]](avmutablecomposition/tracks.md)
  The tracks that a composition contains.
- [func track(withTrackID: CMPersistentTrackID) -> AVMutableCompositionTrack?](avmutablecomposition/track(withtrackid:).md)
  Returns a track that contains the specified identifier.
- [func tracks(withMediaType: AVMediaType) -> [AVMutableCompositionTrack]](avmutablecomposition/tracks(withmediatype:).md)
  Returns tracks that contain media of a specified type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmutablecomposition/tracks(withmediacharacteristic:))*