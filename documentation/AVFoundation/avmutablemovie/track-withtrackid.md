# track(withTrackID:)

**Framework**: AVFoundation  
**Kind**: method

Retrieves a track in the movie that contains the specified identifier.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
func track(withTrackID trackID: CMPersistentTrackID) -> AVMutableMovieTrack?
```

#### Return Value

A movie track, or `nil` if there is no track with the identifier.

#### Discussion

Apple discourages using this method in iOS 15, tvOS 15, macOS 12, and watchOS 8 or later. Load a track asynchronously using [`loadTrack(withTrackID:completionHandler:)`](avmutablemovie/loadtrack(withtrackid:completionhandler:).md) instead.

## Parameters

- `trackID`: The track identifier for the requested track.

## See Also

- [var tracks: [AVMutableMovieTrack]](avmutablemovie/tracks.md)
  The tracks that a movie contains.
- [func tracks(withMediaType: AVMediaType) -> [AVMutableMovieTrack]](avmutablemovie/tracks(withmediatype:).md)
  Retrieves tracks in the movie that present media of the specified type.
- [func tracks(withMediaCharacteristic: AVMediaCharacteristic) -> [AVMutableMovieTrack]](avmutablemovie/tracks(withmediacharacteristic:).md)
  Retrieve tracks in the movie that present media of the specified characteristic.
- [func unusedTrackID() -> CMPersistentTrackID](avmutablemovie/unusedtrackid.md)
  Returns an identifier that no other tracks in the asset use.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmutablemovie/track(withtrackid:))*