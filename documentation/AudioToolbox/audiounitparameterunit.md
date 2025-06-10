# AudioUnitParameterUnit

**Framework**: Audio Toolbox  
**Kind**: enum

The unit-of-measure for an audio unit parameter.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
enum AudioUnitParameterUnit
```

#### Overview

The various units of measure for audio unit parameters are described in `Audio Unit Parameter Units of Measure`.

## Topics

### Enumeration Cases
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
- [AudioUnitParameterUnit.midiNoteNumber](audiounitparameterunit/midinotenumber.md)
  A whole-number unit of measure corresponding to audio frequency.
- [AudioUnitParameterUnit.meters](audiounitparameterunit/meters.md)
  A distance unit of measure, corresponding to meters.
- [AudioUnitParameterUnit.milliseconds](audiounitparameterunit/milliseconds.md)
  A time unit of measure representing milliseconds.
- [AudioUnitParameterUnit.mixerFaderCurve1](audiounitparameterunit/mixerfadercurve1.md)
  An audio power unit of measure.
- [AudioUnitParameterUnit.octaves](audiounitparameterunit/octaves.md)
  A relative unit of measure for the musical interval between two notes.
- [AudioUnitParameterUnit.pan](audiounitparameterunit/pan.md)
  An audio position unit of measure.
- [AudioUnitParameterUnit.percent](audiounitparameterunit/percent.md)
  A percentage unit of measure.
- [AudioUnitParameterUnit.phase](audiounitparameterunit/phase.md)
  An angular degree unit of measure.
- [AudioUnitParameterUnit.rate](audiounitparameterunit/rate.md)
  A multiplication factor unit of measure.
- [AudioUnitParameterUnit.ratio](audiounitparameterunit/ratio.md)
  A unitless ratio unit of measure.
- [AudioUnitParameterUnit.relativeSemiTones](audiounitparameterunit/relativesemitones.md)
  A relative unit of measure for a musical interval between two notes.
- [AudioUnitParameterUnit.sampleFrames](audiounitparameterunit/sampleframes.md)
  A sample-frame-count unit of measure.
- [AudioUnitParameterUnit.seconds](audiounitparameterunit/seconds.md)
  A whole-seconds unit of measure, indicating either absolute or relative time.
- [AudioUnitParameterUnit.midi2Controller](audiounitparameterunit/midi2controller.md)
### Initializers
- [init?(rawValue: UInt32)](audiounitparameterunit/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [Audio Unit Types](1584142-audio_unit_types.md)
  The defined types of audio processing plug-ins known as audio units.
- [Inter-App Audio Unit Types](1619501-inter-app-audio-unit-types.md)
- [Audio Unit Manufacturer Identifier](1584143-audio_unit_manufacturer_identifi.md)
  The Apple audio unit manufacturer code.
- [Audio Unit Output Subtypes](1584148-audio-unit-output-subtypes.md)
- [I/O Audio Unit Subtypes](1619485-i-o-audio-unit-subtypes.md)
- [Converter Audio Unit Subtypes](1584145-converter_audio_unit_subtypes.md)
  Audio data format converter audio unit subtypes for audio units provided by Apple.
- [Reserved Audio Unit Clump Identifier](1533986-reserved_audio_unit_clump_identi.md)
  Reserved for system use.
- [Offline Audio Unit Properties](1534054-offline_audio_unit_properties.md)
  Properties for audio units that perform offline processing—that is, processing in a nonplayback, nonrealtime mode.
- [MIDI Audio Unit Parameters](1389613-midi_audio_unit_parameters.md)
  Parameters for instrument units.
- [General Audio Unit Function Selectors](1584140-general_audio_unit_function_sele.md)
  General audio unit component selectors that correspond to functions in the audio unit API.
- [Generator Audio Unit Subtypes](1619493-generator_audio_unit_subtypes.md)
  Audio units that serve as sound sources.
- [Input/Output Audio Unit Subtypes](1584139-input_output_audio_unit_subtypes.md)
  Input/output audio unit subtypes for audio units provided by Apple.
- [Audio Unit Panner Subtypes](1584151-audio-unit-panner-subtypes.md)
- [Audio Unit Player Subtypes](1584155-audio-unit-player-subtypes.md)
- [Audio Unit Pitch Subtypes](1584152-audio-unit-pitch-subtypes.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audiounitparameterunit)*