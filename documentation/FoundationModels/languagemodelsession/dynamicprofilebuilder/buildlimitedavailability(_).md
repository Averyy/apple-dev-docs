# buildLimitedAvailability(_:)

**Framework**: Foundation Models  
**Kind**: method  
**Role**: Type Method

Creates a builder with a limited availability dynamic profile.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
@export(implementation)
static func buildLimitedAvailability(_ component: some LanguageModelSession.DynamicProfile) -> LanguageModelSession.AnyDynamicProfile
```

## Parameters

- `component`: The dynamic profile.

## See Also

### Building a dynamic profile
- [static func buildBlock<T>(T) -> T](./buildblock%28_%29.md)
  Creates a builder with a block.
- [static func buildEither<TrueContent, FalseContent>(first: TrueContent) -> LanguageModelSession.ConditionalDynamicProfile<TrueContent, FalseContent>](./buildeither%28first%29.md)
  Creates a builder with the first component.
- [static func buildEither<TrueContent, FalseContent>(second: FalseContent) -> LanguageModelSession.ConditionalDynamicProfile<TrueContent, FalseContent>](./buildeither%28second%29.md)
  Creates a builder with the second component.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/languagemodelsession/dynamicprofilebuilder/buildlimitedavailability(_:))*