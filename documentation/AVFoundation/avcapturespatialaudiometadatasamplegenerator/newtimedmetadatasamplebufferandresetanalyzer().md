# newTimedMetadataSampleBufferAndResetAnalyzer()

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

Creates a sample buffer containing a spatial audio timed metadata sample computed from all analyzed audio buffers, and resets the analyzer to its initial state.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
func newTimedMetadataSampleBufferAndResetAnalyzer() -> Unmanaged<CMSampleBuffer>?
```

```objc
- (CMSampleBufferRef) newTimedMetadataSampleBufferAndResetAnalyzer;
```

#### Return Value

A `CMSampleBufferRef` containing the spatial audio timed metadata sample, or `NULL` if no value can be computed.

#### Discussion

Call this method after you pass the last audio sample buffer of your recording to [`analyzeAudioSample(_:)`](./analyzeaudiosample%28_%29.md). Then pass the returned `CMSampleBufferRef` directly to your [`AVAssetWriterInput`](../avassetwriterinput.md) to add the sample to your recording’s audio timed metadata track. Note that [`AVAssetWriter`](../avassetwriter.md) expects one and only one spatial audio metadata sample buffer to be present in the timed metadata track.

> **Note**: Calling this method also resets the analyzer, making it ready for another run of audio sample buffers. Thus one generator can be re-used for multiple recordings.

## See Also

### Analyzing audio samples
- [func analyzeAudioSample(CMSampleBuffer) -> OSStatus](./analyzeaudiosample%28_%29.md)
  Analyzes the provided audio sample buffer for its contribution to the spatial audio timed metadata value.
- [var timedMetadataSampleBufferFormatDescription: CMFormatDescription](./timedmetadatasamplebufferformatdescription.md)
  Returns the format description of the sample buffer returned from the [`newTimedMetadataSampleBufferAndResetAnalyzer()`](./newtimedmetadatasamplebufferandresetanalyzer%28%29.md) method.
- [func resetAnalyzer()](./resetanalyzer%28%29.md)
  Calling this method resets the analyzer to its initial state so that a new run of audio sample buffers can be analyzed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturespatialaudiometadatasamplegenerator/newtimedmetadatasamplebufferandresetanalyzer())*