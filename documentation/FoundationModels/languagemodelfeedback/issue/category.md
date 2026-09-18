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
- watchOS 27.0+

## Declaration

```swift
enum Category
```

## Mentions

- [Inspecting session transcripts and reporting model feedback](inspecting-session-transcripts-and-reporting-model-feedback.md)

## Topics

### Getting the issue category
- [LanguageModelFeedback.Issue.Category.didNotFollowInstructions](languagemodelfeedback/issue/category/didnotfollowinstructions.md)
  A response that doesn’t follow instructions correctly.
- [LanguageModelFeedback.Issue.Category.incorrect](languagemodelfeedback/issue/category/incorrect.md)
  An incorrect response.
- [LanguageModelFeedback.Issue.Category.stereotypeOrBias](languagemodelfeedback/issue/category/stereotypeorbias.md)
  A response that exhibits bias or perpetuates a stereotype.
- [LanguageModelFeedback.Issue.Category.suggestiveOrSexual](languagemodelfeedback/issue/category/suggestiveorsexual.md)
  A response with suggestive or sexual material.
- [LanguageModelFeedback.Issue.Category.tooVerbose](languagemodelfeedback/issue/category/tooverbose.md)
  An overly verbose response.
- [LanguageModelFeedback.Issue.Category.triggeredGuardrailUnexpectedly](languagemodelfeedback/issue/category/triggeredguardrailunexpectedly.md)
  An unexpected guardrail violation.
- [LanguageModelFeedback.Issue.Category.unhelpful](languagemodelfeedback/issue/category/unhelpful.md)
  An unhelpful response.
- [LanguageModelFeedback.Issue.Category.vulgarOrOffensive](languagemodelfeedback/issue/category/vulgaroroffensive.md)
  A response with vulgar or offensive material.

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