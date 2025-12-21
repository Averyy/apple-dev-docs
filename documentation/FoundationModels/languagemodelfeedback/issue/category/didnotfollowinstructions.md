# LanguageModelFeedback.Issue.Category.didNotFollowInstructions

**Framework**: Foundation Models  
**Kind**: case

The model did not follow instructions correctly.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
case didNotFollowInstructions
```

#### Discussion

An instruction issue might be where you asked for a recipe in numbered steps, and the model provided a recipe but didn’t number the steps.

## See Also

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
  The response was not unhelpful.
- [LanguageModelFeedback.Issue.Category.vulgarOrOffensive](languagemodelfeedback/issue/category/vulgaroroffensive.md)
  The model produces vulgar or offensive material.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/languagemodelfeedback/issue/category/didnotfollowinstructions)*