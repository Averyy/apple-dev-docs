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
static var tracks: AVAsyncProperty<Root, [AVMovieTrack]> { get }
```

#### Discussion

Use the `AVAsynchronousKeyValueLoading/load(_:)` method to retrieve the property value.

## See Also

- [func loadTrack(withTrackID: CMPersistentTrackID, completionHandler: (AVMovieTrack?, (any Error)?) -> Void)](avmovie/loadtrack(withtrackid:completionhandler:).md)
  Loads a track that contains the specified identifier.
- [func loadTracks(withMediaType: AVMediaType, completionHandler: ([AVMovieTrack]?, (any Error)?) -> Void)](avmovie/loadtracks(withmediatype:completionhandler:).md)
  Loads tracks that contain media of a specified type.
- [func loadTracks(withMediaCharacteristic: AVMediaCharacteristic, completionHandler: ([AVMovieTrack]?, (any Error)?) -> Void)](avmovie/loadtracks(withmediacharacteristic:completionhandler:).md)
  Loads tracks that contain media of a specified characteristic.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avpartialasyncproperty/tracks-80a83)*