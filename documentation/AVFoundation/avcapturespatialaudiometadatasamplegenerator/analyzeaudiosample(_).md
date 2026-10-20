# analyzeAudioSample(_:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

Analyzes the provided audio sample buffer for its contribution to the spatial audio timed metadata value.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
func analyzeAudioSample(_ sbuf: CMSampleBuffer) -> OSStatus
```

```objc
- (OSStatus) analyzeAudioSample:(CMSampleBufferRef) sbuf;
```

#### Return Value

`noErr` if the sample is successfully analyzed, otherwise a non-zero error code.

#### Discussion

You must call this method with each and every spatial audio buffer you provide to [`AVAssetWriter`](../avassetwriter.md), so it can be analyzed for the generation of a proper spatial audio timed metadata value.

## Parameters

- `sbuf`: A sample buffer containing spatial audio.

## See Also

### Analyzing audio samples
- [func newTimedMetadataSampleBufferAndResetAnalyzer() -> Unmanaged<CMSampleBuffer>?](./newtimedmetadatasamplebufferandresetanalyzer%28%29.md)
  Creates a sample buffer containing a spatial audio timed metadata sample computed from all analyzed audio buffers, and resets the analyzer to its initial state.
- [var timedMetadataSampleBufferFormatDescription: CMFormatDescription](./timedmetadatasamplebufferformatdescription.md)
  Returns the format description of the sample buffer returned from the [`newTimedMetadataSampleBufferAndResetAnalyzer()`](./newtimedmetadatasamplebufferandresetanalyzer%28%29.md) method.
- [func resetAnalyzer()](./resetanalyzer%28%29.md)
  Calling this method resets the analyzer to its initial state so that a new run of audio sample buffers can be analyzed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturespatialaudiometadatasamplegenerator/analyzeaudiosample(_:))*