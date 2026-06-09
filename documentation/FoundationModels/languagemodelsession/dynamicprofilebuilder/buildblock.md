# buildBlock(_:)

**Framework**: Foundation Models  
**Kind**: method

Creates a builder with a block.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
static func buildBlock<T>(_ content: T) -> T where T : LanguageModelSession.DynamicProfile
```

## See Also

- [static func buildEither<TrueContent, FalseContent>(first: TrueContent) -> LanguageModelSession.ConditionalDynamicProfile<TrueContent, FalseContent>](languagemodelsession/dynamicprofilebuilder/buildeither(first:).md)
  Creates a builder with the first component.
- [static func buildEither<TrueContent, FalseContent>(second: FalseContent) -> LanguageModelSession.ConditionalDynamicProfile<TrueContent, FalseContent>](languagemodelsession/dynamicprofilebuilder/buildeither(second:).md)
  Creates a builder with the second component.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/languagemodelsession/dynamicprofilebuilder/buildblock(_:))*