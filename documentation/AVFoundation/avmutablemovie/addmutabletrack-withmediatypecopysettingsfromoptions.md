# addMutableTrack(withMediaType:copySettingsFrom:options:)

**Framework**: AVFoundation  
**Kind**: method

Adds an empty track to the target movie.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
func addMutableTrack(withMediaType mediaType: AVMediaType, copySettingsFrom track: AVAssetTrack?, options: [String : Any]? = nil) -> AVMutableMovieTrack?
```

#### Return Value

An [`AVMutableMovieTrack`](avmutablemovietrack.md) object.

## Parameters

- `mediaType`: The media type for the new track.
- `track`: An   containing the desired track settings to be transferred. Set to   to create a track with default settings.
- `options`: A dictionary that contains key for specifying the movie object initialization. Currently, no keys are defined.

## See Also

- [func mutableTrack(compatibleWith: AVAssetTrack) -> AVMutableMovieTrack?](avmutablemovie/mutabletrack(compatiblewith:).md)
  Provides a reference to a track from a mutable movie into which you can insert any time range.
- [func addMutableTracksCopyingSettings(from: [AVAssetTrack], options: [String : Any]?) -> [AVMutableMovieTrack]](avmutablemovie/addmutabletrackscopyingsettings(from:options:).md)
  Adds one or more empty tracks to the target movie and copies the track settings from the source tracks.
- [func removeTrack(AVMovieTrack)](avmutablemovie/removetrack(_:).md)
  Removes the specified track from the target movie.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmutablemovie/addmutabletrack(withmediatype:copysettingsfrom:options:))*