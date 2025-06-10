# LanguageModelFeedbackAttachment.Sentiment

**Framework**: Foundation Models  
**Kind**: enum

A sentiment regarding the model’s response.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
enum Sentiment
```

## Topics

### Getting sentiment
- [LanguageModelFeedbackAttachment.Sentiment.negative](languagemodelfeedbackattachment/sentiment/negative.md)
  A negative sentiment
- [LanguageModelFeedbackAttachment.Sentiment.neutral](languagemodelfeedbackattachment/sentiment/neutral.md)
  A neutral sentiment
- [LanguageModelFeedbackAttachment.Sentiment.positive](languagemodelfeedbackattachment/sentiment/positive.md)
  A positive sentiment
- [static var allCases: [LanguageModelFeedbackAttachment.Sentiment]](languagemodelfeedbackattachment/sentiment/allcases-swift.type.property.md)
  A collection of all values of this type.
- [LanguageModelFeedbackAttachment.Sentiment.AllCases](languagemodelfeedbackattachment/sentiment/allcases-swift.typealias.md)
  A type that can represent a collection of all values of this type.
### Getting the hash value
- [var hashValue: Int](languagemodelfeedbackattachment/sentiment/hashvalue.md)
  The hash value.
- [func hash(into: inout Hasher)](languagemodelfeedbackattachment/sentiment/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Comparing sentiment
- [static func == (LanguageModelFeedbackAttachment.Sentiment, LanguageModelFeedbackAttachment.Sentiment) -> Bool](languagemodelfeedbackattachment/sentiment/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Default Implementations
- [Equatable Implementations](languagemodelfeedbackattachment/sentiment/equatable-implementations.md)

## Relationships

### Conforms To
- [CaseIterable](../Swift/CaseIterable.md)
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [init(input: [Transcript.Entry], output: [Transcript.Entry], sentiment: LanguageModelFeedbackAttachment.Sentiment?, issues: [LanguageModelFeedbackAttachment.Issue], desiredOutputExamples: [[Transcript.Entry]])](languagemodelfeedbackattachment/init(input:output:sentiment:issues:desiredoutputexamples:).md)
  Creates feedback from a person regarding a single transcript.
- [LanguageModelFeedbackAttachment.Issue](languagemodelfeedbackattachment/issue.md)
  An issue with the model’s response.
- [init(input: [Transcript.Entry], outputs: [[Transcript.Entry]], preferredOutputIndex: Array<[Transcript.Entry]>.Index, explanation: String?)](languagemodelfeedbackattachment/init(input:outputs:preferredoutputindex:explanation:).md)
  Creates feedback from a person that indicates their preference among several outputs generated for the same input.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/languagemodelfeedbackattachment/sentiment)*