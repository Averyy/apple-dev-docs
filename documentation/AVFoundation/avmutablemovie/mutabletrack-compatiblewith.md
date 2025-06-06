# mutableTrack(compatibleWith:)

**Framework**: AVFoundation  
**Kind**: method

Provides a reference to a track from a mutable movie into which you can insert any time range.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
func mutableTrack(compatibleWith track: AVAssetTrack) -> AVMutableMovieTrack?
```

#### Return Value

An [`AVMutableMovieTrack`](avmutablemovietrack.md) object that can accommodate the time range insertion. Returns nil when no track is available.

#### Discussion

Keep the number of tracks in a movie to a minimum, corresponding to the number of tracks for which media data must be presented in parallel. If media data of the same type is presented serially, even from multiple assets, a single track of that media type should be used. This method can help the client to identify an existing target track for an insertion.

## Parameters

- `track`: The   containing the desired time range.

## See Also

- [func addMutableTrack(withMediaType: AVMediaType, copySettingsFrom: AVAssetTrack?, options: [String : Any]?) -> AVMutableMovieTrack?](avmutablemovie/addmutabletrack(withmediatype:copysettingsfrom:options:).md)
  Adds an empty track to the target movie.
- [func addMutableTracksCopyingSettings(from: [AVAssetTrack], options: [String : Any]?) -> [AVMutableMovieTrack]](avmutablemovie/addmutabletrackscopyingsettings(from:options:).md)
  Adds one or more empty tracks to the target movie and copies the track settings from the source tracks.
- [func removeTrack(AVMovieTrack)](avmutablemovie/removetrack(_:).md)
  Removes the specified track from the target movie.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmutablemovie/mutabletrack(compatiblewith:))*