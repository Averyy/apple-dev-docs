# logFeedbackAttachment(sentiment:issues:desiredOutput:)

**Framework**: Foundation Models  
**Kind**: method

Logs and serializes a feedback attachment that can be submitted to Apple.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+
- watchOS 27.0+ (Beta)

## Declaration

```swift
@discardableResult
final func logFeedbackAttachment(sentiment: LanguageModelFeedback.Sentiment?, issues: [LanguageModelFeedback.Issue] = [], desiredOutput: Transcript.Entry? = nil) -> Data
```

## Mentions

- [Inspecting session transcripts and reporting model feedback](inspecting-session-transcripts-and-reporting-model-feedback.md)
- [Improving the safety of generative model output](improving-the-safety-of-generative-model-output.md)
- [Prompting an on-device foundation model](prompting-an-on-device-foundation-model.md)

#### Return Value

A `Data` object containing the JSON-encoded feedback attachment that can be submitted to Feedback Assistant.

#### Discussion

This method creates a structured feedback attachment containing the session’s transcript and any provided feedback information. The attachment can be saved to a file and submitted to Apple using [`Feedback Assistant`](https://developer.apple.comhttps://feedbackassistant.apple.com).

If an error occurred during a previous response, any rejected entries that were rolled back from the transcript are included in the feedback data.

```swift
let session = LanguageModelSession()
let response = try await session.respond(to: "What is the capital of France?")

// Create feedback for a helpful response
let feedbackData = session.logFeedbackAttachment(sentiment: .positive)

// Or create feedback for a problematic response
let feedbackData = session.logFeedbackAttachment(
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

If your `desiredOutput` is a string, use [`Transcript.Entry.response(_:)`](transcript/entry/response(_:).md) to turn your desired output into a [`Transcript`](transcript.md) entry:

```swift
let text = Transcript.TextSegment(content: "The capital of France is Paris.")
let segment = Transcript.Segment.text(text)
let response = Transcript.Response(segments: [segment])
let entry = Transcript.Entry.response(response)
```

If your `desiredOutput` is a [`Generable`](generable.md) type, turning that into a [`Transcript`](transcript.md) entry is slightly different:

```swift
let customType = MyCustomType(...) // A generable type.
let structure = Transcript.StructuredSegment(schemaName: String(describing: Foo.self), content: customType.generatedContent)
let segment = Transcript.Segment.structure(structure)
let response = Transcript.Response(segments: [segment])
let entry = Transcript.Entry.response(response)
```

Finally, if you’d like to submit the feedback to Apple, write your feedback to a `.json` file and include the file as an attachment to [`Feedback Assistant`](https://developer.apple.comhttps://feedbackassistant.apple.com). You can include one or many feedback attachment in the same file:

```swift
let allFeedback = feedbackData + feedbackData2 + feedbackData3
let url = URL(fileURLWithPath: "path/to/save/feedback.json")
try allFeedback.write(to: url)
```

## Parameters

- `sentiment`: An optional sentiment rating about the model’s output (positive, negative, or neutral).
- `issues`: An array of specific issues identified with the model’s response. Defaults to an empty array.
- `desiredOutput`: An optional transcript entry showing what the desired output should have been.

## See Also

- [func logFeedbackAttachment(sentiment: LanguageModelFeedback.Sentiment?, issues: [LanguageModelFeedback.Issue], desiredResponseContent: (any ConvertibleToGeneratedContent)?) -> Data](languagemodelsession/logfeedbackattachment(sentiment:issues:desiredresponsecontent:).md)
- [func logFeedbackAttachment(sentiment: LanguageModelFeedback.Sentiment?, issues: [LanguageModelFeedback.Issue], desiredResponseText: String?) -> Data](languagemodelsession/logfeedbackattachment(sentiment:issues:desiredresponsetext:).md)
- [struct LanguageModelFeedback](languagemodelfeedback.md)
  Feedback appropriate for logging or attaching to Feedback Assistant.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/languagemodelsession/logfeedbackattachment(sentiment:issues:desiredoutput:))*