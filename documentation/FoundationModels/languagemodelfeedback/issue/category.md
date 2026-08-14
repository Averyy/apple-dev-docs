# LanguageModelFeedback.Issue.Category

**Framework**: Foundation Models  
**Kind**: enum

Categories for model response issues.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+
- watchOS 27.0+ (Beta)

## Declaration

```swift
enum Category
```

## Mentions

- [Inspecting session transcripts and reporting model feedback](inspecting-session-transcripts-and-reporting-model-feedback.md)

## Topics

### Getting the issue category
- [LanguageModelFeedback.Issue.Category.didNotFollowInstructions](languagemodelfeedback/issue/category/didnotfollowinstructions.md)
  The model did not follow instructions correctly.
- [LanguageModelFeedback.Issue.Category.incorrect](languagemodelfeedback/issue/category/incorrect.md)
  The model provided an incorrect response.
- [LanguageModelFeedback.Issue.Category.stereotypeOrBias](languagemodelfeedback/issue/category/stereotypeorbias.md)
  The model exhibited bias or perpetuated a stereotype.
- [LanguageModelFeedback.Issue.Category.suggestiveOrSexual](languagemodelfeedback/issue/category/suggestiveorsexual.md)
  The model produces suggestive or sexual material.
- [LanguageModelFeedback.Issue.Category.tooVerbose](languagemodelfeedback/issue/category/tooverbose.md)
  The response was too verbose.
- [LanguageModelFeedback.Issue.Category.triggeredGuardrailUnexpectedly](languagemodelfeedback/issue/category/triggeredguardrailunexpectedly.md)
  The model throws a guardrail violation when it shouldn’t.
- [LanguageModelFeedback.Issue.Category.unhelpful](languagemodelfeedback/issue/category/unhelpful.md)
  The response was unhelpful.
- [LanguageModelFeedback.Issue.Category.vulgarOrOffensive](languagemodelfeedback/issue/category/vulgaroroffensive.md)
  The model produces vulgar or offensive material.

## Relationships

### Conforms To
- [CaseIterable](../swift/caseiterable.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [init(category: LanguageModelFeedback.Issue.Category, explanation: String?)](languagemodelfeedback/issue/init(category:explanation:).md)
  Creates an issue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/languagemodelfeedback/issue/category)*