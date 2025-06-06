# tracks(withMediaType:)

**Framework**: AVFoundation  
**Kind**: method

Retrieves tracks in the movie that present media of the specified type.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- watchOS 1.0+

## Declaration

```swift
func tracks(withMediaType mediaType: AVMediaType) -> [AVMovieTrack]
```

#### Return Value

An array of tracks, which is empty if there are no tracks with the media type.

#### Discussion

Apple discourages using this method in iOS 15, tvOS 15, macOS 12, and watchOS 8 or later. Load tracks asynchronously using [`loadTracks(withMediaType:completionHandler:)`](avmovie/loadtracks(withmediatype:completionhandler:).md) instead.

## Parameters

- `mediaType`: The media type of the tracks to return.

## See Also

- [var tracks: [AVMovieTrack]](avmovie/tracks.md)
  The tracks that a movie contains.
- [func track(withTrackID: CMPersistentTrackID) -> AVMovieTrack?](avmovie/track(withtrackid:).md)
  Retrieves a track in the movie that contains the specified identifier.
- [func tracks(withMediaCharacteristic: AVMediaCharacteristic) -> [AVMovieTrack]](avmovie/tracks(withmediacharacteristic:).md)
  Retrieves tracks in the movie that present media of the specified characteristic.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmovie/tracks(withmediatype:))*