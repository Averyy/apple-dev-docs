# tracks

**Framework**: AVFoundation  
**Kind**: property

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

## See Also

- [func track(withTrackID: CMPersistentTrackID) -> AVMutableMovieTrack?](avmutablemovie/track(withtrackid:).md)
  Retrieves a track in the movie that contains the specified identifier.
- [func tracks(withMediaType: AVMediaType) -> [AVMutableMovieTrack]](avmutablemovie/tracks(withmediatype:).md)
  Retrieves tracks in the movie that present media of the specified type.
- [func tracks(withMediaCharacteristic: AVMediaCharacteristic) -> [AVMutableMovieTrack]](avmutablemovie/tracks(withmediacharacteristic:).md)
  Retrieve tracks in the movie that present media of the specified characteristic.
- [func unusedTrackID() -> CMPersistentTrackID](avmutablemovie/unusedtrackid.md)
  Returns an identifier that no other tracks in the asset use.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmutablemovie/tracks)*