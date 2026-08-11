# logFeedbackAttachment(sentiment:issues:desiredResponseContent:)

**Framework**: Foundation Models  
**Kind**: method

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+
- watchOS 27.0+ (Beta)

## Declaration

```swift
@backDeployed(before: iOS 26.1, macOS 26.1, visionOS 26.1)
@discardableResult final func logFeedbackAttachment(sentiment: LanguageModelFeedback.Sentiment?, issues: [LanguageModelFeedback.Issue] = [], desiredResponseContent: (any ConvertibleToGeneratedContent)?) -> Data
```

## Mentions

- [Inspecting session transcripts and reporting model feedback](inspecting-session-transcripts-and-reporting-model-feedback.md)

## See Also

- [func logFeedbackAttachment(sentiment: LanguageModelFeedback.Sentiment?, issues: [LanguageModelFeedback.Issue], desiredOutput: Transcript.Entry?) -> Data](languagemodelsession/logfeedbackattachment(sentiment:issues:desiredoutput:).md)
  Logs and serializes a feedback attachment that can be submitted to Apple.
- [func logFeedbackAttachment(sentiment: LanguageModelFeedback.Sentiment?, issues: [LanguageModelFeedback.Issue], desiredResponseText: String?) -> Data](languagemodelsession/logfeedbackattachment(sentiment:issues:desiredresponsetext:).md)
- [struct LanguageModelFeedback](languagemodelfeedback.md)
  Feedback appropriate for logging or attaching to Feedback Assistant.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/languagemodelsession/logfeedbackattachment(sentiment:issues:desiredresponsecontent:))*