# kAudioUnitProperty_MeterClipping

**Framework**: Audio Toolbox  
**Kind**: var

Indicates audio clipping that has occurred since this property was last accessed.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
var kAudioUnitProperty_MeterClipping: AudioUnitPropertyID { get }
```

#### Discussion

A read-only [`AudioUnitMeterClipping`](audiounitmeterclipping.md) data structure valid on the audio unit global scope.

## See Also

- [var kAudioUnitProperty_InputAnchorTimeStamp: AudioUnitPropertyID](kaudiounitproperty_inputanchortimestamp.md)
- [var kAudioUnitProperty_MatrixDimensions: AudioUnitPropertyID](kaudiounitproperty_matrixdimensions.md)
  Indicates the total number of channels for input and output of a given matrix mixer.
- [var kAudioUnitProperty_MatrixLevels: AudioUnitPropertyID](kaudiounitproperty_matrixlevels.md)
  Describes the internal state of a matrix mixer.
- [var kAudioUnitProperty_MeteringMode: AudioUnitPropertyID](kaudiounitproperty_meteringmode.md)
  Specifies whether metering is enabled or disabled for a particular scope-element combination.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/kaudiounitproperty_meterclipping)*