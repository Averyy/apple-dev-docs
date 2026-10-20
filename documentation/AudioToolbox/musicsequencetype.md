# MusicSequenceType

**Framework**: Audio Toolbox  
**Kind**: enum  
**Role**: Enumeration

The various types of music sequences.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS

## Declaration

```swift
enum MusicSequenceType
```

```c
enum MusicSequenceType : UInt32;
```

## Topics

### Constants
- [MusicSequenceType.beats](./musicsequencetype/beats.md)
  Used for a music sequence that corresponds to a normal MIDI file. The tempo track defines the number of beats per second and can have multiple tempo events.
- [MusicSequenceType.seconds](./musicsequencetype/seconds.md)
  Used for a music sequence that corresponds to a MIDI file, but employs SMPTE timecode. The tempo track contains a single tempo event that specifies 60 beat-per-minute.
- [MusicSequenceType.samples](./musicsequencetype/samples.md)
  Used for audio samples; a music sequence of this type cannot be saved to a MIDI file. The tempo track contains a single tempo event that specifies an audio sample rate in samples-per-second.
### Initializers
- [init?(rawValue: UInt32)](./musicsequencetype/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Enumerations
- [Music Instrument Audio Unit Subtypes](./api-1619498-music-instrument-audio-unit-subt.md)
- [Music Track Properties](./api-1515456-music-track-properties.md)
  Properties for music tracks.
- [struct MusicSequenceFileFlags](./musicsequencefileflags.md)
  Flags that configure the behavior of the [`MusicSequenceFileCreate(_:_:_:_:_:)`](./musicsequencefilecreate%28_,_,_,_,_%29.md) and [`MusicSequenceFileCreateData(_:_:_:_:_:)`](./musicsequencefilecreatedata%28_,_,_,_,_%29.md) functions.
- [enum MusicSequenceFileTypeID](./musicsequencefiletypeid.md)
  The various types of files that can be parsed by a music sequence.
- [struct MusicSequenceLoadFlags](./musicsequenceloadflags.md)
  Flags used to configure the behavior of the [`MusicSequenceFileLoad(_:_:_:_:)`](./musicsequencefileload%28_,_,_,_%29.md) and [`MusicSequenceFileLoadData(_:_:_:_:)`](./musicsequencefileloaddata%28_,_,_,_%29.md) functions.
- [Music Extended Control Event Type](./api-1515446-music-extended-control-event-typ.md)
- [Music Player Errors](./api-1515472-music-player-errors.md)
- [Music Event Types](./api-1515479-music-event-types.md)
- [Music Note Events](./api-1473494-music-note-events.md)
- [Music Device Selectors](./api-1473469-music-device-selectors.md)
- [Music Device Properties](./api-1533931-music-device-properties.md)
- [Music Device Sample Frame Mask](./api-1533978-music-device-sample-frame-mask.md)
- [Music Device Unit Properties](./api-1533963-music-device-unit-properties.md)
- [Instrument Types](./api-1534202-instrument-types.md)
- [Music Device Generic Properties](./api-1533930-music-device-generic-properties.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/musicsequencetype)*