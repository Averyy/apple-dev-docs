# I/O Audio Unit Function Selectors

**Framework**: Audio Toolbox  
**Role**: API Collection

Audio unit component selectors, specific to I/O audio units, that correspond to functions in the audio unit API.

## Topics

### Constants
- [var kAudioOutputUnitRange: Int](./kaudiooutputunitrange.md)
  The start of the numerical range for I/O audio unit function selectors.
- [var kAudioOutputUnitStartSelect: Int](./kaudiooutputunitstartselect.md)
  Used by the system to start an I/O audio unit when you call the [`AudioOutputUnitStart(_:)`](./audiooutputunitstart%28_%29.md) function.
- [var kAudioOutputUnitStopSelect: Int](./kaudiooutputunitstopselect.md)
  Used by the system to stop an I/O audio unit when you call the [`AudioOutputUnitStop(_:)`](./audiooutputunitstop%28_%29.md) function.

## See Also

### Input/Output
- [I/O Audio Unit Properties](./api-1534116-i_o_audio_unit_properties.md)
  Properties for Apple I/O audio units (sometimes called output units).
- [Inter-App Output Unit Property IDs](./api-1621039-inter-app-output-unit-property-ids.md)
- [Inter-App Audio Unit Property IDs](./api-1621038-inter-app-audio-unit-property-ids.md)
- [Output Unit Parameters](./api-1389916-output_unit_parameters.md)
- [AUNetReceive Properties](./api-1534109-aunetreceive-properties.md)
- [AUNetSend Properties](./api-1534207-aunetsend-properties.md)
- [AUNetSend Parameters](./api-1389633-aunetsend-parameters.md)
- [AUNetReceive Parameters](./api-1389920-aunetreceive-parameters.md)
- [AUNetSendPresetFormat Properties](./api-1534212-aunetsendpresetformat-properties.md)
- [Net Status Audio Unit Parameters](./api-1389891-net-status-audio-unit-parameters.md)
- [struct AudioOutputUnitMIDICallbacks](./audiooutputunitmidicallbacks.md)
- [struct AudioOutputUnitStartAtTimeParams](./audiooutputunitstartattimeparams.md)
  A timestamp for scheduled starting of an I/O audio unit.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/1585807-i_o_audio_unit_function_selector)*