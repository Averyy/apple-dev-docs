# shimmer

**Framework**: Speech  
**Kind**: property

The variation in vocal volume stability (amplitude) in each frame of a transcription segment, expressed in decibels.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
@NSCopying
var shimmer: SFAcousticFeature { get }
```

## See Also

- [class SFAcousticFeature](sfacousticfeature.md)
  The value of a voice analysis metric.
- [var voicing: SFAcousticFeature](sfvoiceanalytics/voicing.md)
  The likelihood of a voice in each frame of a transcription segment.
- [var pitch: SFAcousticFeature](sfvoiceanalytics/pitch.md)
  The highness or lowness of the tone (fundamental frequency) in each frame of a transcription segment, expressed as a logarithm.
- [var jitter: SFAcousticFeature](sfvoiceanalytics/jitter.md)
  The variation in pitch in each frame of a transcription segment, expressed as a percentage of the frame’s fundamental frequency.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/sfvoiceanalytics/shimmer)*