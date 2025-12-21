# timedMetadataSampleBufferFormatDescription

**Framework**: AVFoundation  
**Kind**: property

Returns the format description of the sample buffer returned from the [`newTimedMetadataSampleBufferAndResetAnalyzer()`](avcapturespatialaudiometadatasamplegenerator/newtimedmetadatasamplebufferandresetanalyzer().md) method.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+

## Declaration

```swift
var timedMetadataSampleBufferFormatDescription: CMFormatDescription { get }
```

#### Discussion

Use this format description when creating your [`AVAssetWriter`](avassetwriter.md) track for spatial audio timed metadata.

## See Also

- [func analyzeAudioSample(CMSampleBuffer) -> OSStatus](avcapturespatialaudiometadatasamplegenerator/analyzeaudiosample(_:).md)
  Analyzes the provided audio sample buffer for its contribution to the spatial audio timed metadata value.
- [func newTimedMetadataSampleBufferAndResetAnalyzer() -> Unmanaged<CMSampleBuffer>?](avcapturespatialaudiometadatasamplegenerator/newtimedmetadatasamplebufferandresetanalyzer.md)
  Creates a sample buffer containing a spatial audio timed metadata sample computed from all analyzed audio buffers, and resets the analyzer to its initial state.
- [func resetAnalyzer()](avcapturespatialaudiometadatasamplegenerator/resetanalyzer.md)
  Calling this method resets the analyzer to its initial state so that a new run of audio sample buffers can be analyzed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturespatialaudiometadatasamplegenerator/timedmetadatasamplebufferformatdescription)*