# dominance

**Framework**: SensorKit  
**Kind**: property  
**Role**: Instance Property

The degree of how strong or meek the speaker sounds.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+

## Declaration

```swift
var dominance: Double { get }
```

```objc
@property (nonatomic, assign, readonly) double dominance;
```

## Discussion

This property is a range from `-1` to `1`, where negative values indicate negative sentiment, and positive values indicate positive sentiment.

## See Also

### Getting speech analytics
- [var confidence: Double](./confidence.md)
  The level of confidence of the speaker.
- [var mood: Double](./mood.md)
  An indication of how slurry, tired, or exhausted the speaker sounds compared to normal speech.
- [var valence: Double](./valence.md)
  The degree of positive or negative emotion or sentiment of the speaker.
- [var activation: Double](./activation.md)
  The level of energy or activation of the speaker.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sensorkit/srspeechexpression/dominance)*