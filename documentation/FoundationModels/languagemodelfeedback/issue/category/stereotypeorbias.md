# LanguageModelFeedback.Issue.Category.stereotypeOrBias

**Framework**: Foundation Models  
**Kind**: case  
**Role**: Case

A response that exhibits bias or perpetuates a stereotype.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+
- watchOS 27.0+

## Declaration

```swift
case stereotypeOrBias
```

## Discussion

A stereotype or bias issue might be where you ask the model to summarize an article written by a male, and the model doesn’t state the authors sex, but the model uses male pronouns.

## See Also

### Getting the issue category
- [LanguageModelFeedback.Issue.Category.didNotFollowInstructions](./didnotfollowinstructions.md)
  A response that doesn’t follow instructions correctly.
- [LanguageModelFeedback.Issue.Category.incorrect](./incorrect.md)
  An incorrect response.
- [LanguageModelFeedback.Issue.Category.suggestiveOrSexual](./suggestiveorsexual.md)
  A response with suggestive or sexual material.
- [LanguageModelFeedback.Issue.Category.tooVerbose](./tooverbose.md)
  An overly verbose response.
- [LanguageModelFeedback.Issue.Category.triggeredGuardrailUnexpectedly](./triggeredguardrailunexpectedly.md)
  An unexpected guardrail violation.
- [LanguageModelFeedback.Issue.Category.unhelpful](./unhelpful.md)
  An unhelpful response.
- [LanguageModelFeedback.Issue.Category.vulgarOrOffensive](./vulgaroroffensive.md)
  A response with vulgar or offensive material.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/languagemodelfeedback/issue/category/stereotypeorbias)*