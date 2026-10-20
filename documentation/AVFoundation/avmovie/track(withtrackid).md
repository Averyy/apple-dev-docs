# track(withTrackID:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

Retrieves a track in the movie that contains the specified identifier.

**Availability**:
- iOS 4.0+ - Deprecated in 16.0
- iPadOS 4.0+ - Deprecated in 16.0
- Mac Catalyst 13.1+ - Deprecated in 16.0
- macOS 10.7+ - Deprecated in 13.0
- watchOS 1.0+ - Deprecated in 9.0

> **Deprecated**: Use [`loadTrack(withTrackID:completionHandler:)`](./loadtrack%28withtrackid,completionhandler%29.md) instead.

## Declaration

```swift
func track(withTrackID trackID: CMPersistentTrackID) -> AVMovieTrack?
```

```objc
- (AVMovieTrack *) trackWithTrackID:(CMPersistentTrackID) trackID;
```

#### Return Value

A movie track, or `nil` if there is no track with the identifier.

#### Discussion

Apple discourages using this method in iOS 15, tvOS 15, macOS 12, and watchOS 8 or later. Load a track asynchronously using [`loadTrack(withTrackID:completionHandler:)`](./loadtrack%28withtrackid,completionhandler%29.md) instead.

## Parameters

- `trackID`: The persistent track identifier.

## See Also

### Accessing tracks
- [var tracks: [AVMovieTrack]](./tracks.md)
  The tracks that a movie contains.
- [func tracks(withMediaType: AVMediaType) -> [AVMovieTrack]](./tracks%28withmediatype%29.md)
  Retrieves tracks in the movie that present media of the specified type.
- [func tracks(withMediaCharacteristic: AVMediaCharacteristic) -> [AVMovieTrack]](./tracks%28withmediacharacteristic%29.md)
  Retrieves tracks in the movie that present media of the specified characteristic.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmovie/track(withtrackid:))*