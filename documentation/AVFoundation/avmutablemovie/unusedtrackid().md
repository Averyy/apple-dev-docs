# unusedTrackID()

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

Returns an identifier that no other tracks in the asset use.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
func unusedTrackID() -> CMPersistentTrackID
```

```objc
- (CMPersistentTrackID) unusedTrackID;
```

#### Return Value

An unused [`CMPersistentTrackID`](../../CoreMedia/cmpersistenttrackid.md) value.

## See Also

### Accessing tracks
- [var tracks: [AVMutableMovieTrack]](./tracks.md)
  The tracks that a movie contains.
- [func track(withTrackID: CMPersistentTrackID) -> AVMutableMovieTrack?](./track%28withtrackid%29.md)
  Retrieves a track in the movie that contains the specified identifier.
- [func tracks(withMediaType: AVMediaType) -> [AVMutableMovieTrack]](./tracks%28withmediatype%29.md)
  Retrieves tracks in the movie that present media of the specified type.
- [func tracks(withMediaCharacteristic: AVMediaCharacteristic) -> [AVMutableMovieTrack]](./tracks%28withmediacharacteristic%29.md)
  Retrieve tracks in the movie that present media of the specified characteristic.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmutablemovie/unusedtrackid())*