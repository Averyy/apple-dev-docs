# voicing

**Framework**: Speech  
**Kind**: property  
**Role**: Instance Property

The likelihood of a voice in each frame of a transcription segment.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
@NSCopying
var voicing: SFAcousticFeature { get }
```

```objc
@property (nonatomic, copy, readonly) SFAcousticFeature * voicing;
```

## Discussion

The `voicing` value is expressed as a probability in the range `[0.0, 1.0]`.

## See Also

### Analyzing voice
- [class SFAcousticFeature](../sfacousticfeature.md)
  The value of a voice analysis metric.
- [var pitch: SFAcousticFeature](./pitch.md)
  The highness or lowness of the tone (fundamental frequency) in each frame of a transcription segment, expressed as a logarithm.
- [var jitter: SFAcousticFeature](./jitter.md)
  The variation in pitch in each frame of a transcription segment, expressed as a percentage of the frame’s fundamental frequency.
- [var shimmer: SFAcousticFeature](./shimmer.md)
  The variation in vocal volume stability (amplitude) in each frame of a transcription segment, expressed in decibels.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/sfvoiceanalytics/voicing)*