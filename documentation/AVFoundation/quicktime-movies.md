# QuickTime movies

**Framework**: AVFoundation

Access the contents of a QuickTime movie file, and perform sample-level edits of its media tracks.

## Topics

### Movies
- [class AVMovie](avmovie.md)
  An object that represents an audiovisual container that conforms to the QuickTime movie file format or a related format like MPEG-4.
- [class AVMovieTrack](avmovietrack.md)
  A track in a movie that conforms to the QuickTime or ISO base media file format.
### Mutable movies
- [class AVMutableMovie](avmutablemovie.md)
  A mutable object that represents an audiovisual container that conforms to the QuickTime movie file format or a related format like MPEG-4.
- [class AVMutableMovieTrack](avmutablemovietrack.md)
  A mutable track that conforms to the QuickTime or ISO base media file format.
### Fragmented movies
- [class AVFragmentedMovie](avfragmentedmovie.md)
  An object that represents a fragmented movie file.
- [class AVFragmentedMovieTrack](avfragmentedmovietrack.md)
  An object that represents a track in a fragmented movie.
- [class AVFragmentedMovieMinder](avfragmentedmovieminder.md)
  An object that checks whether a fragmented movie appends additional movie fragments.
- [protocol AVFragmentMinding](avfragmentminding.md)
  A protocol that defines whether an asset supports fragment minding.
### Sample cursors
- [class AVSampleCursor](avsamplecursor.md)
  An object that provides information about the media sample at the cursor’s current position.
- [struct AVSampleCursorSyncInfo](avsamplecursorsyncinfo.md)
  A structure that describes the attributes of media samples to consider when resynchronizing a decoder.
- [struct AVSampleCursorDependencyInfo](avsamplecursordependencyinfo.md)
  A value for describing dependencies between a media sample and other media samples in the same sample sequence.
- [struct AVSampleCursorAudioDependencyInfo](avsamplecursoraudiodependencyinfo.md)
  A structure that describes the independent decodability of audio samples.
- [struct AVSampleCursorStorageRange](avsamplecursorstoragerange.md)
  A structure that indicates the offset and length of storage for a media sample or its chunk.
- [struct AVSampleCursorChunkInfo](avsamplecursorchunkinfo.md)
  A value that provides information about a chunk of media samples.
### Media data storage
- [class AVMediaDataStorage](avmediadatastorage.md)
  An object that represents the media sample data storage file.

## See Also

- [Composite assets](composite-assets.md)
  Combine tracks and segments of tracks from multiple assets into a composite asset that you can play or process.
- [Video effects](video-effects.md)
  Define standard video transition effects, synchronize layer animations with media timing, and create custom video compositors.
- [Audio mixing](audio-mixing.md)
  Define how to mix the audio levels from multiple audio tracks over an asset’s duration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/quicktime-movies)*