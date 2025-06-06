# tracks

**Framework**: AVFAudio  
**Kind**: property

An array that contains all the tracks in the sequence.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var tracks: [AVMusicTrack] { get }
```

#### Discussion

The track indices start at `0`, and don’t include the tempo track.

## See Also

- [var isPlaying: Bool](avaudiosequencer/isplaying.md)
  A Boolean value that indicates whether the sequencer’s player is in a playing state.
- [var rate: Float](avaudiosequencer/rate.md)
  The playback rate of the sequencer’s player.
- [var currentPositionInBeats: TimeInterval](avaudiosequencer/currentpositioninbeats.md)
  The current playback position, in beats.
- [var currentPositionInSeconds: TimeInterval](avaudiosequencer/currentpositioninseconds.md)
  The current playback position, in seconds.
- [var tempoTrack: AVMusicTrack](avaudiosequencer/tempotrack.md)
  The track that contains tempo information about the sequence.
- [var userInfo: [String : Any]](avaudiosequencer/userinfo.md)
  A dictionary that contains metadata from a sequence.
- [AVAudioSequencer.InfoDictionaryKey](avaudiosequencer/infodictionarykey.md)
  Constants that defines metadata keys for a sequencer.
- [func data(withSMPTEResolution: Int, error: NSErrorPointer) -> Data](avaudiosequencer/data(withsmpteresolution:error:).md)
  Gets a data object that contains the events from the sequence.
- [var AVMusicTimeStampEndOfTrack: Double](avmusictimestampendoftrack.md)
  A timestamp you use to access all events in a music track through a beat range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosequencer/tracks)*