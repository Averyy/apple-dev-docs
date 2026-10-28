# tracks(withMediaType:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

Returns tracks that contain media of a specified type.

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
func tracks(withMediaType mediaType: AVMediaType) -> [AVMutableCompositionTrack]
```

```objc
- (NSArray<AVMutableCompositionTrack *> *) tracksWithMediaType:(AVMediaType) mediaType;
```

## Return Value

An array of composition tracks, which is empty if there are no matching tracks.

## Discussion

Apple discourages using this method. Load tracks asynchronously using [`loadTracks(withMediaType:completionHandler:)`](./loadtracks%28withmediatype,completionhandler%29.md) instead.

## Parameters

- `mediaType`: The media type of the tracks to return.

## See Also

### Accessing tracks
- [var tracks: [AVMutableCompositionTrack]](./tracks.md)
  The tracks that a composition contains.
- [func track(withTrackID: CMPersistentTrackID) -> AVMutableCompositionTrack?](./track%28withtrackid%29.md)
  Returns a track that contains the specified identifier.
- [func tracks(withMediaCharacteristic: AVMediaCharacteristic) -> [AVMutableCompositionTrack]](./tracks%28withmediacharacteristic%29.md)
  Returns tracks that contain media of a specified characteristic.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmutablecomposition/tracks(withmediatype:))*