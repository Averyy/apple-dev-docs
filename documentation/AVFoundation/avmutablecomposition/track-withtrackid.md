# track(withTrackID:)

**Framework**: AVFoundation  
**Kind**: method

Returns a track that contains the specified identifier.

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
func track(withTrackID trackID: CMPersistentTrackID) -> AVMutableCompositionTrack?
```

#### Return Value

A composition track or `nil` if no track is available.

#### Discussion

Apple discourages using this method. Load a track asynchronously using [`loadTrack(withTrackID:completionHandler:)`](avmutablecomposition/loadtrack(withtrackid:completionhandler:).md) instead.

## Parameters

- `trackID`: The persistent track identifier.

## See Also

- [var tracks: [AVMutableCompositionTrack]](avmutablecomposition/tracks.md)
  The tracks that a composition contains.
- [func tracks(withMediaType: AVMediaType) -> [AVMutableCompositionTrack]](avmutablecomposition/tracks(withmediatype:).md)
  Returns tracks that contain media of a specified type.
- [func tracks(withMediaCharacteristic: AVMediaCharacteristic) -> [AVMutableCompositionTrack]](avmutablecomposition/tracks(withmediacharacteristic:).md)
  Returns tracks that contain media of a specified characteristic.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmutablecomposition/track(withtrackid:))*