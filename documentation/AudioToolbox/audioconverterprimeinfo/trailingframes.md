# trailingFrames

**Framework**: Audio Toolbox  
**Kind**: property

The number of trailing frames of input audio data required by the converter to perform high-quality conversion. Trailing frames follow, in time, the expected final input frame. Your application should be prepared to provide this number of additional input frames except when using the `kConverterPrimeMethod_None` value for the `kAudioConverterPrimeMethod` property. If no additional frames are available in the input stream (because, for example, the desired end frame is at the end of an audio file), then the audio converter synthesizes a sufficient number of silent (`0`-valued) trailing frames.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
var trailingFrames: UInt32
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audioconverterprimeinfo/trailingframes)*