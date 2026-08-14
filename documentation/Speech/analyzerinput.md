# AnalyzerInput

**Framework**: Speech  
**Kind**: struct

Time-coded audio data.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
struct AnalyzerInput
```

#### Overview

The audio data must have an audio format that is supported by the analyzer’s modules; the analyzer does not perform audio conversion. Call [`bestAvailableAudioFormat(compatibleWith:considering:)`](speechanalyzer/bestavailableaudioformat(compatiblewith:considering:).md) (or its variants) to select an appropriate format to convert to.

The audio format may differ from one `AnalyzerInput` object to the next. If the new audio format is supported by the modules, the modules will be reconfigured as needed.

## Topics

### Creating an input element
- [init(buffer: CMReadySampleBuffer<CMReadOnlyDataBlockBuffer>)](analyzerinput/init(buffer:)-3nt02.md)
  Creates an audio input object.
- [init(buffer: AVAudioPCMBuffer)](analyzerinput/init(buffer:)-2ysg3.md)
  Creates an audio input object.
- [init(buffer: AVAudioPCMBuffer, bufferStartTime: CMTime?)](analyzerinput/init(buffer:bufferstarttime:).md)
  Creates an audio input object for audio that may be discontiguous with previous input.
### Inspecting an input element
- [let bufferStartTime: CMTime?](analyzerinput/bufferstarttime.md)
  The time-code of this input.
- [let bufferDuration: CMTime](analyzerinput/bufferduration.md)
  The length of this input.
- [let bufferFormat: AVAudioFormat](analyzerinput/bufferformat.md)
  The audio format of this input.
- [var buffer: AVAudioPCMBuffer](analyzerinput/buffer.md)
  A new copy of the audio data for this input.

## Relationships

### Conforms To
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [protocol SpeechModuleResult](speechmoduleresult.md)
  Protocol that all module results conform to.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/analyzerinput)*