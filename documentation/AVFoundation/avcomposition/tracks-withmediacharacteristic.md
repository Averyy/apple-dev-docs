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
func tracks(withMediaCharacteristic mediaCharacteristic: AVMediaCharacteristic) -> [AVCompositionTrack]
```

#### Return Value

An array of tracks, which is empty if no tracks with the media characteristic exist.

#### Discussion

Apple discourages using this method in iOS 15, tvOS 15, macOS 12, and watchOS 8 or later. Load tracks asynchronously using [`loadTracks(withMediaCharacteristic:completionHandler:)`](avcomposition/loadtracks(withmediacharacteristic:completionhandler:).md) instead.

## Parameters

- `mediaCharacteristic`: The media characteristic of the tracks to return.

## See Also

- [var tracks: [AVCompositionTrack]](avcomposition/tracks.md)
  The tracks that a composition contains.
- [func track(withTrackID: CMPersistentTrackID) -> AVCompositionTrack?](avcomposition/track(withtrackid:).md)
  Returns a track that contains the specified identifier.
- [func tracks(withMediaType: AVMediaType) -> [AVCompositionTrack]](avcomposition/tracks(withmediatype:).md)
  Returns tracks that contain media of a specified type.
- [func unusedTrackID() -> CMPersistentTrackID](avcomposition/unusedtrackid.md)
  Returns an identifier that no other tracks in the asset use.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcomposition/tracks(withmediacharacteristic:))*