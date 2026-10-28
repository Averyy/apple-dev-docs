# track(withTrackID:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (AVMutableMovieTrack *) trackWithTrackID:(CMPersistentTrackID) trackID;
```

## Return Value

A movie track, or `nil` if there is no track with the identifier.

## Discussion

Apple discourages using this method in iOS 15, tvOS 15, macOS 12, and watchOS 8 or later. Load a track asynchronously using [`loadTrack(withTrackID:completionHandler:)`](./loadtrack%28withtrackid,completionhandler%29.md) instead.

## Parameters

- `trackID`: The track identifier for the requested track.

## See Also

### Accessing tracks
- [var tracks: [AVMutableMovieTrack]](./tracks.md)
  The tracks that a movie contains.
- [func tracks(withMediaType: AVMediaType) -> [AVMutableMovieTrack]](./tracks%28withmediatype%29.md)
  Retrieves tracks in the movie that present media of the specified type.
- [func tracks(withMediaCharacteristic: AVMediaCharacteristic) -> [AVMutableMovieTrack]](./tracks%28withmediacharacteristic%29.md)
  Retrieve tracks in the movie that present media of the specified characteristic.
- [func unusedTrackID() -> CMPersistentTrackID](./unusedtrackid%28%29.md)
  Returns an identifier that no other tracks in the asset use.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmutablemovie/track(withtrackid:))*