# AUParameterEventType

**Framework**: Audio Toolbox  
**Kind**: enum  
**Role**: Enumeration

Audio unit parameter event types.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS

## Declaration

```swift
enum AUParameterEventType
```

```c
enum AUParameterEventType : UInt32;
```

## Topics

### Constants
- [AUParameterEventType.parameterEvent_Immediate](./auparametereventtype/parameterevent_immediate.md)
  An immediate change from the parameter’s previous value to a new value.
- [AUParameterEventType.parameterEvent_Ramped](./auparametereventtype/parameterevent_ramped.md)
  A gradual change from the parameter’s previous value to a new value, applied linearly over a specified period of time
### Initializers
- [init?(rawValue: UInt32)](./auparametereventtype/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Enumerations
- [Audio Unit Types](./api-1584142-audio_unit_types.md)
  The defined types of audio processing plug-ins known as audio units.
- [Inter-App Audio Unit Types](./api-1619501-inter-app-audio-unit-types.md)
- [Audio Unit Manufacturer Identifier](./api-1584143-audio_unit_manufacturer_identifi.md)
  The Apple audio unit manufacturer code.
- [Audio Unit Output Subtypes](./api-1584148-audio-unit-output-subtypes.md)
- [I/O Audio Unit Subtypes](./api-1619485-i-o-audio-unit-subtypes.md)
- [Converter Audio Unit Subtypes](./api-1584145-converter_audio_unit_subtypes.md)
  Audio data format converter audio unit subtypes for audio units provided by Apple.
- [Reserved Audio Unit Clump Identifier](./api-1533986-reserved_audio_unit_clump_identi.md)
  Reserved for system use.
- [Offline Audio Unit Properties](./api-1534054-offline_audio_unit_properties.md)
  Properties for audio units that perform offline processing—that is, processing in a nonplayback, nonrealtime mode.
- [MIDI Audio Unit Parameters](./api-1389613-midi_audio_unit_parameters.md)
  Parameters for instrument units.
- [General Audio Unit Function Selectors](./api-1584140-general_audio_unit_function_sele.md)
  General audio unit component selectors that correspond to functions in the audio unit API.
- [Generator Audio Unit Subtypes](./api-1619493-generator_audio_unit_subtypes.md)
  Audio units that serve as sound sources.
- [Input/Output Audio Unit Subtypes](./api-1584139-input_output_audio_unit_subtypes.md)
  Input/output audio unit subtypes for audio units provided by Apple.
- [Audio Unit Panner Subtypes](./api-1584151-audio-unit-panner-subtypes.md)
- [Audio Unit Player Subtypes](./api-1584155-audio-unit-player-subtypes.md)
- [Audio Unit Pitch Subtypes](./api-1584152-audio-unit-pitch-subtypes.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/auparametereventtype)*