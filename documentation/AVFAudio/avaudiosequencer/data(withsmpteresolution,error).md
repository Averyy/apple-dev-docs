# data(withSMPTEResolution:error:)

**Framework**: AVFAudio  
**Kind**: method  
**Role**: Instance Method

Gets a data object that contains the events from the sequence.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func data(withSMPTEResolution SMPTEResolution: Int, error outError: NSErrorPointer) -> Data
```

```objc
- (NSData *) dataWithSMPTEResolution:(NSInteger) SMPTEResolution error:(NSError **) outError;
```

## Discussion

The client controls the lifetime of the data value this method returns.

## Parameters

- `SMPTEResolution`: The relationship between tick and quarter note for saving to a Standard MIDI File. Pass `0` to use the default.
- `outError`: On exit, if an error occurs, a description of the error.

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
- [AVAudioSequencer.InfoDictionaryKey](./infodictionarykey.md)
  Constants that defines metadata keys for a sequencer.
- [var AVMusicTimeStampEndOfTrack: Double](../avmusictimestampendoftrack.md)
  A timestamp you use to access all events in a music track through a beat range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosequencer/data(withsmpteresolution:error:))*