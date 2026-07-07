# newTimedMetadataSampleBufferAndResetAnalyzer()

**Framework**: AVFoundation  
**Kind**: method

Creates a sample buffer containing a spatial audio timed metadata sample computed from all analyzed audio buffers, and resets the analyzer to its initial state.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+

## Declaration

```swift
func newTimedMetadataSampleBufferAndResetAnalyzer() -> Unmanaged<CMSampleBuffer>?
```

#### Return Value

A `CMSampleBufferRef` containing the spatial audio timed metadata sample, or `NULL` if no value can be computed.

#### Discussion

Call this method after you pass the last audio sample buffer of your recording to [`analyzeAudioSample(_:)`](avcapturespatialaudiometadatasamplegenerator/analyzeaudiosample(_:).md). Then pass the returned `CMSampleBufferRef` directly to your [`AVAssetWriterInput`](avassetwriterinput.md) to add the sample to your recording’s audio timed metadata track. Note that [`AVAssetWriter`](avassetwriter.md) expects one and only one spatial audio metadata sample buffer to be present in the timed metadata track.

> **Note**: Calling this method also resets the analyzer, making it ready for another run of audio sample buffers. Thus one generator can be re-used for multiple recordings.

## See Also

- [func analyzeAudioSample(CMSampleBuffer) -> OSStatus](avcapturespatialaudiometadatasamplegenerator/analyzeaudiosample(_:).md)
  Analyzes the provided audio sample buffer for its contribution to the spatial audio timed metadata value.
- [var timedMetadataSampleBufferFormatDescription: CMFormatDescription](avcapturespatialaudiometadatasamplegenerator/timedmetadatasamplebufferformatdescription.md)
  Returns the format description of the sample buffer returned from the [`newTimedMetadataSampleBufferAndResetAnalyzer()`](avcapturespatialaudiometadatasamplegenerator/newtimedmetadatasamplebufferandresetanalyzer().md) method.
- [func resetAnalyzer()](avcapturespatialaudiometadatasamplegenerator/resetanalyzer.md)
  Calling this method resets the analyzer to its initial state so that a new run of audio sample buffers can be analyzed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturespatialaudiometadatasamplegenerator/newtimedmetadatasamplebufferandresetanalyzer())*