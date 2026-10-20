# AVFragmentedMovie

**Framework**: AVFoundation  
**Kind**: class  
**Role**: Class

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

```objc
@interface AVFragmentedMovie : AVMovie
```

## Topics

### Loading tracks
- [static var tracks: AVAsyncProperty<Root, [AVFragmentedMovieTrack]>](./avpartialasyncproperty/tracks-7fr6q.md)
  The tracks that a movie contains.
- [func loadTrack(withTrackID: CMPersistentTrackID, completionHandler: (AVFragmentedMovieTrack?, (any Error)?) -> Void)](./avfragmentedmovie/loadtrack%28withtrackid,completionhandler%29.md)
  Loads a track that contains the specified identifier.
- [func loadTracks(withMediaType: AVMediaType, completionHandler: ([AVFragmentedMovieTrack]?, (any Error)?) -> Void)](./avfragmentedmovie/loadtracks%28withmediatype,completionhandler%29.md)
  Loads tracks that contain media of a specified type.
- [func loadTracks(withMediaCharacteristic: AVMediaCharacteristic, completionHandler: ([AVFragmentedMovieTrack]?, (any Error)?) -> Void)](./avfragmentedmovie/loadtracks%28withmediacharacteristic,completionhandler%29.md)
  Loads tracks that contain media of a specified characteristic.
### Accessing tracks
- [var tracks: [AVFragmentedMovieTrack]](./avfragmentedmovie/tracks.md)
  The tracks that a movie contains.
- [func track(withTrackID: CMPersistentTrackID) -> AVFragmentedMovieTrack?](./avfragmentedmovie/track%28withtrackid%29.md)
  Retrieves a track in the movie that contains the specified identifier.
- [func tracks(withMediaType: AVMediaType) -> [AVFragmentedMovieTrack]](./avfragmentedmovie/tracks%28withmediatype%29.md)
  Retrieves tracks in the movie that present media of the specified type.
- [func tracks(withMediaCharacteristic: AVMediaCharacteristic) -> [AVFragmentedMovieTrack]](./avfragmentedmovie/tracks%28withmediacharacteristic%29.md)
  Retrieves tracks in the movie that present media of the specified characteristic.

## Relationships

### Inherits From
- [AVMovie](./avmovie.md)
### Conforms To
- [AVAsynchronousKeyValueLoading](./avasynchronouskeyvalueloading.md)
- [AVFragmentMinding](./avfragmentminding.md)
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSMutableCopying](../Foundation/nsmutablecopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Fragmented movies
- [class AVFragmentedMovieTrack](./avfragmentedmovietrack.md)
  An object that represents a track in a fragmented movie.
- [class AVFragmentedMovieMinder](./avfragmentedmovieminder.md)
  An object that checks whether a fragmented movie appends additional movie fragments.
- [protocol AVFragmentMinding](./avfragmentminding.md)
  A protocol that defines whether an asset supports fragment minding.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avfragmentedmovie)*