# AnalyzerInput

**Framework**: Speech  
**Kind**: struct

Time-coded audio data.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
struct AnalyzerInput
```

#### Overview

The audio data must have an `AVAudioFormat` that is supported by the analyzer’s modules; the analyzer does not perform audio conversion. Call [`bestAvailableAudioFormat(compatibleWith:considering:)`](speechanalyzer/bestavailableaudioformat(compatiblewith:considering:).md) (or its variants) to select an appropriate format to convert to.

The audio format may differ from one `AnalyzerInput` object to the next. The modules will be reconfigured if necessary (and possible) as needed.

## Topics

### Creating an input element
- [init(buffer: AVAudioPCMBuffer)](analyzerinput/init(buffer:).md)
  Creates an audio input object.
- [init(buffer: AVAudioPCMBuffer, bufferStartTime: CMTime?)](analyzerinput/init(buffer:bufferstarttime:).md)
  Creates an audio input object for audio that may be discontiguous with previous input.
### Inspecting an input element
- [let buffer: AVAudioPCMBuffer](analyzerinput/buffer.md)
  The audio buffer containing this input.
- [let bufferStartTime: CMTime?](analyzerinput/bufferstarttime.md)
  The time-code of this input.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [protocol SpeechModuleResult](speechmoduleresult.md)
  Protocol that all module results conform to.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/analyzerinput)*