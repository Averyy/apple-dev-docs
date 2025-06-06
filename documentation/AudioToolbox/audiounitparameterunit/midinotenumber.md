# AudioUnitParameterUnit.midiNoteNumber

**Framework**: Audio Toolbox  
**Kind**: case

A whole-number unit of measure corresponding to audio frequency.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
case midiNoteNumber
```

#### Discussion

Absolute pitch as defined in the MIDI specification. A standard piano keyboard ranges from MIDI note number 21 (for the A0 note) to 108 (for the C8 note), with MIDI note 60 corresponding to middle C (C4). The frequency for a given MIDI note number may depend on a tuning table.

## See Also

- [AudioUnitParameterUnit.absoluteCents](audiounitparameterunit/absolutecents.md)
  An absolute unit of measure for the musical pitch of a note.
- [AudioUnitParameterUnit.BPM](audiounitparameterunit/bpm.md)
  A whole-number unit of measure for musical tempo, representing beats per minute.
- [AudioUnitParameterUnit.beats](audiounitparameterunit/beats.md)
  A time unit of measure in musical beats.
- [AudioUnitParameterUnit.boolean](audiounitparameterunit/boolean.md)
  A Boolean-like unit of measure.
- [AudioUnitParameterUnit.cents](audiounitparameterunit/cents.md)
  A logarithmic unit of measure for a musical interval between two notes.
- [AudioUnitParameterUnit.customUnit](audiounitparameterunit/customunit.md)
  A custom unit of measure.
- [AudioUnitParameterUnit.decibels](audiounitparameterunit/decibels.md)
  A logarithmic unit of measure representing the ratio between two audio levels.
- [AudioUnitParameterUnit.degrees](audiounitparameterunit/degrees.md)
  An angular degree unit of measure.
- [AudioUnitParameterUnit.equalPowerCrossfade](audiounitparameterunit/equalpowercrossfade.md)
  An audio power unit of measure.
- [AudioUnitParameterUnit.generic](audiounitparameterunit/generic.md)
  A generic unit of measure.
- [AudioUnitParameterUnit.hertz](audiounitparameterunit/hertz.md)
  A hertz unit of measure.
- [AudioUnitParameterUnit.indexed](audiounitparameterunit/indexed.md)
  An indexed unit of measure.
- [AudioUnitParameterUnit.linearGain](audiounitparameterunit/lineargain.md)
  A linear unit of measure representing the difference between two audio levels.
- [AudioUnitParameterUnit.midiController](audiounitparameterunit/midicontroller.md)
  A whole-number unit of measure corresponding to standard MIDI control numbers.
- [AudioUnitParameterUnit.meters](audiounitparameterunit/meters.md)
  A distance unit of measure, corresponding to meters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audiounitparameterunit/midinotenumber)*