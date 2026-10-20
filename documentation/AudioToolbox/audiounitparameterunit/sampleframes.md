# AudioUnitParameterUnit.sampleFrames

**Framework**: Audio Toolbox  
**Kind**: case  
**Role**: Case

A sample-frame-count unit of measure.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS

## Declaration

```swift
case sampleFrames
```

```c
kAudioUnitParameterUnit_SampleFrames
```

#### Discussion

The duration of a sample frame, for fixed frame-rate audio formats, is equal to 1.0/`kAudioUnitProperty_SampleRate` seconds.

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
- [AudioUnitParameterUnit.equalPowerCrossfade](./equalpowercrossfade.md)
  An audio power unit of measure.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audiounitparameterunit/sampleframes)*