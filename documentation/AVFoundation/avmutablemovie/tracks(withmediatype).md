# tracks(withMediaType:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

Retrieves tracks in the movie that present media of the specified type.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
func tracks(withMediaType mediaType: AVMediaType) -> [AVMutableMovieTrack]
```

```objc
- (NSArray<AVMutableMovieTrack *> *) tracksWithMediaType:(AVMediaType) mediaType;
```

#### Return Value

An array of tracks, which is empty if there are no tracks with the media type.

#### Discussion

Apple discourages using this method in iOS 15, tvOS 15, macOS 12, and watchOS 8 or later. Load tracks asynchronously using [`loadTracks(withMediaType:completionHandler:)`](./loadtracks%28withmediatype,completionhandler%29.md) instead.

## Parameters

- `mediaType`: The media type of the tracks to return.

## See Also

### Accessing tracks
- [var tracks: [AVMutableMovieTrack]](./tracks.md)
  The tracks that a movie contains.
- [func track(withTrackID: CMPersistentTrackID) -> AVMutableMovieTrack?](./track%28withtrackid%29.md)
  Retrieves a track in the movie that contains the specified identifier.
- [func tracks(withMediaCharacteristic: AVMediaCharacteristic) -> [AVMutableMovieTrack]](./tracks%28withmediacharacteristic%29.md)
  Retrieve tracks in the movie that present media of the specified characteristic.
- [func unusedTrackID() -> CMPersistentTrackID](./unusedtrackid%28%29.md)
  Returns an identifier that no other tracks in the asset use.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmutablemovie/tracks(withmediatype:))*