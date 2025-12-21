# LanguageModelFeedback.Sentiment

**Framework**: Foundation Models  
**Kind**: enum

A sentiment regarding the model’s response.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
enum Sentiment
```

## Topics

### Getting sentiment
- [LanguageModelFeedback.Sentiment.negative](languagemodelfeedback/sentiment/negative.md)
  A negative sentiment
- [LanguageModelFeedback.Sentiment.neutral](languagemodelfeedback/sentiment/neutral.md)
  A neutral sentiment
- [LanguageModelFeedback.Sentiment.positive](languagemodelfeedback/sentiment/positive.md)
  A positive sentiment

## Relationships

### Conforms To
- [CaseIterable](../Swift/CaseIterable.md)
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [LanguageModelFeedback.Issue](languagemodelfeedback/issue.md)
  An issue with the model’s response.
- [func logFeedbackAttachment(sentiment: LanguageModelFeedback.Sentiment?, issues: [LanguageModelFeedback.Issue], desiredOutput: Transcript.Entry?) -> Data](languagemodelsession/logfeedbackattachment(sentiment:issues:desiredoutput:).md)
  Logs and serializes data that includes session information that you attach when reporting feedback to Apple.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/languagemodelfeedback/sentiment)*