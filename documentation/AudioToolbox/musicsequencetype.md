# MusicSequenceType

**Framework**: Audio Toolbox  
**Kind**: enum

The various types of music sequences.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
enum MusicSequenceType
```

## Topics

### Constants
- [MusicSequenceType.beats](musicsequencetype/beats.md)
  Used for a music sequence that corresponds to a normal MIDI file. The tempo track defines the number of beats per second and can have multiple tempo events.
- [MusicSequenceType.seconds](musicsequencetype/seconds.md)
  Used for a music sequence that corresponds to a MIDI file, but employs SMPTE timecode. The tempo track contains a single tempo event that specifies 60 beat-per-minute.
- [MusicSequenceType.samples](musicsequencetype/samples.md)
  Used for audio samples; a music sequence of this type cannot be saved to a MIDI file. The tempo track contains a single tempo event that specifies an audio sample rate in samples-per-second.
### Initializers
- [init?(rawValue: UInt32)](musicsequencetype/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [Music Instrument Audio Unit Subtypes](1619498-music-instrument-audio-unit-subt.md)
- [Music Track Properties](1515456-music-track-properties.md)
  Properties for music tracks.
- [struct MusicSequenceFileFlags](musicsequencefileflags.md)
  Flags that configure the behavior of the [`MusicSequenceFileCreate(_:_:_:_:_:)`](musicsequencefilecreate(_:_:_:_:_:).md) and [`MusicSequenceFileCreateData(_:_:_:_:_:)`](musicsequencefilecreatedata(_:_:_:_:_:).md) functions.
- [enum MusicSequenceFileTypeID](musicsequencefiletypeid.md)
  The various types of files that can be parsed by a music sequence.
- [struct MusicSequenceLoadFlags](musicsequenceloadflags.md)
  Flags used to configure the behavior of the [`MusicSequenceFileLoad(_:_:_:_:)`](musicsequencefileload(_:_:_:_:).md) and [`MusicSequenceFileLoadData(_:_:_:_:)`](musicsequencefileloaddata(_:_:_:_:).md) functions.
- [Music Extended Control Event Type](1515446-music-extended-control-event-typ.md)
- [Music Player Errors](1515472-music-player-errors.md)
- [Music Event Types](1515479-music-event-types.md)
- [Music Note Events](1473494-music-note-events.md)
- [Music Device Selectors](1473469-music-device-selectors.md)
- [Music Device Properties](1533931-music-device-properties.md)
- [Music Device Sample Frame Mask](1533978-music-device-sample-frame-mask.md)
- [Music Device Unit Properties](1533963-music-device-unit-properties.md)
- [Instrument Types](1534202-instrument-types.md)
- [Music Device Generic Properties](1533930-music-device-generic-properties.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/musicsequencetype)*