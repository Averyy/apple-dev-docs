# kAudioUnitProperty_MeteringMode

**Framework**: Audio Toolbox  
**Kind**: var

Specifies whether metering is enabled or disabled for a particular scope-element combination.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
var kAudioUnitProperty_MeteringMode: AudioUnitPropertyID { get }
```

#### Discussion

A read/write `UInt32` value valid on the input and output scopes.

## See Also

- [var kAudioUnitProperty_InputAnchorTimeStamp: AudioUnitPropertyID](kaudiounitproperty_inputanchortimestamp.md)
- [var kAudioUnitProperty_MatrixDimensions: AudioUnitPropertyID](kaudiounitproperty_matrixdimensions.md)
  Indicates the total number of channels for input and output of a given matrix mixer.
- [var kAudioUnitProperty_MatrixLevels: AudioUnitPropertyID](kaudiounitproperty_matrixlevels.md)
  Describes the internal state of a matrix mixer.
- [var kAudioUnitProperty_MeterClipping: AudioUnitPropertyID](kaudiounitproperty_meterclipping.md)
  Indicates audio clipping that has occurred since this property was last accessed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/kaudiounitproperty_meteringmode)*