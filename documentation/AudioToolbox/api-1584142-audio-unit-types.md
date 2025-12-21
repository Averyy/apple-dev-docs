# Audio Unit Types

**Framework**: Audio Toolbox

The defined types of audio processing plug-ins known as audio units.

## Topics

### Types
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
- [var kAudioUnitType_MIDIProcessor: UInt32](kaudiounittype_midiprocessor.md)
- [var kAudioUnitType_SpeechSynthesizer: UInt32](kaudiounittype_speechsynthesizer.md)

## See Also

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
- [enum AudioUnitEventType](audiouniteventtype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/1584142-audio_unit_types)*