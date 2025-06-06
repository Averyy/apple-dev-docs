# kAudioUnitProperty_MatrixDimensions

**Framework**: Audio Toolbox  
**Kind**: var

Indicates the total number of channels for input and output of a given matrix mixer.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
var kAudioUnitProperty_MatrixDimensions: AudioUnitPropertyID { get }
```

#### Discussion

A read-only `2 * UInt32` value valid on the audio unit global scope.

## See Also

- [var kAudioUnitProperty_InputAnchorTimeStamp: AudioUnitPropertyID](kaudiounitproperty_inputanchortimestamp.md)
- [var kAudioUnitProperty_MatrixLevels: AudioUnitPropertyID](kaudiounitproperty_matrixlevels.md)
  Describes the internal state of a matrix mixer.
- [var kAudioUnitProperty_MeterClipping: AudioUnitPropertyID](kaudiounitproperty_meterclipping.md)
  Indicates audio clipping that has occurred since this property was last accessed.
- [var kAudioUnitProperty_MeteringMode: AudioUnitPropertyID](kaudiounitproperty_meteringmode.md)
  Specifies whether metering is enabled or disabled for a particular scope-element combination.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/kaudiounitproperty_matrixdimensions)*