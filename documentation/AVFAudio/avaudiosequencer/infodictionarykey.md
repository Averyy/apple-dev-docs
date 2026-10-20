# AVAudioSequencer.InfoDictionaryKey

**Framework**: AVFAudio  
**Kind**: struct  
**Role**: Structure

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

```c
typedef NSString * AVAudioSequencerInfoDictionaryKey;
```

## Topics

### Creating a dictionary key
- [init(rawValue: String)](./infodictionarykey/init%28rawvalue%29.md)
  Creates a new instance with the raw value you specify.
### Getting album details
- [static let album: AVAudioSequencer.InfoDictionaryKey](./infodictionarykey/album.md)
  A key that represents the album.
- [static let artist: AVAudioSequencer.InfoDictionaryKey](./infodictionarykey/artist.md)
  A key that represents the artist.
- [static let comments: AVAudioSequencer.InfoDictionaryKey](./infodictionarykey/comments.md)
  A key that represents the comments.
- [static let composer: AVAudioSequencer.InfoDictionaryKey](./infodictionarykey/composer.md)
  A key that represents the composer.
- [static let copyright: AVAudioSequencer.InfoDictionaryKey](./infodictionarykey/copyright.md)
  A key that represents the copyright statement.
- [static let genre: AVAudioSequencer.InfoDictionaryKey](./infodictionarykey/genre.md)
  A key that represents the genre.
- [static let lyricist: AVAudioSequencer.InfoDictionaryKey](./infodictionarykey/lyricist.md)
  A key that represents the lyricist.
- [static let title: AVAudioSequencer.InfoDictionaryKey](./infodictionarykey/title.md)
  A key that represents the title.
- [static let trackNumber: AVAudioSequencer.InfoDictionaryKey](./infodictionarykey/tracknumber.md)
  A key that represents the track number.
- [static let subTitle: AVAudioSequencer.InfoDictionaryKey](./infodictionarykey/subtitle.md)
  A key that represents the subtitle.
- [static let year: AVAudioSequencer.InfoDictionaryKey](./infodictionarykey/year.md)
  A key that represents the year.
### Getting the duration and time
- [static let approximateDurationInSeconds: AVAudioSequencer.InfoDictionaryKey](./infodictionarykey/approximatedurationinseconds.md)
  A key that represents the approximate duration.
- [static let timeSignature: AVAudioSequencer.InfoDictionaryKey](./infodictionarykey/timesignature.md)
  A key that represents the time signature.
- [static let tempo: AVAudioSequencer.InfoDictionaryKey](./infodictionarykey/tempo.md)
  A key that represents the tempo.
### Getting the recording date
- [static let recordedDate: AVAudioSequencer.InfoDictionaryKey](./infodictionarykey/recordeddate.md)
  A key that represents the date of the recording.
### Getting encoding information
- [static let encodingApplication: AVAudioSequencer.InfoDictionaryKey](./infodictionarykey/encodingapplication.md)
  A key that represents the encoding application.
- [static let sourceEncoder: AVAudioSequencer.InfoDictionaryKey](./infodictionarykey/sourceencoder.md)
  A key that represents the encoder the source uses.
- [static let nominalBitRate: AVAudioSequencer.InfoDictionaryKey](./infodictionarykey/nominalbitrate.md)
  A key that represents the nominal bit rate.
- [static let sourceBitDepth: AVAudioSequencer.InfoDictionaryKey](./infodictionarykey/sourcebitdepth.md)
  A key that represents the bit depth of the source.
- [static let keySignature: AVAudioSequencer.InfoDictionaryKey](./infodictionarykey/keysignature.md)
  A key that represents the key signature.
### Getting the channel layout
- [static let channelLayout: AVAudioSequencer.InfoDictionaryKey](./infodictionarykey/channellayout.md)
  A key that represents the channel layout.
### Getting the recording code
- [static let ISRC: AVAudioSequencer.InfoDictionaryKey](./infodictionarykey/isrc.md)
  A key that represents the international standard recording code.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Getting sequence properties
- [var isPlaying: Bool](./isplaying.md)
  A Boolean value that indicates whether the sequencer’s player is in a playing state.
- [var rate: Float](./rate.md)
  The playback rate of the sequencer’s player.
- [var tracks: [AVMusicTrack]](./tracks.md)
  An array that contains all the tracks in the sequence.
- [var currentPositionInBeats: TimeInterval](./currentpositioninbeats.md)
  The current playback position, in beats.
- [var currentPositionInSeconds: TimeInterval](./currentpositioninseconds.md)
  The current playback position, in seconds.
- [var tempoTrack: AVMusicTrack](./tempotrack.md)
  The track that contains tempo information about the sequence.
- [var userInfo: [String : Any]](./userinfo.md)
  A dictionary that contains metadata from a sequence.
- [func data(withSMPTEResolution: Int, error: NSErrorPointer) -> Data](./data%28withsmpteresolution,error%29.md)
  Gets a data object that contains the events from the sequence.
- [var AVMusicTimeStampEndOfTrack: Double](../avmusictimestampendoftrack.md)
  A timestamp you use to access all events in a music track through a beat range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosequencer/infodictionarykey)*