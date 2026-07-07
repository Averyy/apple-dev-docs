# resetAnalyzer()

**Framework**: AVFoundation  
**Kind**: method

Calling this method resets the analyzer to its initial state so that a new run of audio sample buffers can be analyzed.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+

## Declaration

```swift
func resetAnalyzer()
```

#### Discussion

Call this method if you need to abort generating the audio timed metadata buffer for audio already provided to [`analyzeAudioSample(_:)`](avcapturespatialaudiometadatasamplegenerator/analyzeaudiosample(_:).md).

## See Also

- [func analyzeAudioSample(CMSampleBuffer) -> OSStatus](avcapturespatialaudiometadatasamplegenerator/analyzeaudiosample(_:).md)
  Analyzes the provided audio sample buffer for its contribution to the spatial audio timed metadata value.
- [func newTimedMetadataSampleBufferAndResetAnalyzer() -> Unmanaged<CMSampleBuffer>?](avcapturespatialaudiometadatasamplegenerator/newtimedmetadatasamplebufferandresetanalyzer.md)
  Creates a sample buffer containing a spatial audio timed metadata sample computed from all analyzed audio buffers, and resets the analyzer to its initial state.
- [var timedMetadataSampleBufferFormatDescription: CMFormatDescription](avcapturespatialaudiometadatasamplegenerator/timedmetadatasamplebufferformatdescription.md)
  Returns the format description of the sample buffer returned from the [`newTimedMetadataSampleBufferAndResetAnalyzer()`](avcapturespatialaudiometadatasamplegenerator/newtimedmetadatasamplebufferandresetanalyzer().md) method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturespatialaudiometadatasamplegenerator/resetanalyzer())*