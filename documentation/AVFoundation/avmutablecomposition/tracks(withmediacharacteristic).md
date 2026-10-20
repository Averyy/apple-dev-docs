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
func tracks(withMediaCharacteristic mediaCharacteristic: AVMediaCharacteristic) -> [AVMutableCompositionTrack]
```

```objc
- (NSArray<AVMutableCompositionTrack *> *) tracksWithMediaCharacteristic:(AVMediaCharacteristic) mediaCharacteristic;
```

#### Return Value

An array of composition tracks, which is empty if there are no matching tracks.

#### Discussion

Apple discourages using this method. Load tracks asynchronously using [`loadTracks(withMediaCharacteristic:completionHandler:)`](./loadtracks%28withmediacharacteristic,completionhandler%29.md) instead.

## Parameters

- `mediaCharacteristic`: The media characteristic of the tracks to return.

## See Also

### Accessing tracks
- [var tracks: [AVMutableCompositionTrack]](./tracks.md)
  The tracks that a composition contains.
- [func track(withTrackID: CMPersistentTrackID) -> AVMutableCompositionTrack?](./track%28withtrackid%29.md)
  Returns a track that contains the specified identifier.
- [func tracks(withMediaType: AVMediaType) -> [AVMutableCompositionTrack]](./tracks%28withmediatype%29.md)
  Returns tracks that contain media of a specified type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmutablecomposition/tracks(withmediacharacteristic:))*