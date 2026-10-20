# buffer

**Framework**: Speech  
**Kind**: property  
**Role**: Instance Property

A new copy of the audio data for this input.

**Availability**:
- iOS 26.0+ - Deprecated in 27.0
- iPadOS 26.0+ - Deprecated in 27.0
- Mac Catalyst 26.0+ - Deprecated in 27.0
- macOS 26.0+ - Deprecated in 27.0
- tvOS 26.0+ - Deprecated in 27.0
- visionOS 26.0+ - Deprecated in 27.0

> **Deprecated**: use other AnalyzerInput properties to get information about audio

## Declaration

```swift
var buffer: AVAudioPCMBuffer { get }
```

## See Also

### Inspecting an input element
- [let bufferStartTime: CMTime?](./bufferstarttime.md)
  The time-code of this input.
- [let bufferDuration: CMTime](./bufferduration.md)
  The length of this input.
- [let bufferFormat: AVAudioFormat](./bufferformat.md)
  The audio format of this input.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/analyzerinput/buffer)*