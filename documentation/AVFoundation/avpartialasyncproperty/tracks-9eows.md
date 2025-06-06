# tracks

**Framework**: AVFoundation  
**Kind**: property

The tracks that a composition contains.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst ?+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
static var tracks: AVAsyncProperty<Root, [AVCompositionTrack]> { get }
```

## See Also

- [func loadTrack(withTrackID: CMPersistentTrackID, completionHandler: (AVCompositionTrack?, (any Error)?) -> Void)](avcomposition/loadtrack(withtrackid:completionhandler:).md)
  Loads a track that contains the specified identifier.
- [func loadTracks(withMediaType: AVMediaType, completionHandler: ([AVCompositionTrack]?, (any Error)?) -> Void)](avcomposition/loadtracks(withmediatype:completionhandler:).md)
  Loads tracks that contain media of a specified type.
- [func loadTracks(withMediaCharacteristic: AVMediaCharacteristic, completionHandler: ([AVCompositionTrack]?, (any Error)?) -> Void)](avcomposition/loadtracks(withmediacharacteristic:completionhandler:).md)
  Loads tracks that contain media of a specified characteristic.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avpartialasyncproperty/tracks-9eows)*