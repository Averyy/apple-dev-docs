# LanguageModelFeedbackAttachment.Issue

**Framework**: Foundation Models  
**Kind**: struct

An issue with the model’s response.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
struct Issue
```

## Topics

### Initializing an issue
- [init(category: LanguageModelFeedbackAttachment.Issue.Category, explanation: String?)](languagemodelfeedbackattachment/issue/init(category:explanation:).md)
  Creates a new issue
- [LanguageModelFeedbackAttachment.Issue.Category](languagemodelfeedbackattachment/issue/category.md)
  Categories for model response issues.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [init(input: [Transcript.Entry], output: [Transcript.Entry], sentiment: LanguageModelFeedbackAttachment.Sentiment?, issues: [LanguageModelFeedbackAttachment.Issue], desiredOutputExamples: [[Transcript.Entry]])](languagemodelfeedbackattachment/init(input:output:sentiment:issues:desiredoutputexamples:).md)
  Creates feedback from a person regarding a single transcript.
- [LanguageModelFeedbackAttachment.Sentiment](languagemodelfeedbackattachment/sentiment.md)
  A sentiment regarding the model’s response.
- [init(input: [Transcript.Entry], outputs: [[Transcript.Entry]], preferredOutputIndex: Array<[Transcript.Entry]>.Index, explanation: String?)](languagemodelfeedbackattachment/init(input:outputs:preferredoutputindex:explanation:).md)
  Creates feedback from a person that indicates their preference among several outputs generated for the same input.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/languagemodelfeedbackattachment/issue)*