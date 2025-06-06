# AVAudioSequencer.InfoDictionaryKey

**Framework**: AVFAudio  
**Kind**: struct

Constants that defines metadata keys for a sequencer.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
struct InfoDictionaryKey
```

## Topics

### Getting Album Details
- [static let album: AVAudioSequencer.InfoDictionaryKey](avaudiosequencer/infodictionarykey/album.md)
  A key that represents the album.
- [static let artist: AVAudioSequencer.InfoDictionaryKey](avaudiosequencer/infodictionarykey/artist.md)
  A key that represents the artist.
- [static let comments: AVAudioSequencer.InfoDictionaryKey](avaudiosequencer/infodictionarykey/comments.md)
  A key that represents the comments.
- [static let composer: AVAudioSequencer.InfoDictionaryKey](avaudiosequencer/infodictionarykey/composer.md)
  A key that represents the composer.
- [static let copyright: AVAudioSequencer.InfoDictionaryKey](avaudiosequencer/infodictionarykey/copyright.md)
  A key that represents the copyright statement.
- [static let genre: AVAudioSequencer.InfoDictionaryKey](avaudiosequencer/infodictionarykey/genre.md)
  A key that represents the genre.
- [static let lyricist: AVAudioSequencer.InfoDictionaryKey](avaudiosequencer/infodictionarykey/lyricist.md)
  A key that represents the lyricist.
- [static let title: AVAudioSequencer.InfoDictionaryKey](avaudiosequencer/infodictionarykey/title.md)
  A key that represents the title.
- [static let trackNumber: AVAudioSequencer.InfoDictionaryKey](avaudiosequencer/infodictionarykey/tracknumber.md)
  A key that represents the track number.
- [static let subTitle: AVAudioSequencer.InfoDictionaryKey](avaudiosequencer/infodictionarykey/subtitle.md)
  A key that represents the subtitle.
- [static let year: AVAudioSequencer.InfoDictionaryKey](avaudiosequencer/infodictionarykey/year.md)
  A key that represents the year.
### Getting the Duration and Time
- [static let approximateDurationInSeconds: AVAudioSequencer.InfoDictionaryKey](avaudiosequencer/infodictionarykey/approximatedurationinseconds.md)
  A key that represents the approximate duration.
- [static let timeSignature: AVAudioSequencer.InfoDictionaryKey](avaudiosequencer/infodictionarykey/timesignature.md)
  A key that represents the time signature.
- [static let tempo: AVAudioSequencer.InfoDictionaryKey](avaudiosequencer/infodictionarykey/tempo.md)
  A key that represents the tempo.
### Getting the Recording Date
- [static let recordedDate: AVAudioSequencer.InfoDictionaryKey](avaudiosequencer/infodictionarykey/recordeddate.md)
  A key that represents the date of the recording.
### Getting Encoding Information
- [static let encodingApplication: AVAudioSequencer.InfoDictionaryKey](avaudiosequencer/infodictionarykey/encodingapplication.md)
  A key that represents the encoding application.
- [static let sourceEncoder: AVAudioSequencer.InfoDictionaryKey](avaudiosequencer/infodictionarykey/sourceencoder.md)
  A key that represents the encoder the source uses.
- [static let nominalBitRate: AVAudioSequencer.InfoDictionaryKey](avaudiosequencer/infodictionarykey/nominalbitrate.md)
  A key that represents the nominal bit rate.
- [static let sourceBitDepth: AVAudioSequencer.InfoDictionaryKey](avaudiosequencer/infodictionarykey/sourcebitdepth.md)
  A key that represents the bit depth of the source.
- [static let keySignature: AVAudioSequencer.InfoDictionaryKey](avaudiosequencer/infodictionarykey/keysignature.md)
  A key that represents the key signature.
### Getting the Channel Layout
- [static let channelLayout: AVAudioSequencer.InfoDictionaryKey](avaudiosequencer/infodictionarykey/channellayout.md)
  A key that represents the channel layout.
### Getting the Recording Code
- [static let ISRC: AVAudioSequencer.InfoDictionaryKey](avaudiosequencer/infodictionarykey/isrc.md)
  A key that represents the international standard recording code.
### Creating a Dictionary Key
- [init(rawValue: String)](avaudiosequencer/infodictionarykey/init(rawvalue:).md)
  Creates a new instance with the raw value you specify.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var isPlaying: Bool](avaudiosequencer/isplaying.md)
  A Boolean value that indicates whether the sequencer’s player is in a playing state.
- [var rate: Float](avaudiosequencer/rate.md)
  The playback rate of the sequencer’s player.
- [var tracks: [AVMusicTrack]](avaudiosequencer/tracks.md)
  An array that contains all the tracks in the sequence.
- [var currentPositionInBeats: TimeInterval](avaudiosequencer/currentpositioninbeats.md)
  The current playback position, in beats.
- [var currentPositionInSeconds: TimeInterval](avaudiosequencer/currentpositioninseconds.md)
  The current playback position, in seconds.
- [var tempoTrack: AVMusicTrack](avaudiosequencer/tempotrack.md)
  The track that contains tempo information about the sequence.
- [var userInfo: [String : Any]](avaudiosequencer/userinfo.md)
  A dictionary that contains metadata from a sequence.
- [func data(withSMPTEResolution: Int, error: NSErrorPointer) -> Data](avaudiosequencer/data(withsmpteresolution:error:).md)
  Gets a data object that contains the events from the sequence.
- [var AVMusicTimeStampEndOfTrack: Double](avmusictimestampendoftrack.md)
  A timestamp you use to access all events in a music track through a beat range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosequencer/infodictionarykey)*