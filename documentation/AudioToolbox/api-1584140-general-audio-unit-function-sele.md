# General Audio Unit Function Selectors

**Framework**: Audio Toolbox

General audio unit component selectors that correspond to functions in the audio unit API.

## Topics

### Constants
- [var kAudioUnitAddPropertyListenerSelect: Int](kaudiounitaddpropertylistenerselect.md)
  Used by the system to register a property listener callback function for an audio unit when you call the [`AudioUnitAddPropertyListener(_:_:_:_:)`](audiounitaddpropertylistener(_:_:_:_:).md) function.
- [var kAudioUnitAddRenderNotifySelect: Int](kaudiounitaddrendernotifyselect.md)
- [var kAudioUnitComplexRenderSelect: Int](kaudiounitcomplexrenderselect.md)
- [var kAudioUnitGetParameterSelect: Int](kaudiounitgetparameterselect.md)
  Used by the system to get the current value of an audio unit parameter when you call the [`AudioUnitGetParameter(_:_:_:_:_:)`](audiounitgetparameter(_:_:_:_:_:).md) function.
- [var kAudioUnitGetPropertyInfoSelect: Int](kaudiounitgetpropertyinfoselect.md)
  Used by the system to get property information from an audio unit when you call the [`AudioUnitGetPropertyInfo(_:_:_:_:_:_:)`](audiounitgetpropertyinfo(_:_:_:_:_:_:).md) function.
- [var kAudioUnitGetPropertySelect: Int](kaudiounitgetpropertyselect.md)
- [var kAudioUnitInitializeSelect: Int](kaudiounitinitializeselect.md)
- [var kAudioUnitProcessMultipleSelect: Int](kaudiounitprocessmultipleselect.md)
- [var kAudioUnitProcessSelect: Int](kaudiounitprocessselect.md)
- [var kAudioUnitRange: Int](kaudiounitrange.md)
- [var kAudioUnitRemovePropertyListenerSelect: Int](kaudiounitremovepropertylistenerselect.md)
  Used by the system to unregister a property listener callback function from an audio unit when you call the `AudioUnitRemovePropertyListener` function.
- [var kAudioUnitRemovePropertyListenerWithUserDataSelect: Int](kaudiounitremovepropertylistenerwithuserdataselect.md)
- [var kAudioUnitRemoveRenderNotifySelect: Int](kaudiounitremoverendernotifyselect.md)
- [var kAudioUnitRenderSelect: Int](kaudiounitrenderselect.md)
  Used by the system to invoke audio rendering by an audio unit when you call the [`AudioUnitRender(_:_:_:_:_:_:)`](audiounitrender(_:_:_:_:_:_:).md) function.
- [var kAudioUnitResetSelect: Int](kaudiounitresetselect.md)
  Used by the system to reset an audio unit when you call the [`AudioUnitReset(_:_:_:)`](audiounitreset(_:_:_:).md) function.
- [var kAudioUnitScheduleParametersSelect: Int](kaudiounitscheduleparametersselect.md)
  Used by the system to schedule an audio unit parameter value change when you call the [`AudioUnitScheduleParameters(_:_:_:)`](audiounitscheduleparameters(_:_:_:).md) function.
- [var kAudioUnitSetParameterSelect: Int](kaudiounitsetparameterselect.md)
  Used by the system to set the value of an audio unit parameter when you call the [`AudioUnitSetParameter(_:_:_:_:_:_:)`](audiounitsetparameter(_:_:_:_:_:_:).md) function.
- [var kAudioUnitSetPropertySelect: Int](kaudiounitsetpropertyselect.md)
- [var kAudioUnitUninitializeSelect: Int](kaudiounituninitializeselect.md)
  Used by the system to uninitialize an audio unit when you call the [`AudioUnitUninitialize(_:)`](audiounituninitialize(_:).md) function.

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
- [Generator Audio Unit Subtypes](1619493-generator_audio_unit_subtypes.md)
  Audio units that serve as sound sources.
- [Input/Output Audio Unit Subtypes](1584139-input_output_audio_unit_subtypes.md)
  Input/output audio unit subtypes for audio units provided by Apple.
- [Audio Unit Panner Subtypes](1584151-audio-unit-panner-subtypes.md)
- [Audio Unit Player Subtypes](1584155-audio-unit-player-subtypes.md)
- [Audio Unit Pitch Subtypes](1584152-audio-unit-pitch-subtypes.md)
- [enum AudioUnitEventType](audiouniteventtype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/1584140-general_audio_unit_function_sele)*