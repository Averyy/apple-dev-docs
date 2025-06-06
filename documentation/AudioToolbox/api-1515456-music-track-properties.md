# Music Track Properties

**Framework**: Audio Toolbox

Properties for music tracks.

## Topics

### Constants
- [var kSequenceTrackProperty_LoopInfo: UInt32](ksequencetrackproperty_loopinfo.md)
  Looping information for a music track.
- [var kSequenceTrackProperty_OffsetTime: UInt32](ksequencetrackproperty_offsettime.md)
  A music track’s start time in terms of beat number.
- [var kSequenceTrackProperty_MuteStatus: UInt32](ksequencetrackproperty_mutestatus.md)
  The mute/unmute state of a music track. By default this value is `false` (not muted). A read/write Boolean value.
- [var kSequenceTrackProperty_SoloStatus: UInt32](ksequencetrackproperty_solostatus.md)
  The solo/unsolo state of a music track. By default this value is `false` (not soloed). A read/write Boolean value.
- [var kSequenceTrackProperty_AutomatedParameters: UInt32](ksequencetrackproperty_automatedparameters.md)
  Indicates whether or not a music track’s purpose is audio unit parameter automation. If this property’s value is other than 0, music events in the track can only indicate points in an automation curve. A read/write `UInt32` value, where a value other than 0 indicates that the track is for parameter automation.
- [var kSequenceTrackProperty_TrackLength: UInt32](ksequencetrackproperty_tracklength.md)
  The time of the last music event in a music track, plus time required for note fade-outs and so on.
- [var kSequenceTrackProperty_TimeResolution: UInt32](ksequencetrackproperty_timeresolution.md)
  The time resolution for a sequence of music events. For example, this value can indicate the time resolution that was specified by the MIDI file used to construct a sequence.

## See Also

- [Music Instrument Audio Unit Subtypes](1619498-music-instrument-audio-unit-subt.md)
- [struct MusicSequenceFileFlags](musicsequencefileflags.md)
  Flags that configure the behavior of the [`MusicSequenceFileCreate(_:_:_:_:_:)`](musicsequencefilecreate(_:_:_:_:_:).md) and [`MusicSequenceFileCreateData(_:_:_:_:_:)`](musicsequencefilecreatedata(_:_:_:_:_:).md) functions.
- [enum MusicSequenceFileTypeID](musicsequencefiletypeid.md)
  The various types of files that can be parsed by a music sequence.
- [struct MusicSequenceLoadFlags](musicsequenceloadflags.md)
  Flags used to configure the behavior of the [`MusicSequenceFileLoad(_:_:_:_:)`](musicsequencefileload(_:_:_:_:).md) and [`MusicSequenceFileLoadData(_:_:_:_:)`](musicsequencefileloaddata(_:_:_:_:).md) functions.
- [enum MusicSequenceType](musicsequencetype.md)
  The various types of music sequences.
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

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/1515456-music-track-properties)*