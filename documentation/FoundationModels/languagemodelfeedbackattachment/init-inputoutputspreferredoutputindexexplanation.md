# init(input:outputs:preferredOutputIndex:explanation:)

**Framework**: Foundation Models  
**Kind**: init

Creates feedback from a person that indicates their preference among several outputs generated for the same input.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
init(input: [Transcript.Entry], outputs: [[Transcript.Entry]], preferredOutputIndex: Array<[Transcript.Entry]>.Index, explanation: String? = nil)
```

#### Discussion

Typically each output will contain a single transcript entry representing the model’s response. The exception is for tool calling, where one example will contain three or more entries representing tool calls, tool outputs, and the final response.

## Parameters

- `input`: Transcript entries containing previous prompts and responses.
- `outputs`: Transcript entries for several candidate outputs.
- `explanation`: An optional explanation from the user about their choice.

## See Also

- [init(input: [Transcript.Entry], output: [Transcript.Entry], sentiment: LanguageModelFeedbackAttachment.Sentiment?, issues: [LanguageModelFeedbackAttachment.Issue], desiredOutputExamples: [[Transcript.Entry]])](languagemodelfeedbackattachment/init(input:output:sentiment:issues:desiredoutputexamples:).md)
  Creates feedback from a person regarding a single transcript.
- [LanguageModelFeedbackAttachment.Sentiment](languagemodelfeedbackattachment/sentiment.md)
  A sentiment regarding the model’s response.
- [LanguageModelFeedbackAttachment.Issue](languagemodelfeedbackattachment/issue.md)
  An issue with the model’s response.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/languagemodelfeedbackattachment/init(input:outputs:preferredoutputindex:explanation:))*