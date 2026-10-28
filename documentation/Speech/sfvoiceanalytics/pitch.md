# pitch

**Framework**: Speech  
**Kind**: property  
**Role**: Instance Property

The highness or lowness of the tone (fundamental frequency) in each frame of a transcription segment, expressed as a logarithm.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
@NSCopying
var pitch: SFAcousticFeature { get }
```

```objc
@property (nonatomic, copy, readonly) SFAcousticFeature * pitch;
```

## Discussion

The value is a logarithm (base `e`) of the normalized pitch estimate for each frame.

## See Also

### Analyzing voice
- [class SFAcousticFeature](../sfacousticfeature.md)
  The value of a voice analysis metric.
- [var voicing: SFAcousticFeature](./voicing.md)
  The likelihood of a voice in each frame of a transcription segment.
- [var jitter: SFAcousticFeature](./jitter.md)
  The variation in pitch in each frame of a transcription segment, expressed as a percentage of the frame’s fundamental frequency.
- [var shimmer: SFAcousticFeature](./shimmer.md)
  The variation in vocal volume stability (amplitude) in each frame of a transcription segment, expressed in decibels.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/sfvoiceanalytics/pitch)*