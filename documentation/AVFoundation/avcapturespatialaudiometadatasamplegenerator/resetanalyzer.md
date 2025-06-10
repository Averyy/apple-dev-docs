# resetAnalyzer()

**Framework**: AVFoundation  
**Kind**: method

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)

## Declaration

```swift
func resetAnalyzer()
```

#### Discussion

Calling this method will reset the analyzer to its initial state so that a new run of audio sample buffers can be analyzed.

If the client needs to abort generating the audio timed metadata buffer for audio buffers already given to analyzeAudioSample:, calling this method is required to prepare the analyzer for a new run of sample buffers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturespatialaudiometadatasamplegenerator/resetanalyzer())*