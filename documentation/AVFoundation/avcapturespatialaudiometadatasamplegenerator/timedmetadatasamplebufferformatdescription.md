# timedMetadataSampleBufferFormatDescription

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

Returns the format description of the sample buffer returned from the [`newTimedMetadataSampleBufferAndResetAnalyzer()`](./newtimedmetadatasamplebufferandresetanalyzer%28%29.md) method.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
var timedMetadataSampleBufferFormatDescription: CMFormatDescription { get }
```

```objc
@property (nonatomic, readonly) CMFormatDescriptionRef timedMetadataSampleBufferFormatDescription;
```

## Discussion

Use this format description when creating your [`AVAssetWriter`](../avassetwriter.md) track for spatial audio timed metadata.

## See Also

### Analyzing audio samples
- [func analyzeAudioSample(CMSampleBuffer) -> OSStatus](./analyzeaudiosample%28_%29.md)
  Analyzes the provided audio sample buffer for its contribution to the spatial audio timed metadata value.
- [func newTimedMetadataSampleBufferAndResetAnalyzer() -> Unmanaged<CMSampleBuffer>?](./newtimedmetadatasamplebufferandresetanalyzer%28%29.md)
  Creates a sample buffer containing a spatial audio timed metadata sample computed from all analyzed audio buffers, and resets the analyzer to its initial state.
- [func resetAnalyzer()](./resetanalyzer%28%29.md)
  Calling this method resets the analyzer to its initial state so that a new run of audio sample buffers can be analyzed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturespatialaudiometadatasamplegenerator/timedmetadatasamplebufferformatdescription)*