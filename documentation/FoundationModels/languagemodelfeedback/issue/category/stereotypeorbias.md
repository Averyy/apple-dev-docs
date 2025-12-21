# LanguageModelFeedback.Issue.Category.stereotypeOrBias

**Framework**: Foundation Models  
**Kind**: case

The model exhibited bias or perpetuated a stereotype.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
case stereotypeOrBias
```

#### Discussion

A stereotype or bias issue might be where you ask the model to summarize an article written by a male, and the model doesn’t state the authors sex, but the model uses male pronouns.

## See Also

- [LanguageModelFeedback.Issue.Category.didNotFollowInstructions](languagemodelfeedback/issue/category/didnotfollowinstructions.md)
  The model did not follow instructions correctly.
- [LanguageModelFeedback.Issue.Category.incorrect](languagemodelfeedback/issue/category/incorrect.md)
  The model provided an incorrect response.
- [LanguageModelFeedback.Issue.Category.suggestiveOrSexual](languagemodelfeedback/issue/category/suggestiveorsexual.md)
  The model produces suggestive or sexual material.
- [LanguageModelFeedback.Issue.Category.tooVerbose](languagemodelfeedback/issue/category/tooverbose.md)
  The response was too verbose.
- [LanguageModelFeedback.Issue.Category.triggeredGuardrailUnexpectedly](languagemodelfeedback/issue/category/triggeredguardrailunexpectedly.md)
  The model throws a guardrail violation when it shouldn’t.
- [LanguageModelFeedback.Issue.Category.unhelpful](languagemodelfeedback/issue/category/unhelpful.md)
  The response was not unhelpful.
- [LanguageModelFeedback.Issue.Category.vulgarOrOffensive](languagemodelfeedback/issue/category/vulgaroroffensive.md)
  The model produces vulgar or offensive material.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/languagemodelfeedback/issue/category/stereotypeorbias)*