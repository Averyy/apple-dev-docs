# loadTrack(withTrackID:completionHandler:)

**Framework**: AVFoundation  
**Kind**: method

Loads a track that contains the specified identifier.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
func loadTrack(withTrackID trackID: CMPersistentTrackID) async throws -> AVMovieTrack?
```

## Parameters

- `trackID`: The identifier of the track to load.
- `completionHandler`: A callback that the system invokes after it finishes the loading request. It passes the completion handler the following parameters:

## See Also

- [static var tracks: AVAsyncProperty<Root, [AVMovieTrack]>](avpartialasyncproperty/tracks-80a83.md)
  The tracks that a movie contains.
- [func loadTracks(withMediaType: AVMediaType, completionHandler: ([AVMovieTrack]?, (any Error)?) -> Void)](avmovie/loadtracks(withmediatype:completionhandler:).md)
  Loads tracks that contain media of a specified type.
- [func loadTracks(withMediaCharacteristic: AVMediaCharacteristic, completionHandler: ([AVMovieTrack]?, (any Error)?) -> Void)](avmovie/loadtracks(withmediacharacteristic:completionhandler:).md)
  Loads tracks that contain media of a specified characteristic.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmovie/loadtrack(withtrackid:completionhandler:))*