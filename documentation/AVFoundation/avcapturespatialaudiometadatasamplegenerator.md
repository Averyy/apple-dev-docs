# AVCaptureSpatialAudioMetadataSampleGenerator

**Framework**: AVFoundation  
**Kind**: class

An interface for generating a spatial audio timed metadata sample.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+

## Declaration

```swift
class AVCaptureSpatialAudioMetadataSampleGenerator
```

## Topics

### Analyzing audio samples
- [func analyzeAudioSample(CMSampleBuffer) -> OSStatus](avcapturespatialaudiometadatasamplegenerator/analyzeaudiosample(_:).md)
  Analyzes the provided audio sample buffer for its contribution to the spatial audio timed metadata value.
- [func newTimedMetadataSampleBufferAndResetAnalyzer() -> Unmanaged<CMSampleBuffer>?](avcapturespatialaudiometadatasamplegenerator/newtimedmetadatasamplebufferandresetanalyzer.md)
  Creates a sample buffer containing a spatial audio timed metadata sample computed from all analyzed audio buffers, and resets the analyzer to its initial state.
- [var timedMetadataSampleBufferFormatDescription: CMFormatDescription](avcapturespatialaudiometadatasamplegenerator/timedmetadatasamplebufferformatdescription.md)
  Returns the format description of the sample buffer returned from the [`newTimedMetadataSampleBufferAndResetAnalyzer()`](avcapturespatialaudiometadatasamplegenerator/newtimedmetadatasamplebufferandresetanalyzer().md) method.
- [func resetAnalyzer()](avcapturespatialaudiometadatasamplegenerator/resetanalyzer.md)
  Calling this method resets the analyzer to its initial state so that a new run of audio sample buffers can be analyzed.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [Capturing Spatial Audio in your iOS app](capturing-spatial-audio-in-your-ios-app.md)
  Enhance your app’s audio recording capabilities by supporting Spatial Audio capture.
- [class AVCaptureVideoDataOutput](avcapturevideodataoutput.md)
  A capture output that records video and provides access to video frames for processing.
- [class AVCaptureAudioDataOutput](avcaptureaudiodataoutput.md)
  A capture output that records audio and provides access to audio sample buffers as they are recorded.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturespatialaudiometadatasamplegenerator)*