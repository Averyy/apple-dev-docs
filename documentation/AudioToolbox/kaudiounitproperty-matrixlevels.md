# kAudioUnitProperty_MatrixLevels

**Framework**: Audio Toolbox  
**Kind**: var

Describes the internal state of a matrix mixer.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
var kAudioUnitProperty_MatrixLevels: AudioUnitPropertyID { get }
```

#### Discussion

Calculate the size required for this property’s value as follows:

```objc
(input channel count + 1) * (output channel count + 1)
```

Obtain the channel counts using the `kAudioUnitProperty_MatrixDimensions` property.

For example, consider a matrix mixer that has 2 input channels and 2 output channels. The value of this property then requires a 3 x 3 array of `Float32` values. You can retrieve specific pieces of information for this example matrix mixer’s state as follows:

- Global volume is stored at `volumes[2][2]`
- Input volumes are stored in the last column: first input channel at `volumes[0][2]`; second input channel at `volumes[1][2]`
- Output volumes are stored in the last row: first output channel at `volumes [2][0]`; second output channel at `volumes[2][1]`
- Cross-point volumes are stored at their expected locations(`volumes[0][1]`, etc)

A read-only two-dimensional array of `Float32` values valid on the audio unit global scope.

## See Also

- [var kAudioUnitProperty_InputAnchorTimeStamp: AudioUnitPropertyID](kaudiounitproperty_inputanchortimestamp.md)
- [var kAudioUnitProperty_MatrixDimensions: AudioUnitPropertyID](kaudiounitproperty_matrixdimensions.md)
  Indicates the total number of channels for input and output of a given matrix mixer.
- [var kAudioUnitProperty_MeterClipping: AudioUnitPropertyID](kaudiounitproperty_meterclipping.md)
  Indicates audio clipping that has occurred since this property was last accessed.
- [var kAudioUnitProperty_MeteringMode: AudioUnitPropertyID](kaudiounitproperty_meteringmode.md)
  Specifies whether metering is enabled or disabled for a particular scope-element combination.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/kaudiounitproperty_matrixlevels)*