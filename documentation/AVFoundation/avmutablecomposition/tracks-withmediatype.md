# tracks(withMediaType:)

**Framework**: AVFoundation  
**Kind**: method

Returns tracks that contain media of a specified type.

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
func tracks(withMediaType mediaType: AVMediaType) -> [AVMutableCompositionTrack]
```

#### Return Value

An array of composition tracks, which is empty if there are no matching tracks.

#### Discussion

Apple discourages using this method. Load tracks asynchronously using [`loadTracks(withMediaType:completionHandler:)`](avmutablecomposition/loadtracks(withmediatype:completionhandler:).md) instead.

## Parameters

- `mediaType`: The media type of the tracks to return.

## See Also

- [var tracks: [AVMutableCompositionTrack]](avmutablecomposition/tracks.md)
  The tracks that a composition contains.
- [func track(withTrackID: CMPersistentTrackID) -> AVMutableCompositionTrack?](avmutablecomposition/track(withtrackid:).md)
  Returns a track that contains the specified identifier.
- [func tracks(withMediaCharacteristic: AVMediaCharacteristic) -> [AVMutableCompositionTrack]](avmutablecomposition/tracks(withmediacharacteristic:).md)
  Returns tracks that contain media of a specified characteristic.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmutablecomposition/tracks(withmediatype:))*