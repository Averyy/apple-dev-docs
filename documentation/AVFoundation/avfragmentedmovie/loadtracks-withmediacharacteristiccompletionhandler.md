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
func loadTracks(withMediaCharacteristic mediaCharacteristic: AVMediaCharacteristic) async throws -> [AVFragmentedMovieTrack]
```

## Parameters

- `mediaCharacteristic`: The media characteristic of the tracks to load.
- `completionHandler`: A callback that the system invokes after it finishes the loading request. It passes the completion handler the following parameters:

## See Also

- [static var tracks: AVAsyncProperty<Root, [AVFragmentedMovieTrack]>](avpartialasyncproperty/tracks-7fr6q.md)
  The tracks that a movie contains.
- [func loadTrack(withTrackID: CMPersistentTrackID, completionHandler: (AVFragmentedMovieTrack?, (any Error)?) -> Void)](avfragmentedmovie/loadtrack(withtrackid:completionhandler:).md)
  Loads a track that contains the specified identifier.
- [func loadTracks(withMediaType: AVMediaType, completionHandler: ([AVFragmentedMovieTrack]?, (any Error)?) -> Void)](avfragmentedmovie/loadtracks(withmediatype:completionhandler:).md)
  Loads tracks that contain media of a specified type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avfragmentedmovie/loadtracks(withmediacharacteristic:completionhandler:))*