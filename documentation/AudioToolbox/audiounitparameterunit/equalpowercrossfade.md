# AudioUnitParameterUnit.equalPowerCrossfade

**Framework**: Audio Toolbox  
**Kind**: case  
**Role**: Case

An audio power unit of measure.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS

## Declaration

```swift
case equalPowerCrossfade
```

```c
kAudioUnitParameterUnit_EqualPowerCrossfade
```

## Discussion

Recommended range is from 0 through 100, representing a crossfade mix of two sources according to `sqrt (x)` and `sqrt (1.0 - x)`.

## See Also

### Enumeration Cases
- [AudioUnitParameterUnit.absoluteCents](./absolutecents.md)
  An absolute unit of measure for the musical pitch of a note.
- [AudioUnitParameterUnit.BPM](./bpm.md)
  A whole-number unit of measure for musical tempo, representing beats per minute.
- [AudioUnitParameterUnit.beats](./beats.md)
  A time unit of measure in musical beats.
- [AudioUnitParameterUnit.boolean](./boolean.md)
  A Boolean-like unit of measure.
- [AudioUnitParameterUnit.cents](./cents.md)
  A logarithmic unit of measure for a musical interval between two notes.
- [AudioUnitParameterUnit.customUnit](./customunit.md)
  A custom unit of measure.
- [AudioUnitParameterUnit.decibels](./decibels.md)
  A logarithmic unit of measure representing the ratio between two audio levels.
- [AudioUnitParameterUnit.degrees](./degrees.md)
  An angular degree unit of measure.
- [AudioUnitParameterUnit.generic](./generic.md)
  A generic unit of measure.
- [AudioUnitParameterUnit.hertz](./hertz.md)
  A hertz unit of measure.
- [AudioUnitParameterUnit.indexed](./indexed.md)
  An indexed unit of measure.
- [AudioUnitParameterUnit.linearGain](./lineargain.md)
  A linear unit of measure representing the difference between two audio levels.
- [AudioUnitParameterUnit.midiController](./midicontroller.md)
  A whole-number unit of measure corresponding to standard MIDI control numbers.
- [AudioUnitParameterUnit.midiNoteNumber](./midinotenumber.md)
  A whole-number unit of measure corresponding to audio frequency.
- [AudioUnitParameterUnit.meters](./meters.md)
  A distance unit of measure, corresponding to meters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audiounitparameterunit/equalpowercrossfade)*