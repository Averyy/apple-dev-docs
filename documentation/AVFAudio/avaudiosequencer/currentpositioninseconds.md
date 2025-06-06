# currentPositionInSeconds

**Framework**: AVFAudio  
**Kind**: property

The current playback position, in seconds.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var currentPositionInSeconds: TimeInterval { get set }
```

#### Discussion

This property positions the sequencer’s player to the specified time. You can update this property while the player is in a playing state, in which case, playback resumes at the new position.

## See Also

- [var isPlaying: Bool](avaudiosequencer/isplaying.md)
  A Boolean value that indicates whether the sequencer’s player is in a playing state.
- [var rate: Float](avaudiosequencer/rate.md)
  The playback rate of the sequencer’s player.
- [var tracks: [AVMusicTrack]](avaudiosequencer/tracks.md)
  An array that contains all the tracks in the sequence.
- [var currentPositionInBeats: TimeInterval](avaudiosequencer/currentpositioninbeats.md)
  The current playback position, in beats.
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

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosequencer/currentpositioninseconds)*