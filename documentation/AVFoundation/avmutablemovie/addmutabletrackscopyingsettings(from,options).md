# addMutableTracksCopyingSettings(from:options:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

Adds one or more empty tracks to the target movie and copies the track settings from the source tracks.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
func addMutableTracksCopyingSettings(from existingTracks: [AVAssetTrack], options: [String : Any]? = nil) -> [AVMutableMovieTrack]
```

```objc
- (NSArray<AVMutableMovieTrack *> *) addMutableTracksCopyingSettingsFromTracks:(NSArray<AVAssetTrack *> *) existingTracks options:(NSDictionary<NSString *,id> *) options;
```

## Return Value

An array of [`AVMutableMovieTrack`](../avmutablemovietrack.md) objects. The index of a track in this array is the same as the index of its source track in the `existingTracks` array.

## Discussion

Properties involving pairs of tracks,such as track references, are copied from the source tracks to the target tracks.

## Parameters

- `existingTracks`: An array of asset tracks to be added.
- `options`: A dictionary that contains key for specifying the movie object initialization. Currently, no keys are defined.

## See Also

### Managing tracks
- [func mutableTrack(compatibleWith: AVAssetTrack) -> AVMutableMovieTrack?](./mutabletrack%28compatiblewith%29.md)
  Provides a reference to a track from a mutable movie into which you can insert any time range.
- [func addMutableTrack(withMediaType: AVMediaType, copySettingsFrom: AVAssetTrack?, options: [String : Any]?) -> AVMutableMovieTrack?](./addmutabletrack%28withmediatype,copysettingsfrom,options%29.md)
  Adds an empty track to the target movie.
- [func removeTrack(AVMovieTrack)](./removetrack%28_%29.md)
  Removes the specified track from the target movie.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmutablemovie/addmutabletrackscopyingsettings(from:options:))*