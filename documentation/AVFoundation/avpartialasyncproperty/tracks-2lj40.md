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
static var tracks: AVAsyncProperty<Root, [AVMutableMovieTrack]> { get }
```

Available when `Root` inherits `AVMutableMovie`.

## Discussion

Use the [`load(_:isolation:)`](../avasynchronouskeyvalueloading/load%28_,isolation%29.md) method to retrieve the property value.

## See Also

### Loading tracks
- [func loadTrack(withTrackID: CMPersistentTrackID, completionHandler: (AVMutableMovieTrack?, (any Error)?) -> Void)](../avmutablemovie/loadtrack%28withtrackid,completionhandler%29.md)
  Loads a track that contains the specified identifier.
- [func loadTracks(withMediaType: AVMediaType, completionHandler: ([AVMutableMovieTrack]?, (any Error)?) -> Void)](../avmutablemovie/loadtracks%28withmediatype,completionhandler%29.md)
  Loads tracks that contain media of a specified type.
- [func loadTracks(withMediaCharacteristic: AVMediaCharacteristic, completionHandler: ([AVMutableMovieTrack]?, (any Error)?) -> Void)](../avmutablemovie/loadtracks%28withmediacharacteristic,completionhandler%29.md)
  Loads tracks that contain media of a specified characteristic.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avpartialasyncproperty/tracks-2lj40)*