# init(input:output:sentiment:issues:desiredOutputExamples:)

**Framework**: Foundation Models  
**Kind**: init

Creates feedback from a person regarding a single transcript.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
init(input: [Transcript.Entry], output: [Transcript.Entry], sentiment: LanguageModelFeedbackAttachment.Sentiment?, issues: [LanguageModelFeedbackAttachment.Issue] = [], desiredOutputExamples: [[Transcript.Entry]] = [])
```

#### Discussion

Typically each output will contain a single transcript entry representing the model’s response. The exception is for tool calling, where one example will contain three or more entries representing tool calls, tool outputs, and the final response.

## Parameters

- `input`: Transcript entries containing previous prompts and responses.
- `output`: Transcript entries containing model output.
- `sentiment`: An optional sentiment about the model’s output.
- `issues`: Issues regarding the model’s response.
- `desiredOutputExamples`: Examples of desired outputs.

## See Also

- [LanguageModelFeedbackAttachment.Sentiment](languagemodelfeedbackattachment/sentiment.md)
  A sentiment regarding the model’s response.
- [LanguageModelFeedbackAttachment.Issue](languagemodelfeedbackattachment/issue.md)
  An issue with the model’s response.
- [init(input: [Transcript.Entry], outputs: [[Transcript.Entry]], preferredOutputIndex: Array<[Transcript.Entry]>.Index, explanation: String?)](languagemodelfeedbackattachment/init(input:outputs:preferredoutputindex:explanation:).md)
  Creates feedback from a person that indicates their preference among several outputs generated for the same input.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/languagemodelfeedbackattachment/init(input:output:sentiment:issues:desiredoutputexamples:))*