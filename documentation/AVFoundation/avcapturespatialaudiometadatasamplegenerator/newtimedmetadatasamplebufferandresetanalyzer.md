# newTimedMetadataSampleBufferAndResetAnalyzer()

**Framework**: AVFoundation  
**Kind**: method

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)

## Declaration

```swift
func newTimedMetadataSampleBufferAndResetAnalyzer() -> Unmanaged<CMSampleBuffer>?
```

#### Return Value

Returns an CMSampleBuffer that contains the spatial audio timed metadata sample. If no value can be computed, NULL will be returned.

#### Discussion

Returns a CMSampleBuffer containing a spatial audio timed metadata sample containing the value computed from all of the prior audio sample buffers passed to analyzeAudioSample:. The analyzer is also reset to its initial state, making it ready for a new run of sample buffers.

This method is to be called after the last audio sample buffer has been passed to the client’s AVAssetWriterInput for audio. The returned CMSampleBuffer can be passed directly to the client’s AVAssetWriterInput for the audio timed metadata track. Note that it is expected that one and only one sample buffer be present in the timed metadata track.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturespatialaudiometadatasamplegenerator/newtimedmetadatasamplebufferandresetanalyzer())*