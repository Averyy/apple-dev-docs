# logFeedbackAttachment(sentiment:issues:desiredOutput:)

**Framework**: Foundation Models  
**Kind**: method

Logs and serializes data that includes session information that you attach when reporting feedback to Apple.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
@discardableResult
final func logFeedbackAttachment(sentiment: LanguageModelFeedback.Sentiment?, issues: [LanguageModelFeedback.Issue] = [], desiredOutput: Transcript.Entry? = nil) -> Data
```

## Mentions

- [Prompting an on-device foundation model](prompting-an-on-device-foundation-model.md)

#### Return Value

A `Data` object containing the JSON-encoded attachment.

#### Discussion

This method creates a structured attachment containing the session’s transcript and additional feedback information you provide. You can save the attachment data to a `.json` file and attach it when reporting feedback with [`Feedback Assistant`](https://developer.apple.comhttps://feedbackassistant.apple.com).

If an error occurs during a previous response, the method includes any rejected entries that were rolled back from the transcript in the feedback data.

```swift
let session = LanguageModelSession()
let response = try await session.respond(to: "What is the capital of France?")

// Create feedback for a helpful response.
let helpfulFeedbackData = session.logFeedbackAttachment(sentiment: .positive)

// Create feedback for a problematic response.
let problematicFeedbackData = session.logFeedbackAttachment(
    sentiment: .negative,
    issues: [
        LanguageModelFeedback.Issue(
            category: .incorrect,
            explanation: "The model provided outdated information"
        )
    ],
    desiredOutput: Transcript.Entry.response(...)
)
```

If `desiredOutput` is a string, use [`Transcript.Entry.response(_:)`](transcript/entry/response(_:).md) to turn your desired output into a [`Transcript`](transcript.md) entry:

```swift
let text = Transcript.TextSegment(content: "The capital of France is Paris.")
let segment = Transcript.Segment.text(text)
let response = Transcript.Response(segments: [segment])
let entry = Transcript.Entry.response(response)
```

To create a transcript when `desiredOutput` is a [`Generable`](generable.md) type:

```swift
let customType = MyCustomType(...) // A generable type.
let structure = Transcript.StructuredSegment(source: String(describing: Foo.self), content: customType.generatedContent)
let segment = Transcript.Segment.structure(structure)
let response = Transcript.Response(segments: [segment])
let entry = Transcript.Entry.response(response)
```

When you submit feedback to Apple, write your feedback to a `.json` file and include the file as an attachment to [`Feedback Assistant`](https://developer.apple.comhttps://feedbackassistant.apple.com). You can include multiple feedback attachments in the same file:

```swift
let allFeedback = helpfulFeedbackData + problematicFeedbackData
let url = URL(fileURLWithPath: "path/to/save/feedback.jsonl")
try allFeedback.write(to: url)
```

## Parameters

- `sentiment`: A   rating about the model’s output (positive,   negative, or neutral).
- `issues`: An array of specific   you identify with the model’s   response.
- `desiredOutput`: A   entry showing the output you expect.

## See Also

- [LanguageModelFeedback.Issue](languagemodelfeedback/issue.md)
  An issue with the model’s response.
- [LanguageModelFeedback.Sentiment](languagemodelfeedback/sentiment.md)
  A sentiment regarding the model’s response.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/languagemodelsession/logfeedbackattachment(sentiment:issues:desiredoutput:))*