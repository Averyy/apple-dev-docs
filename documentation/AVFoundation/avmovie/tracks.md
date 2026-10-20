# tracks

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The tracks that a movie contains.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
var tracks: [AVMovieTrack] { get }
```

```objc
@property (nonatomic, readonly) NSArray<AVMovieTrack *> * tracks;
```

## See Also

### Accessing tracks
- [func track(withTrackID: CMPersistentTrackID) -> AVMovieTrack?](./track%28withtrackid%29.md)
  Retrieves a track in the movie that contains the specified identifier.
- [func tracks(withMediaType: AVMediaType) -> [AVMovieTrack]](./tracks%28withmediatype%29.md)
  Retrieves tracks in the movie that present media of the specified type.
- [func tracks(withMediaCharacteristic: AVMediaCharacteristic) -> [AVMovieTrack]](./tracks%28withmediacharacteristic%29.md)
  Retrieves tracks in the movie that present media of the specified characteristic.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmovie/tracks)*