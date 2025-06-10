# LanguageModelFeedbackAttachment.Issue.Category

**Framework**: Foundation Models  
**Kind**: enum

Categories for model response issues.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
enum Category
```

## Topics

### Getting the issue category
- [LanguageModelFeedbackAttachment.Issue.Category.didNotFollowInstructions](languagemodelfeedbackattachment/issue/category/didnotfollowinstructions.md)
  The model did not follow instructions correctly.
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
### Accessing the hash value
- [var hashValue: Int](languagemodelfeedbackattachment/issue/category/hashvalue.md)
  The hash value.
- [func hash(into: inout Hasher)](languagemodelfeedbackattachment/issue/category/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Comparing issue categories
- [static func == (LanguageModelFeedbackAttachment.Issue.Category, LanguageModelFeedbackAttachment.Issue.Category) -> Bool](languagemodelfeedbackattachment/issue/category/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Default Implementations
- [Equatable Implementations](languagemodelfeedbackattachment/issue/category/equatable-implementations.md)

## Relationships

### Conforms To
- [CaseIterable](../Swift/CaseIterable.md)
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [init(category: LanguageModelFeedbackAttachment.Issue.Category, explanation: String?)](languagemodelfeedbackattachment/issue/init(category:explanation:).md)
  Creates a new issue


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/languagemodelfeedbackattachment/issue/category)*