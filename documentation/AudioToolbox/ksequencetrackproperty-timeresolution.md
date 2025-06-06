# kSequenceTrackProperty_TimeResolution

**Framework**: Audio Toolbox  
**Kind**: var

The time resolution for a sequence of music events. For example, this value can indicate the time resolution that was specified by the MIDI file used to construct a sequence.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
var kSequenceTrackProperty_TimeResolution: UInt32 { get }
```

#### Discussion

To use a specific time resolution when writing a new file, retrieve this value and then specify it when calling the [`MusicSequenceFileCreate(_:_:_:_:_:)`](musicsequencefilecreate(_:_:_:_:_:).md) function.

This value does not directly determine playback rate for a music track, but rather it

`kSequenceTrackProperty_TimeResolution` is set in two possible ways:

- If you create a music sequence programmatically, the value is set to 480.
- If you create a music sequence from a MIDI file, the value is set to the time resolution specified in the MIDI file.

A read-only `SInt16` value that is valid only for a tempo track.

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/ksequencetrackproperty_timeresolution)*