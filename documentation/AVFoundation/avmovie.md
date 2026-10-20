# AVMovie

**Framework**: AVFoundation  
**Kind**: class  
**Role**: Class

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

```objc
@interface AVMovie : AVAsset
```

#### Overview

`AVMovie` supports operations involving the format-specific portions of the QuickTime movie model that [`AVAsset`](./avasset.md) doesn’t support. For instance, retrieving the movie header from an existing QuickTime movie file. You can also use `AVMovie` to write a movie header into a new file, thereby creating a reference movie.

## Topics

### Creating a movie
- [convenience init(url: URL)](./avmovie/init%28url%29.md)
  Creates a movie that models the media at the specified URL.
- [init(url: URL, options: [String : Any]?)](./avmovie/init%28url,options%29-1wjrq.md)
  Creates a movie object from a movie header stored in a QuickTime movie file of ISO base media file.
- [init(data: Data, options: [String : Any]?)](./avmovie/init%28data,options%29.md)
  Creates a movie object from a movie file’s data.
- [Initialization options](./initialization-options.md)
  Specify options to configure the initialization of a movie.
### Determining supported file types
- [class func movieTypes() -> [AVFileType]](./avmovie/movietypes%28%29.md)
  Returns the file types that a movie supports.
### Loading tracks
- [static var tracks: AVAsyncProperty<Root, [AVMovieTrack]>](./avpartialasyncproperty/tracks-80a83.md)
  The tracks that a movie contains.
- [func loadTrack(withTrackID: CMPersistentTrackID, completionHandler: (AVMovieTrack?, (any Error)?) -> Void)](./avmovie/loadtrack%28withtrackid,completionhandler%29.md)
  Loads a track that contains the specified identifier.
- [func loadTracks(withMediaType: AVMediaType, completionHandler: ([AVMovieTrack]?, (any Error)?) -> Void)](./avmovie/loadtracks%28withmediatype,completionhandler%29.md)
  Loads tracks that contain media of a specified type.
- [func loadTracks(withMediaCharacteristic: AVMediaCharacteristic, completionHandler: ([AVMovieTrack]?, (any Error)?) -> Void)](./avmovie/loadtracks%28withmediacharacteristic,completionhandler%29.md)
  Loads tracks that contain media of a specified characteristic.
### Creating and writing headers
- [func `is`(compatibleWithFileType: AVFileType) -> Bool](./avmovie/is%28compatiblewithfiletype%29.md)
  Returns a Boolean value that indicates whether the system can create a movie header of the specified type.
- [func makeMovieHeader(fileType: AVFileType) throws -> Data](./avmovie/makemovieheader%28filetype%29.md)
  Creates a header for a movie for the specified file type.
- [func writeHeader(to: URL, fileType: AVFileType, options: AVMovieWritingOptions) throws](./avmovie/writeheader%28to,filetype,options%29.md)
  Writes the movie header to the specified URL.
- [struct AVMovieWritingOptions](./avmoviewritingoptions.md)
  A structure that defines options to control the writing of a movie header to a destination URL.
### Determining fragment support
- [var canContainMovieFragments: Bool](./avmovie/cancontainmoviefragments.md)
  A Boolean value that indicates whether fragments can extend the movie file.
- [var containsMovieFragments: Bool](./avmovie/containsmoviefragments.md)
  A Boolean value that indicates whether at least one movie fragment extends the movie file.
### Accessing movie information
- [var url: URL?](./avmovie/url.md)
  A URL to a QuickTime or ISO base media file.
- [var data: Data?](./avmovie/data.md)
  A data object that contains the movie file’s data.
### Accessing tracks
- [var tracks: [AVMovieTrack]](./avmovie/tracks.md)
  The tracks that a movie contains.
- [func track(withTrackID: CMPersistentTrackID) -> AVMovieTrack?](./avmovie/track%28withtrackid%29.md)
  Retrieves a track in the movie that contains the specified identifier.
- [func tracks(withMediaType: AVMediaType) -> [AVMovieTrack]](./avmovie/tracks%28withmediatype%29.md)
  Retrieves tracks in the movie that present media of the specified type.
- [func tracks(withMediaCharacteristic: AVMediaCharacteristic) -> [AVMovieTrack]](./avmovie/tracks%28withmediacharacteristic%29.md)
  Retrieves tracks in the movie that present media of the specified characteristic.
### Accessing data storage
- [var defaultMediaDataStorage: AVMediaDataStorage?](./avmovie/defaultmediadatastorage.md)
  The default storage container for media data added to a movie.
### Initializers
- [init(URL: URL, options: [String : Any]?)](./avmovie/init%28url,options%29-3tgg4.md)
- [convenience init(URL: URL, options: [String : Any]?)](./avmovie/init%28url,options%29-9sf6c.md)

## Relationships

### Inherits From
- [AVAsset](./avasset.md)
### Inherited By
- [AVFragmentedMovie](./avfragmentedmovie.md)
- [AVMutableMovie](./avmutablemovie.md)
### Conforms To
- [AVAsynchronousKeyValueLoading](./avasynchronouskeyvalueloading.md)
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSMutableCopying](../Foundation/nsmutablecopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Movies
- [class AVMovieTrack](./avmovietrack.md)
  A track in a movie that conforms to the QuickTime or ISO base media file format.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmovie)*