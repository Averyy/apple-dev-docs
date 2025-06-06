# track(withTrackID:)

**Framework**: AVFoundation  
**Kind**: method

Retrieves a track in the movie that contains the specified identifier.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- watchOS 1.0+

## Declaration

```swift
func track(withTrackID trackID: CMPersistentTrackID) -> AVFragmentedMovieTrack?
```

#### Return Value

A movie track, or `nil` if there is no track with the identifier.

#### Discussion

Apple discourages using this method in iOS 15, tvOS 15, macOS 12, and watchOS 8 or later. Load a track asynchronously using [`loadTrack(withTrackID:completionHandler:)`](avfragmentedmovie/loadtrack(withtrackid:completionhandler:).md) instead.

## Parameters

- `trackID`: The persistent track identifier.

## See Also

- [var tracks: [AVFragmentedMovieTrack]](avfragmentedmovie/tracks.md)
  The tracks that a movie contains.
- [func tracks(withMediaType: AVMediaType) -> [AVFragmentedMovieTrack]](avfragmentedmovie/tracks(withmediatype:).md)
  Retrieves tracks in the movie that present media of the specified type.
- [func tracks(withMediaCharacteristic: AVMediaCharacteristic) -> [AVFragmentedMovieTrack]](avfragmentedmovie/tracks(withmediacharacteristic:).md)
  Retrieves tracks in the movie that present media of the specified characteristic.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avfragmentedmovie/track(withtrackid:))*