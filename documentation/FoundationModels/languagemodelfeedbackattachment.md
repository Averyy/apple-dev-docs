# LanguageModelFeedbackAttachment

**Framework**: Foundation Models  
**Kind**: struct

Feedback appropriate for attaching to Feedback Assistant.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
struct LanguageModelFeedbackAttachment
```

## Mentions

- [Improving safety from generative model output](improving-safety-from-generative-model-output.md)

#### Overview

Use this type to build out user feedback experiences in your app. After collecting feedback, serialize them into a JSON or JSONL file and submit it to Apple using Feedback Assistant. This type supports simple thumbs up or down feedback experiences, all the way to experiences that ask people to compare multiple outputs and explain their preferences.

The following code shows creating a `LanguageModelFeedbackAttachment` using the session transcript to find the input for the provided input. Then, it encodes the data for you to use when submitting feedback.

```swift
private func submitFeedback(entry: Transcript.Entry, positive: Bool) {
    // Create a feedback object with the model input, output, and a sentiment value.
    let feedback = LanguageModelFeedbackAttachment(
      input: Array(session.trancript.entries.prefix(while: { $0 != entry })),
      output: [entry],
      sentiment: positive ? .positive : .negative
    )

    // Convert the feedback to JSON.
    let json = try! JSONEncoder().encode(feedback)

    // Manually submit the data file through Feedback Assistant.
}
```

## Topics

### Creating feedback
- [init(input: [Transcript.Entry], output: [Transcript.Entry], sentiment: LanguageModelFeedbackAttachment.Sentiment?, issues: [LanguageModelFeedbackAttachment.Issue], desiredOutputExamples: [[Transcript.Entry]])](languagemodelfeedbackattachment/init(input:output:sentiment:issues:desiredoutputexamples:).md)
  Creates feedback from a person regarding a single transcript.
- [LanguageModelFeedbackAttachment.Sentiment](languagemodelfeedbackattachment/sentiment.md)
  A sentiment regarding the model’s response.
- [LanguageModelFeedbackAttachment.Issue](languagemodelfeedbackattachment/issue.md)
  An issue with the model’s response.
- [init(input: [Transcript.Entry], outputs: [[Transcript.Entry]], preferredOutputIndex: Array<[Transcript.Entry]>.Index, explanation: String?)](languagemodelfeedbackattachment/init(input:outputs:preferredoutputindex:explanation:).md)
  Creates feedback from a person that indicates their preference among several outputs generated for the same input.
### Encoding feedback
- [func encode(to: any Encoder) throws](languagemodelfeedbackattachment/encode(to:).md)
  Encodes this value into the given encoder.

## Relationships

### Conforms To
- [Encodable](../Swift/Encodable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/languagemodelfeedbackattachment)*