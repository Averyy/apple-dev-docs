# addMutableTrack(withMediaType:copySettingsFrom:options:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (AVMutableMovieTrack *) addMutableTrackWithMediaType:(AVMediaType) mediaType copySettingsFromTrack:(AVAssetTrack *) track options:(NSDictionary<NSString *,id> *) options;
```

#### Return Value

An [`AVMutableMovieTrack`](../avmutablemovietrack.md) object.

## Parameters

- `mediaType`: The media type for the new track.
- `track`: An [`AVAssetTrack`](../avassettrack.md) containing the desired track settings to be transferred. Set to `nil` to create a track with default settings.
- `options`: A dictionary that contains key for specifying the movie object initialization. Currently, no keys are defined.

## See Also

### Managing tracks
- [func mutableTrack(compatibleWith: AVAssetTrack) -> AVMutableMovieTrack?](./mutabletrack%28compatiblewith%29.md)
  Provides a reference to a track from a mutable movie into which you can insert any time range.
- [func addMutableTracksCopyingSettings(from: [AVAssetTrack], options: [String : Any]?) -> [AVMutableMovieTrack]](./addmutabletrackscopyingsettings%28from,options%29.md)
  Adds one or more empty tracks to the target movie and copies the track settings from the source tracks.
- [func removeTrack(AVMovieTrack)](./removetrack%28_%29.md)
  Removes the specified track from the target movie.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmutablemovie/addmutabletrack(withmediatype:copysettingsfrom:options:))*