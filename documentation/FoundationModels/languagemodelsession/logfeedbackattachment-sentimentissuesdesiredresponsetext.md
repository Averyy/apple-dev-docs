# logFeedbackAttachment(sentiment:issues:desiredResponseText:)

**Framework**: Foundation Models  
**Kind**: method

Logs and serializes a feedback attachment that includes the response text you expected.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+
- watchOS 27.0+

## Declaration

```swift
@backDeployed(before: iOS 26.1, macOS 26.1, visionOS 26.1)
@discardableResult final func logFeedbackAttachment(sentiment: LanguageModelFeedback.Sentiment?, issues: [LanguageModelFeedback.Issue] = [], desiredResponseText: String?) -> Data
```

## Mentions

- [Inspecting session transcripts and reporting model feedback](inspecting-session-transcripts-and-reporting-model-feedback.md)

#### Return Value

A `Data` object containing the JSON-encoded feedback attachment that can be submitted to Feedback Assistant.

## Parameters

- `sentiment`: An optional sentiment rating about the model’s output.
- `issues`: An array of specific issues identified with the model’s response. Defaults to an empty array.
- `desiredResponseText`: The text the model should have produced, if you have one.

## See Also

- [func logFeedbackAttachment(sentiment: LanguageModelFeedback.Sentiment?, issues: [LanguageModelFeedback.Issue], desiredOutput: Transcript.Entry?) -> Data](languagemodelsession/logfeedbackattachment(sentiment:issues:desiredoutput:).md)
  Logs and serializes a feedback attachment that can be submitted to Apple.
- [func logFeedbackAttachment(sentiment: LanguageModelFeedback.Sentiment?, issues: [LanguageModelFeedback.Issue], desiredResponseContent: (any ConvertibleToGeneratedContent)?) -> Data](languagemodelsession/logfeedbackattachment(sentiment:issues:desiredresponsecontent:).md)
  Logs and serializes a feedback attachment that includes the content you expected.
- [struct LanguageModelFeedback](languagemodelfeedback.md)
  Feedback appropriate for logging or attaching to Feedback Assistant.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/languagemodelsession/logfeedbackattachment(sentiment:issues:desiredresponsetext:))*