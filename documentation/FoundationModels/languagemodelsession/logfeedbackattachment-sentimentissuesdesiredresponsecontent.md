# logFeedbackAttachment(sentiment:issues:desiredResponseContent:)

**Framework**: Foundation Models  
**Kind**: method

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
@backDeployed(before: iOS 26.1, macOS 26.1, visionOS 26.1)
@discardableResult final func logFeedbackAttachment(sentiment: LanguageModelFeedback.Sentiment?, issues: [LanguageModelFeedback.Issue] = [], desiredResponseContent: (any ConvertibleToGeneratedContent)?) -> Data
```

## See Also

- [func logFeedbackAttachment(sentiment: LanguageModelFeedback.Sentiment?, issues: [LanguageModelFeedback.Issue], desiredOutput: Transcript.Entry?) -> Data](languagemodelsession/logfeedbackattachment(sentiment:issues:desiredoutput:).md)
  Logs and serializes data that includes session information that you attach when reporting feedback to Apple.
- [func logFeedbackAttachment(sentiment: LanguageModelFeedback.Sentiment?, issues: [LanguageModelFeedback.Issue], desiredResponseText: String?) -> Data](languagemodelsession/logfeedbackattachment(sentiment:issues:desiredresponsetext:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/languagemodelsession/logfeedbackattachment(sentiment:issues:desiredresponsecontent:))*