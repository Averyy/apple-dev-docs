# tracks(withMediaCharacteristic:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

Returns tracks that contain media of a specified characteristic.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
func tracks(withMediaCharacteristic mediaCharacteristic: AVMediaCharacteristic) -> [AVCompositionTrack]
```

```objc
- (NSArray<AVCompositionTrack *> *) tracksWithMediaCharacteristic:(AVMediaCharacteristic) mediaCharacteristic;
```

#### Return Value

An array of tracks, which is empty if no tracks with the media characteristic exist.

#### Discussion

Apple discourages using this method in iOS 15, tvOS 15, macOS 12, and watchOS 8 or later. Load tracks asynchronously using [`loadTracks(withMediaCharacteristic:completionHandler:)`](./loadtracks%28withmediacharacteristic,completionhandler%29.md) instead.

## Parameters

- `mediaCharacteristic`: The media characteristic of the tracks to return.

## See Also

### Accessing tracks
- [var tracks: [AVCompositionTrack]](./tracks.md)
  The tracks that a composition contains.
- [func track(withTrackID: CMPersistentTrackID) -> AVCompositionTrack?](./track%28withtrackid%29.md)
  Returns a track that contains the specified identifier.
- [func tracks(withMediaType: AVMediaType) -> [AVCompositionTrack]](./tracks%28withmediatype%29.md)
  Returns tracks that contain media of a specified type.
- [func unusedTrackID() -> CMPersistentTrackID](./unusedtrackid%28%29.md)
  Returns an identifier that no other tracks in the asset use.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcomposition/tracks(withmediacharacteristic:))*