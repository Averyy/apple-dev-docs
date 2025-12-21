# LanguageModelFeedback

**Framework**: Foundation Models  
**Kind**: struct

Feedback appropriate for logging or attaching to Feedback Assistant.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
struct LanguageModelFeedback
```

## Mentions

- [Improving the safety of generative model output](improving-the-safety-of-generative-model-output.md)

#### Overview

`LanguageModelFeedback` is a namespace with structures for describing feedback in a consistent way. [`LanguageModelFeedback.Sentiment`](languagemodelfeedback/sentiment.md) describes the sentiment of the feedback, while [`LanguageModelFeedback.Issue`](languagemodelfeedback/issue.md) offers a standard template for issues.

Given a model session, use [`logFeedbackAttachment(sentiment:issues:desiredOutput:)`](languagemodelsession/logfeedbackattachment(sentiment:issues:desiredoutput:).md) to produce structured feedback.

```swift
let session = LanguageModelSession()
let response = try await session.respond(to: "What is the capital of France?")

// Create feedback for a problematic response.
let feedbackData = session.logFeedbackAttachment(
    sentiment: LanguageModelFeedback.Sentiment.negative,
    issues: [
        LanguageModelFeedback.Issue(
            category: .incorrect,
            explanation: "The model provided outdated information"
        )
    ],
    desiredOutput: Transcript.Entry.response(...)
)
```

## Topics

### Creating feedback
- [LanguageModelFeedback.Issue](languagemodelfeedback/issue.md)
  An issue with the model’s response.
- [LanguageModelFeedback.Sentiment](languagemodelfeedback/sentiment.md)
  A sentiment regarding the model’s response.
- [func logFeedbackAttachment(sentiment: LanguageModelFeedback.Sentiment?, issues: [LanguageModelFeedback.Issue], desiredOutput: Transcript.Entry?) -> Data](languagemodelsession/logfeedbackattachment(sentiment:issues:desiredoutput:).md)
  Logs and serializes data that includes session information that you attach when reporting feedback to Apple.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/languagemodelfeedback)*