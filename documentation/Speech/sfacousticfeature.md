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
### Initializers
- [init?(coder: NSCoder)](sfacousticfeature/init(coder:).md)

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSCoding](../foundation/nscoding.md)
- [NSCopying](../foundation/nscopying.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [NSSecureCoding](../foundation/nssecurecoding.md)

## See Also

- [class SFVoiceAnalytics](sfvoiceanalytics.md)
  A collection of vocal analysis metrics.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/sfacousticfeature)*