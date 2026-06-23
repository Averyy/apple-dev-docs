# buildEither(second:)

**Framework**: Foundation Models  
**Kind**: method

Creates a builder with the second component.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
@export(implementation)
static func buildEither<TrueContent, FalseContent>(second content: FalseContent) -> LanguageModelSession.ConditionalDynamicProfile<TrueContent, FalseContent> where TrueContent : LanguageModelSession.DynamicProfile, FalseContent : LanguageModelSession.DynamicProfile
```

## See Also

- [static func buildBlock<T>(T) -> T](languagemodelsession/dynamicprofilebuilder/buildblock(_:).md)
  Creates a builder with a block.
- [static func buildEither<TrueContent, FalseContent>(first: TrueContent) -> LanguageModelSession.ConditionalDynamicProfile<TrueContent, FalseContent>](languagemodelsession/dynamicprofilebuilder/buildeither(first:).md)
  Creates a builder with the first component.
- [static func buildLimitedAvailability(some LanguageModelSession.DynamicProfile) -> LanguageModelSession.AnyDynamicProfile](languagemodelsession/dynamicprofilebuilder/buildlimitedavailability(_:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/languagemodelsession/dynamicprofilebuilder/buildeither(second:))*