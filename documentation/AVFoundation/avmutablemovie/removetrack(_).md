# removeTrack(_:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

Removes the specified track from the target movie.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
func removeTrack(_ track: AVMovieTrack)
```

```objc
- (void) removeTrack:(AVMovieTrack *) track;
```

## Parameters

- `track`: The movie to be removed.

## See Also

### Managing tracks
- [func mutableTrack(compatibleWith: AVAssetTrack) -> AVMutableMovieTrack?](./mutabletrack%28compatiblewith%29.md)
  Provides a reference to a track from a mutable movie into which you can insert any time range.
- [func addMutableTrack(withMediaType: AVMediaType, copySettingsFrom: AVAssetTrack?, options: [String : Any]?) -> AVMutableMovieTrack?](./addmutabletrack%28withmediatype,copysettingsfrom,options%29.md)
  Adds an empty track to the target movie.
- [func addMutableTracksCopyingSettings(from: [AVAssetTrack], options: [String : Any]?) -> [AVMutableMovieTrack]](./addmutabletrackscopyingsettings%28from,options%29.md)
  Adds one or more empty tracks to the target movie and copies the track settings from the source tracks.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmutablemovie/removetrack(_:))*