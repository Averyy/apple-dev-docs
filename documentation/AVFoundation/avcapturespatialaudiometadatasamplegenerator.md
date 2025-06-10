# AVCaptureSpatialAudioMetadataSampleGenerator

**Framework**: AVFoundation  
**Kind**: class

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)

## Declaration

```swift
class AVCaptureSpatialAudioMetadataSampleGenerator
```

#### Overview

Defines an interface for generating a spatial audio timed metadata sample.

## Topics

### Instance Properties
- [var timedMetadataSampleBufferFormatDescription: CMFormatDescription](avcapturespatialaudiometadatasamplegenerator/timedmetadatasamplebufferformatdescription.md)
### Instance Methods
- [func analyzeAudioSample(CMSampleBuffer) -> OSStatus](avcapturespatialaudiometadatasamplegenerator/analyzeaudiosample(_:).md)
- [func newTimedMetadataSampleBufferAndResetAnalyzer() -> Unmanaged<CMSampleBuffer>?](avcapturespatialaudiometadatasamplegenerator/newtimedmetadatasamplebufferandresetanalyzer.md)
- [func resetAnalyzer()](avcapturespatialaudiometadatasamplegenerator/resetanalyzer.md)

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturespatialaudiometadatasamplegenerator)*