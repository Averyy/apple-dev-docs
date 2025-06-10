# LanguageModelFeedbackAttachment.Issue.Category.stereotypeOrBias

**Framework**: Foundation Models  
**Kind**: case

The model exhibited bias or perpetuated a sterotype.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
case stereotypeOrBias
```

#### Discussion

A stereotype or bias issue might be where you ask the model to summarize an article written by a male, and the model doesn’t state the authors sex, but the model uses male pronouns.

## See Also

- [LanguageModelFeedbackAttachment.Issue.Category.didNotFollowInstructions](languagemodelfeedbackattachment/issue/category/didnotfollowinstructions.md)
  The model did not follow instructions correctly.
- [LanguageModelFeedbackAttachment.Issue.Category.incorrect](languagemodelfeedbackattachment/issue/category/incorrect.md)
  The model provided an incorrect response.
- [LanguageModelFeedbackAttachment.Issue.Category.suggestiveOrSexual](languagemodelfeedbackattachment/issue/category/suggestiveorsexual.md)
  The model produces suggestive or sexual material.
- [LanguageModelFeedbackAttachment.Issue.Category.tooVerbose](languagemodelfeedbackattachment/issue/category/tooverbose.md)
  The response was too verbose.
- [LanguageModelFeedbackAttachment.Issue.Category.triggeredGuardrailUnexpectedly](languagemodelfeedbackattachment/issue/category/triggeredguardrailunexpectedly.md)
  The model throws a guardrail violation when it shouldn’t.
- [LanguageModelFeedbackAttachment.Issue.Category.unhelpful](languagemodelfeedbackattachment/issue/category/unhelpful.md)
  The response was not unhelpful.
- [LanguageModelFeedbackAttachment.Issue.Category.vulgarOrOffensive](languagemodelfeedbackattachment/issue/category/vulgaroroffensive.md)
  The model produces vulgar or offensive material.
- [static var allCases: [LanguageModelFeedbackAttachment.Issue.Category]](languagemodelfeedbackattachment/issue/category/allcases-swift.type.property.md)
  A collection of all values of this type.
- [LanguageModelFeedbackAttachment.Issue.Category.AllCases](languagemodelfeedbackattachment/issue/category/allcases-swift.typealias.md)
  A type that can represent a collection of all values of this type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/languagemodelfeedbackattachment/issue/category/stereotypeorbias)*