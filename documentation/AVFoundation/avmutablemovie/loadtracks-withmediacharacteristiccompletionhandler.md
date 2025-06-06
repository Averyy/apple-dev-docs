# loadTracks(withMediaCharacteristic:completionHandler:)

**Framework**: AVFoundation  
**Kind**: method

Loads tracks that contain media of a specified characteristic.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
func loadTracks(withMediaCharacteristic mediaCharacteristic: AVMediaCharacteristic) async throws -> [AVMutableMovieTrack]
```

## Parameters

- `mediaCharacteristic`: The media characteristic of the tracks to load.
- `completionHandler`: A callback that the system invokes after it finishes the loading request. It passes the completion handler the following parameters:

## See Also

- [static var tracks: AVAsyncProperty<Root, [AVMutableMovieTrack]>](avpartialasyncproperty/tracks-2lj40.md)
  The tracks that a movie contains.
- [func loadTrack(withTrackID: CMPersistentTrackID, completionHandler: (AVMutableMovieTrack?, (any Error)?) -> Void)](avmutablemovie/loadtrack(withtrackid:completionhandler:).md)
  Loads a track that contains the specified identifier.
- [func loadTracks(withMediaType: AVMediaType, completionHandler: ([AVMutableMovieTrack]?, (any Error)?) -> Void)](avmutablemovie/loadtracks(withmediatype:completionhandler:).md)
  Loads tracks that contain media of a specified type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmutablemovie/loadtracks(withmediacharacteristic:completionhandler:))*