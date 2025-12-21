# kAudioUnitType_MIDIProcessor

**Framework**: Audio Toolbox  
**Kind**: var

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
var kAudioUnitType_MIDIProcessor: UInt32 { get }
```

## See Also

- [var kAudioUnitType_Output: UInt32](kaudiounittype_output.md)
  An output unit provides input, output, or both input and output simultaneously. It can be used as the head of an audio unit processing graph.
- [var kAudioUnitType_MusicDevice: UInt32](kaudiounittype_musicdevice.md)
  An instrument unit can be used as a software musical instrument, such as a sampler or synthesizer. It responds to MIDI (Musical Instrument Digital Interface) control signals and can create notes.
- [var kAudioUnitType_MusicEffect: UInt32](kaudiounittype_musiceffect.md)
  An effect unit that can respond to MIDI control messages, typically through a mapping of  MIDI messages to parameters of the audio unit’s DSP algorithm.
- [var kAudioUnitType_FormatConverter: UInt32](kaudiounittype_formatconverter.md)
- [var kAudioUnitType_Effect: UInt32](kaudiounittype_effect.md)
- [var kAudioUnitType_Mixer: UInt32](kaudiounittype_mixer.md)
  A mixer unit takes a number of input channels and mixes them to provide one or more output channels.
- [var kAudioUnitType_Panner: UInt32](kaudiounittype_panner.md)
- [var kAudioUnitType_OfflineEffect: UInt32](kaudiounittype_offlineeffect.md)
  An offline effect unit provides digital signal processing of a sort that cannot proceed in realtime. For example, level normalization requires examination of an entire sound, beginning to end, before the normalization factor can be calculated. As such, offline effect units also have a notion of a priming stage that can be performed before the actual rendering/processing phase is executed.
- [var kAudioUnitType_Generator: UInt32](kaudiounittype_generator.md)
  A generator unit provides audio output but has no audio input. This audio unit type is appropriate for a tone generator. Unlike an instrument unit, a generator unit does not have a control input.
- [var kAudioUnitType_SpeechSynthesizer: UInt32](kaudiounittype_speechsynthesizer.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/kaudiounittype_midiprocessor)*