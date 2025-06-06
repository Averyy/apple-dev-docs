# SFAcousticFeature

**Framework**: Speech  
**Kind**: class

The value of a voice analysis metric.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
class SFAcousticFeature
```

## Topics

### Inspecting a feature
- [var frameDuration: TimeInterval](sfacousticfeature/frameduration.md)
  The duration of the audio frame.
- [var acousticFeatureValuePerFrame: [Double]](sfacousticfeature/acousticfeaturevalueperframe-5krkk.md)
  An array of feature values, one value per audio frame, corresponding to a transcript segment of recorded audio.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)

## See Also

- [var voicing: SFAcousticFeature](sfvoiceanalytics/voicing.md)
  The likelihood of a voice in each frame of a transcription segment.
- [var pitch: SFAcousticFeature](sfvoiceanalytics/pitch.md)
  The highness or lowness of the tone (fundamental frequency) in each frame of a transcription segment, expressed as a logarithm.
- [var jitter: SFAcousticFeature](sfvoiceanalytics/jitter.md)
  The variation in pitch in each frame of a transcription segment, expressed as a percentage of the frame’s fundamental frequency.
- [var shimmer: SFAcousticFeature](sfvoiceanalytics/shimmer.md)
  The variation in vocal volume stability (amplitude) in each frame of a transcription segment, expressed in decibels.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/sfacousticfeature)*