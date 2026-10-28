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
func tracks(withMediaType mediaType: AVMediaType) -> [AVCompositionTrack]
```

```objc
- (NSArray<AVCompositionTrack *> *) tracksWithMediaType:(AVMediaType) mediaType;
```

## Return Value

An array of tracks, which is empty if no tracks with the media type exist.

## Discussion

Apple discourages using this method in iOS 15, tvOS 15, macOS 12, and watchOS 8 or later. Load tracks asynchronously using [`loadTracks(withMediaType:completionHandler:)`](./loadtracks%28withmediatype,completionhandler%29.md) instead.

## Parameters

- `mediaType`: The media type of the tracks to return.

## See Also

### Accessing tracks
- [var tracks: [AVCompositionTrack]](./tracks.md)
  The tracks that a composition contains.
- [func track(withTrackID: CMPersistentTrackID) -> AVCompositionTrack?](./track%28withtrackid%29.md)
  Returns a track that contains the specified identifier.
- [func tracks(withMediaCharacteristic: AVMediaCharacteristic) -> [AVCompositionTrack]](./tracks%28withmediacharacteristic%29.md)
  Returns tracks that contain media of a specified characteristic.
- [func unusedTrackID() -> CMPersistentTrackID](./unusedtrackid%28%29.md)
  Returns an identifier that no other tracks in the asset use.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcomposition/tracks(withmediatype:))*