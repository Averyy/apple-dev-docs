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

- [class SFVoiceAnalytics](sfvoiceanalytics.md)
  A collection of vocal analysis metrics.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/sfacousticfeature)*