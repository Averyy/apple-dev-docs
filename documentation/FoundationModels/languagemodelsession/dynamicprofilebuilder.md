# LanguageModelSession.DynamicProfileBuilder

**Framework**: Foundation Models  
**Kind**: struct  
**Role**: Structure

A type that represents a dynamic profile builder.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
@resultBuilder
struct DynamicProfileBuilder
```

## Mentions

- [Composing dynamic sessions with instructions and profiles](../composing-dynamic-sessions-with-instructions-and-profiles.md)

## Topics

### Building a dynamic profile
- [static func buildBlock<T>(T) -> T](./dynamicprofilebuilder/buildblock%28_%29.md)
  Creates a builder with a block.
- [static func buildEither<TrueContent, FalseContent>(first: TrueContent) -> LanguageModelSession.ConditionalDynamicProfile<TrueContent, FalseContent>](./dynamicprofilebuilder/buildeither%28first%29.md)
  Creates a builder with the first component.
- [static func buildEither<TrueContent, FalseContent>(second: FalseContent) -> LanguageModelSession.ConditionalDynamicProfile<TrueContent, FalseContent>](./dynamicprofilebuilder/buildeither%28second%29.md)
  Creates a builder with the second component.
- [static func buildLimitedAvailability(some LanguageModelSession.DynamicProfile) -> LanguageModelSession.AnyDynamicProfile](./dynamicprofilebuilder/buildlimitedavailability%28_%29.md)
  Creates a builder with a limited availability dynamic profile.

## See Also

### Creating a session with a dynamic profile
- [convenience init(profile: sending some LanguageModelSession.DynamicProfile, history: some Collection<Transcript.Entry>)](./init%28profile,history%29.md)
  Creates a session with a profile.
- [convenience init(model: some LanguageModel, dynamicInstructions: sending some DynamicInstructions, history: some Collection<Transcript.Entry>)](./init%28model,dynamicinstructions,history%29.md)
  Creates a session with dynamic instructions.
- [LanguageModelSession.DynamicProfile](./dynamicprofile.md)
  A dynamic profile that contains one or more profiles.
- [LanguageModelSession.DynamicProfileModifier](./dynamicprofilemodifier.md)
  A protocol for creating reusable wrappers around dynamic profile content.
- [LanguageModelSession.ConditionalDynamicProfile](./conditionaldynamicprofile.md)
  A dynamic profile that resolves to one of two profiles, depending on a condition.
- [LanguageModelSession.DynamicProfileModifierContent](./dynamicprofilemodifiercontent.md)
  A type that represents the dynamic profile a modifier applies to.
- [LanguageModelSession.ModifiedDynamicProfile](./modifieddynamicprofile.md)
  A dynamic profile with a modifier applied to it.
- [LanguageModelSession.AnyDynamicProfile](./anydynamicprofile.md)
  A type-erased dynamic profile.
- [LanguageModelSession.Profile](./profile.md)
  A profile that contains dynamic instructions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/languagemodelsession/dynamicprofilebuilder)*