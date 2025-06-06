# valence

**Framework**: SensorKit  
**Kind**: property

The degree of positive or negative emotion or sentiment of the speaker.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+

## Declaration

```swift
var valence: Double { get }
```

#### Discussion

This property is a range from `-1` to `1`, where negative values indicate negative sentiment, and positive values indicate positive sentiment.

## See Also

- [var confidence: Double](srspeechexpression/confidence.md)
  The level of confidence of the speaker.
- [var mood: Double](srspeechexpression/mood.md)
  An indication of how slurry, tired, or exhausted the speaker sounds compared to normal speech.
- [var activation: Double](srspeechexpression/activation.md)
  The level of energy or activation of the speaker.
- [var dominance: Double](srspeechexpression/dominance.md)
  The degree of how strong or meek the speaker sounds.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sensorkit/srspeechexpression/valence)*