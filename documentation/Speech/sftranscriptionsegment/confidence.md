# confidence

**Framework**: Speech  
**Kind**: property

The level of confidence the speech recognizer has in its recognition of the speech transcribed for the segment.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
var confidence: Float { get }
```

#### Discussion

This property reflects the overall confidence in the recognition of the entire phrase. The value is `0` if there was no recognition, and it is closer to `1` when there is a high certainty that a transcription matches the user’s speech exactly. For example, a confidence value of `0.94` represents a very high confidence level, and is more likely to be correct than a transcription with a confidence value of `0.72`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/sftranscriptionsegment/confidence)*