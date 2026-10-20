# AVCaptureSpatialAudioMetadataSampleGenerator

**Framework**: AVFoundation  
**Kind**: class  
**Role**: Class

An interface for generating a spatial audio timed metadata sample.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
class AVCaptureSpatialAudioMetadataSampleGenerator
```

```objc
@interface AVCaptureSpatialAudioMetadataSampleGenerator : NSObject
```

## Topics

### Analyzing audio samples
- [func analyzeAudioSample(CMSampleBuffer) -> OSStatus](./avcapturespatialaudiometadatasamplegenerator/analyzeaudiosample%28_%29.md)
  Analyzes the provided audio sample buffer for its contribution to the spatial audio timed metadata value.
- [func newTimedMetadataSampleBufferAndResetAnalyzer() -> Unmanaged<CMSampleBuffer>?](./avcapturespatialaudiometadatasamplegenerator/newtimedmetadatasamplebufferandresetanalyzer%28%29.md)
  Creates a sample buffer containing a spatial audio timed metadata sample computed from all analyzed audio buffers, and resets the analyzer to its initial state.
- [var timedMetadataSampleBufferFormatDescription: CMFormatDescription](./avcapturespatialaudiometadatasamplegenerator/timedmetadatasamplebufferformatdescription.md)
  Returns the format description of the sample buffer returned from the [`newTimedMetadataSampleBufferAndResetAnalyzer()`](./avcapturespatialaudiometadatasamplegenerator/newtimedmetadatasamplebufferandresetanalyzer%28%29.md) method.
- [func resetAnalyzer()](./avcapturespatialaudiometadatasamplegenerator/resetanalyzer%28%29.md)
  Calling this method resets the analyzer to its initial state so that a new run of audio sample buffers can be analyzed.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Stream capture
- [Capturing Spatial Audio in your iOS app](./capturing-spatial-audio-in-your-ios-app.md)
  Enhance your app’s audio recording capabilities by supporting Spatial Audio capture.
- [class AVCaptureVideoDataOutput](./avcapturevideodataoutput.md)
  A capture output that records video and provides access to video frames for processing.
- [class AVCaptureAudioDataOutput](./avcaptureaudiodataoutput.md)
  A capture output that records audio and provides access to audio sample buffers as they are recorded.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturespatialaudiometadatasamplegenerator)*