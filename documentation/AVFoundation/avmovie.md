# AVMovie

**Framework**: AVFoundation  
**Kind**: class

An object that represents an audiovisual container that conforms to the QuickTime movie file format or a related format like MPEG-4.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
class AVMovie
```

#### Overview

`AVMovie` supports operations involving the format-specific portions of the QuickTime movie model that [`AVAsset`](avasset.md) doesn’t support. For instance, retrieving the movie header from an existing QuickTime movie file. You can also use `AVMovie` to write a movie header into a new file, thereby creating a reference movie.

## Topics

### Creating a Movie
- [convenience init(url: URL)](avmovie/init(url:).md)
  Creates a movie that models the media at the specified URL.
- [init(url: URL, options: [String : Any]?)](avmovie/init(url:options:).md)
  Creates a movie object from a movie header stored in a QuickTime movie file of ISO base media file.
- [init(data: Data, options: [String : Any]?)](avmovie/init(data:options:).md)
  Creates a movie object from a movie file’s data.
- [Initialization Options](initialization-options.md)
  Specify options to configure the initialization of a movie.
### Determining Supported File Types
- [class func movieTypes() -> [AVFileType]](avmovie/movietypes.md)
  Returns the file types that a movie supports.
### Loading Tracks
- [static var tracks: AVAsyncProperty<Root, [AVMovieTrack]>](avpartialasyncproperty/tracks-80a83.md)
  The tracks that a movie contains.
- [func loadTrack(withTrackID: CMPersistentTrackID, completionHandler: (AVMovieTrack?, (any Error)?) -> Void)](avmovie/loadtrack(withtrackid:completionhandler:).md)
  Loads a track that contains the specified identifier.
- [func loadTracks(withMediaType: AVMediaType, completionHandler: ([AVMovieTrack]?, (any Error)?) -> Void)](avmovie/loadtracks(withmediatype:completionhandler:).md)
  Loads tracks that contain media of a specified type.
- [func loadTracks(withMediaCharacteristic: AVMediaCharacteristic, completionHandler: ([AVMovieTrack]?, (any Error)?) -> Void)](avmovie/loadtracks(withmediacharacteristic:completionhandler:).md)
  Loads tracks that contain media of a specified characteristic.
### Creating and Writing Headers
- [func `is`(compatibleWithFileType: AVFileType) -> Bool](avmovie/is(compatiblewithfiletype:).md)
  Returns a Boolean value that indicates whether the system can create a movie header of the specified type.
- [func makeMovieHeader(fileType: AVFileType) throws -> Data](avmovie/makemovieheader(filetype:).md)
  Creates a header for a movie for the specified file type.
- [func writeHeader(to: URL, fileType: AVFileType, options: AVMovieWritingOptions) throws](avmovie/writeheader(to:filetype:options:).md)
  Writes the movie header to the specified URL.
- [struct AVMovieWritingOptions](avmoviewritingoptions.md)
  A structure that defines options to control the writing of a movie header to a destination URL.
### Determining Fragment Support
- [var canContainMovieFragments: Bool](avmovie/cancontainmoviefragments.md)
  A Boolean value that indicates whether fragments can extend the movie file.
- [var containsMovieFragments: Bool](avmovie/containsmoviefragments.md)
  A Boolean value that indicates whether at least one movie fragment extends the movie file.
### Accessing Movie Information
- [var url: URL?](avmovie/url.md)
  A URL to a QuickTime or ISO base media file.
- [var data: Data?](avmovie/data.md)
  A data object that contains the movie file’s data.
### Accessing Tracks
- [var tracks: [AVMovieTrack]](avmovie/tracks.md)
  The tracks that a movie contains.
- [func track(withTrackID: CMPersistentTrackID) -> AVMovieTrack?](avmovie/track(withtrackid:).md)
  Retrieves a track in the movie that contains the specified identifier.
- [func tracks(withMediaType: AVMediaType) -> [AVMovieTrack]](avmovie/tracks(withmediatype:).md)
  Retrieves tracks in the movie that present media of the specified type.
- [func tracks(withMediaCharacteristic: AVMediaCharacteristic) -> [AVMovieTrack]](avmovie/tracks(withmediacharacteristic:).md)
  Retrieves tracks in the movie that present media of the specified characteristic.
### Accessing Data Storage
- [var defaultMediaDataStorage: AVMediaDataStorage?](avmovie/defaultmediadatastorage.md)
  The default storage container for media data added to a movie.

## Relationships

### Inherits From
- [AVAsset](avasset.md)
### Inherited By
- [AVFragmentedMovie](avfragmentedmovie.md)
- [AVMutableMovie](avmutablemovie.md)
### Conforms To
- [AVAsynchronousKeyValueLoading](avasynchronouskeyvalueloading.md)
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSMutableCopying](../Foundation/NSMutableCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class AVMovieTrack](avmovietrack.md)
  A track in a movie that conforms to the QuickTime or ISO base media file format.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmovie)*