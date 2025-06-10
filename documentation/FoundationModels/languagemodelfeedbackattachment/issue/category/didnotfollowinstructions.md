# LanguageModelFeedbackAttachment.Issue.Category.didNotFollowInstructions

**Framework**: Foundation Models  
**Kind**: case

The model did not follow instructions correctly.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
case didNotFollowInstructions
```

#### Discussion

An instruction issue might be where you asked for a recipe in numbered steps, and the model provided a recipe but didn’t number the steps.

## See Also

- [LanguageModelFeedbackAttachment.Issue.Category.incorrect](languagemodelfeedbackattachment/issue/category/incorrect.md)
  The model provided an incorrect response.
- [LanguageModelFeedbackAttachment.Issue.Category.stereotypeOrBias](languagemodelfeedbackattachment/issue/category/stereotypeorbias.md)
  The model exhibited bias or perpetuated a sterotype.
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

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/languagemodelfeedbackattachment/issue/category/didnotfollowinstructions)*