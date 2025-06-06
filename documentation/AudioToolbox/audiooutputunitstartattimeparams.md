# AudioOutputUnitStartAtTimeParams

**Framework**: Audio Toolbox  
**Kind**: struct

A timestamp for scheduled starting of an I/O audio unit.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
struct AudioOutputUnitStartAtTimeParams
```

## Topics

### Initializers
- [init()](audiooutputunitstartattimeparams/init.md)
- [init(mTimestamp: AudioTimeStamp, mFlags: UInt32)](audiooutputunitstartattimeparams/init(mtimestamp:mflags:).md)
### Instance Properties
- [var mFlags: UInt32](audiooutputunitstartattimeparams/mflags.md)
- [var mTimestamp: AudioTimeStamp](audiooutputunitstartattimeparams/mtimestamp.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [I/O Audio Unit Properties](1534116-i_o_audio_unit_properties.md)
  Properties for Apple I/O audio units (sometimes called output units).
- [Inter-App Output Unit Property IDs](1621039-inter-app-output-unit-property-ids.md)
- [Inter-App Audio Unit Property IDs](1621038-inter-app-audio-unit-property-ids.md)
- [Output Unit Parameters](1389916-output_unit_parameters.md)
- [AUNetReceive Properties](1534109-aunetreceive-properties.md)
- [AUNetSend Properties](1534207-aunetsend-properties.md)
- [AUNetSend Parameters](1389633-aunetsend-parameters.md)
- [AUNetReceive Parameters](1389920-aunetreceive-parameters.md)
- [AUNetSendPresetFormat Properties](1534212-aunetsendpresetformat-properties.md)
- [Net Status Audio Unit Parameters](1389891-net-status-audio-unit-parameters.md)
- [I/O Audio Unit Function Selectors](1585807-i_o_audio_unit_function_selector.md)
  Audio unit component selectors, specific to I/O audio units, that correspond to functions in the audio unit API.
- [struct AudioOutputUnitMIDICallbacks](audiooutputunitmidicallbacks.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audiooutputunitstartattimeparams)*