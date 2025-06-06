# AVFragmentedMovie

**Framework**: AVFoundation  
**Kind**: class

An object that represents a fragmented movie file.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
class AVFragmentedMovie
```

## Topics

### Loading Tracks
- [static var tracks: AVAsyncProperty<Root, [AVFragmentedMovieTrack]>](avpartialasyncproperty/tracks-7fr6q.md)
  The tracks that a movie contains.
- [func loadTrack(withTrackID: CMPersistentTrackID, completionHandler: (AVFragmentedMovieTrack?, (any Error)?) -> Void)](avfragmentedmovie/loadtrack(withtrackid:completionhandler:).md)
  Loads a track that contains the specified identifier.
- [func loadTracks(withMediaType: AVMediaType, completionHandler: ([AVFragmentedMovieTrack]?, (any Error)?) -> Void)](avfragmentedmovie/loadtracks(withmediatype:completionhandler:).md)
  Loads tracks that contain media of a specified type.
- [func loadTracks(withMediaCharacteristic: AVMediaCharacteristic, completionHandler: ([AVFragmentedMovieTrack]?, (any Error)?) -> Void)](avfragmentedmovie/loadtracks(withmediacharacteristic:completionhandler:).md)
  Loads tracks that contain media of a specified characteristic.
### Accessing Tracks
- [var tracks: [AVFragmentedMovieTrack]](avfragmentedmovie/tracks.md)
  The tracks that a movie contains.
- [func track(withTrackID: CMPersistentTrackID) -> AVFragmentedMovieTrack?](avfragmentedmovie/track(withtrackid:).md)
  Retrieves a track in the movie that contains the specified identifier.
- [func tracks(withMediaType: AVMediaType) -> [AVFragmentedMovieTrack]](avfragmentedmovie/tracks(withmediatype:).md)
  Retrieves tracks in the movie that present media of the specified type.
- [func tracks(withMediaCharacteristic: AVMediaCharacteristic) -> [AVFragmentedMovieTrack]](avfragmentedmovie/tracks(withmediacharacteristic:).md)
  Retrieves tracks in the movie that present media of the specified characteristic.

## Relationships

### Inherits From
- [AVMovie](avmovie.md)
### Conforms To
- [AVAsynchronousKeyValueLoading](avasynchronouskeyvalueloading.md)
- [AVFragmentMinding](avfragmentminding.md)
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSMutableCopying](../Foundation/NSMutableCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [class AVFragmentedMovieTrack](avfragmentedmovietrack.md)
  An object that represents a track in a fragmented movie.
- [class AVFragmentedMovieMinder](avfragmentedmovieminder.md)
  An object that checks whether a fragmented movie appends additional movie fragments.
- [protocol AVFragmentMinding](avfragmentminding.md)
  A protocol that defines whether an asset supports fragment minding.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avfragmentedmovie)*