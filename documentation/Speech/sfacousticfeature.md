# SFAcousticFeature

**Framework**: Speech  
**Kind**: class  
**Role**: Class

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

```objc
@interface SFAcousticFeature : NSObject
```

## Topics

### Inspecting a feature
- [var frameDuration: TimeInterval](./sfacousticfeature/frameduration.md)
  The duration of the audio frame.
- [var acousticFeatureValuePerFrame: [Double]](./sfacousticfeature/acousticfeaturevalueperframe-5krkk.md)
  An array of feature values, one value per audio frame, corresponding to a transcript segment of recorded audio.
- [acousticFeatureValuePerFrame](./sfacousticfeature/acousticfeaturevalueperframe-gsz5.md)
  An array of feature values, one value per audio frame, corresponding to a transcript segment of recorded audio.
### Initializers
- [init?(coder: NSCoder)](./sfacousticfeature/init%28coder%29.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)

## See Also

### Voice analytics
- [class SFVoiceAnalytics](./sfvoiceanalytics.md)
  A collection of vocal analysis metrics.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/sfacousticfeature)*