# tracks

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The tracks that a movie contains.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
var tracks: [AVMutableMovieTrack] { get }
```

```objc
@property (nonatomic, readonly) NSArray<AVMutableMovieTrack *> * tracks;
```

## See Also

### Accessing tracks
- [func track(withTrackID: CMPersistentTrackID) -> AVMutableMovieTrack?](./track%28withtrackid%29.md)
  Retrieves a track in the movie that contains the specified identifier.
- [func tracks(withMediaType: AVMediaType) -> [AVMutableMovieTrack]](./tracks%28withmediatype%29.md)
  Retrieves tracks in the movie that present media of the specified type.
- [func tracks(withMediaCharacteristic: AVMediaCharacteristic) -> [AVMutableMovieTrack]](./tracks%28withmediacharacteristic%29.md)
  Retrieve tracks in the movie that present media of the specified characteristic.
- [func unusedTrackID() -> CMPersistentTrackID](./unusedtrackid%28%29.md)
  Returns an identifier that no other tracks in the asset use.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmutablemovie/tracks)*