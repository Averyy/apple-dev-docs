# AudioUnitParameterUnit.absoluteCents

**Framework**: Audio Toolbox  
**Kind**: case

An absolute unit of measure for the musical pitch of a note.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
case absoluteCents
```

#### Discussion

Absolute musical pitch in cents. 1,200 cents are equal to one octave. If `f` is a frequency in hertz, then `absoluteCents = 1200 * log2 (f/440) + 6900`. See also the [`AudioUnitParameterUnit.cents`](audiounitparameterunit/cents.md) property.

## See Also

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
- [AudioUnitParameterUnit.midiNoteNumber](audiounitparameterunit/midinotenumber.md)
  A whole-number unit of measure corresponding to audio frequency.
- [AudioUnitParameterUnit.meters](audiounitparameterunit/meters.md)
  A distance unit of measure, corresponding to meters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audiounitparameterunit/absolutecents)*