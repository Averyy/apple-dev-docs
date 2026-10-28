# tempoTrack

**Framework**: AVFAudio  
**Kind**: property  
**Role**: Instance Property

The track that contains tempo information about the sequence.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var tempoTrack: AVMusicTrack { get }
```

```objc
@property (nonatomic, readonly) AVMusicTrack * tempoTrack;
```

## Discussion

Each sequence has a single tempo track. The framework places all tempo events into this track along with other appropriate events, such as the time signature from a MIDI file.

You can edit the tempo track like any other track. The framework ignores nontempo events in the track.

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
- [var userInfo: [String : Any]](./userinfo.md)
  A dictionary that contains metadata from a sequence.
- [AVAudioSequencer.InfoDictionaryKey](./infodictionarykey.md)
  Constants that defines metadata keys for a sequencer.
- [func data(withSMPTEResolution: Int, error: NSErrorPointer) -> Data](./data%28withsmpteresolution,error%29.md)
  Gets a data object that contains the events from the sequence.
- [var AVMusicTimeStampEndOfTrack: Double](../avmusictimestampendoftrack.md)
  A timestamp you use to access all events in a music track through a beat range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosequencer/tempotrack)*