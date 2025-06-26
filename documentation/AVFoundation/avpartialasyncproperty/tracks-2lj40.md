# tracks

**Framework**: AVFoundation  
**Kind**: property

The tracks that a movie contains.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst ?+
- macOS 12.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
static var tracks: AVAsyncProperty<Root, [AVMutableMovieTrack]> { get }
```

#### Discussion

Use the [`load(_:isolation:)`](avasynchronouskeyvalueloading/load(_:isolation:).md) method to retrieve the property value.

## See Also

- [func loadTrack(withTrackID: CMPersistentTrackID, completionHandler: (AVMutableMovieTrack?, (any Error)?) -> Void)](avmutablemovie/loadtrack(withtrackid:completionhandler:).md)
  Loads a track that contains the specified identifier.
- [func loadTracks(withMediaType: AVMediaType, completionHandler: ([AVMutableMovieTrack]?, (any Error)?) -> Void)](avmutablemovie/loadtracks(withmediatype:completionhandler:).md)
  Loads tracks that contain media of a specified type.
- [func loadTracks(withMediaCharacteristic: AVMediaCharacteristic, completionHandler: ([AVMutableMovieTrack]?, (any Error)?) -> Void)](avmutablemovie/loadtracks(withmediacharacteristic:completionhandler:).md)
  Loads tracks that contain media of a specified characteristic.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avpartialasyncproperty/tracks-2lj40)*