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
func track(withTrackID trackID: CMPersistentTrackID) -> AVCompositionTrack?
```

#### Return Value

A composition track, or `nil` if no track with the identifier exists.

#### Discussion

Apple discourages using this method in iOS 15, tvOS 15, macOS 12, and watchOS 8 or later. Load a track asynchronously using [`loadTrack(withTrackID:completionHandler:)`](avcomposition/loadtrack(withtrackid:completionhandler:).md) instead.

## Parameters

- `trackID`: The identifier of the track to retrieve.

## See Also

- [var tracks: [AVCompositionTrack]](avcomposition/tracks.md)
  The tracks that a composition contains.
- [func tracks(withMediaType: AVMediaType) -> [AVCompositionTrack]](avcomposition/tracks(withmediatype:).md)
  Returns tracks that contain media of a specified type.
- [func tracks(withMediaCharacteristic: AVMediaCharacteristic) -> [AVCompositionTrack]](avcomposition/tracks(withmediacharacteristic:).md)
  Returns tracks that contain media of a specified characteristic.
- [func unusedTrackID() -> CMPersistentTrackID](avcomposition/unusedtrackid.md)
  Returns an identifier that no other tracks in the asset use.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcomposition/track(withtrackid:))*