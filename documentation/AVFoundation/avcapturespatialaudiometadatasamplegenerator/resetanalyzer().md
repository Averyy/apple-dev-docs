# resetAnalyzer()

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

Calling this method resets the analyzer to its initial state so that a new run of audio sample buffers can be analyzed.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
func resetAnalyzer()
```

```objc
- (void) resetAnalyzer;
```

## Discussion

Call this method if you need to abort generating the audio timed metadata buffer for audio already provided to [`analyzeAudioSample(_:)`](./analyzeaudiosample%28_%29.md).

## See Also

### Analyzing audio samples
- [func analyzeAudioSample(CMSampleBuffer) -> OSStatus](./analyzeaudiosample%28_%29.md)
  Analyzes the provided audio sample buffer for its contribution to the spatial audio timed metadata value.
- [func newTimedMetadataSampleBufferAndResetAnalyzer() -> Unmanaged<CMSampleBuffer>?](./newtimedmetadatasamplebufferandresetanalyzer%28%29.md)
  Creates a sample buffer containing a spatial audio timed metadata sample computed from all analyzed audio buffers, and resets the analyzer to its initial state.
- [var timedMetadataSampleBufferFormatDescription: CMFormatDescription](./timedmetadatasamplebufferformatdescription.md)
  Returns the format description of the sample buffer returned from the [`newTimedMetadataSampleBufferAndResetAnalyzer()`](./newtimedmetadatasamplebufferandresetanalyzer%28%29.md) method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturespatialaudiometadatasamplegenerator/resetanalyzer())*