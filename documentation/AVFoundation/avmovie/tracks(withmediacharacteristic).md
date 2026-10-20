# tracks(withMediaCharacteristic:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

Retrieves tracks in the movie that present media of the specified characteristic.

**Availability**:
- iOS 4.0+ - Deprecated in 16.0
- iPadOS 4.0+ - Deprecated in 16.0
- Mac Catalyst 13.1+ - Deprecated in 16.0
- macOS 10.7+ - Deprecated in 13.0
- watchOS 1.0+ - Deprecated in 9.0

> **Deprecated**: Use [`loadTracks(withMediaCharacteristic:completionHandler:)`](./loadtracks%28withmediacharacteristic,completionhandler%29.md) instead.

## Declaration

```swift
func tracks(withMediaCharacteristic mediaCharacteristic: AVMediaCharacteristic) -> [AVMovieTrack]
```

```objc
- (NSArray<AVMovieTrack *> *) tracksWithMediaCharacteristic:(AVMediaCharacteristic) mediaCharacteristic;
```

#### Return Value

An array of tracks, which is empty if there are no tracks with the media characteristic.

#### Discussion

Apple discourages using this method in iOS 15, tvOS 15, macOS 12, and watchOS 8 or later. Load tracks asynchronously using [`loadTracks(withMediaCharacteristic:completionHandler:)`](./loadtracks%28withmediacharacteristic,completionhandler%29.md) instead.

## Parameters

- `mediaCharacteristic`: The media characteristic of the tracks to return.

## See Also

### Accessing tracks
- [var tracks: [AVMovieTrack]](./tracks.md)
  The tracks that a movie contains.
- [func track(withTrackID: CMPersistentTrackID) -> AVMovieTrack?](./track%28withtrackid%29.md)
  Retrieves a track in the movie that contains the specified identifier.
- [func tracks(withMediaType: AVMediaType) -> [AVMovieTrack]](./tracks%28withmediatype%29.md)
  Retrieves tracks in the movie that present media of the specified type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmovie/tracks(withmediacharacteristic:))*