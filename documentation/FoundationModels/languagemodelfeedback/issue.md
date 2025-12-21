# LanguageModelFeedback.Issue

**Framework**: Foundation Models  
**Kind**: struct

An issue with the model’s response.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
struct Issue
```

## Topics

### Initializing an issue
- [init(category: LanguageModelFeedback.Issue.Category, explanation: String?)](languagemodelfeedback/issue/init(category:explanation:).md)
  Creates a new issue
- [LanguageModelFeedback.Issue.Category](languagemodelfeedback/issue/category.md)
  Categories for model response issues.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [LanguageModelFeedback.Sentiment](languagemodelfeedback/sentiment.md)
  A sentiment regarding the model’s response.
- [func logFeedbackAttachment(sentiment: LanguageModelFeedback.Sentiment?, issues: [LanguageModelFeedback.Issue], desiredOutput: Transcript.Entry?) -> Data](languagemodelsession/logfeedbackattachment(sentiment:issues:desiredoutput:).md)
  Logs and serializes data that includes session information that you attach when reporting feedback to Apple.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/languagemodelfeedback/issue)*