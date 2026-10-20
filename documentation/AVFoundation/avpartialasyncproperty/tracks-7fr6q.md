# tracks

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Type Property

The tracks that a movie contains.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
static var tracks: AVAsyncProperty<Root, [AVFragmentedMovieTrack]> { get }
```

Available when `Root` inherits `AVFragmentedMovie`.

## See Also

### Loading tracks
- [func loadTrack(withTrackID: CMPersistentTrackID, completionHandler: (AVFragmentedMovieTrack?, (any Error)?) -> Void)](../avfragmentedmovie/loadtrack%28withtrackid,completionhandler%29.md)
  Loads a track that contains the specified identifier.
- [func loadTracks(withMediaType: AVMediaType, completionHandler: ([AVFragmentedMovieTrack]?, (any Error)?) -> Void)](../avfragmentedmovie/loadtracks%28withmediatype,completionhandler%29.md)
  Loads tracks that contain media of a specified type.
- [func loadTracks(withMediaCharacteristic: AVMediaCharacteristic, completionHandler: ([AVFragmentedMovieTrack]?, (any Error)?) -> Void)](../avfragmentedmovie/loadtracks%28withmediacharacteristic,completionhandler%29.md)
  Loads tracks that contain media of a specified characteristic.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avpartialasyncproperty/tracks-7fr6q)*