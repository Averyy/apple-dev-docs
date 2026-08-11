# LanguageModelSession.DynamicProfileBuilder

**Framework**: Foundation Models  
**Kind**: struct

A type that represents a dynamic profile builder.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
@resultBuilder
struct DynamicProfileBuilder
```

## Mentions

- [Composing dynamic sessions with instructions and profiles](composing-dynamic-sessions-with-instructions-and-profiles.md)

## Topics

### Building a dynamic profile
- [static func buildBlock<T>(T) -> T](languagemodelsession/dynamicprofilebuilder/buildblock(_:).md)
  Creates a builder with a block.
- [static func buildEither<TrueContent, FalseContent>(first: TrueContent) -> LanguageModelSession.ConditionalDynamicProfile<TrueContent, FalseContent>](languagemodelsession/dynamicprofilebuilder/buildeither(first:).md)
  Creates a builder with the first component.
- [static func buildEither<TrueContent, FalseContent>(second: FalseContent) -> LanguageModelSession.ConditionalDynamicProfile<TrueContent, FalseContent>](languagemodelsession/dynamicprofilebuilder/buildeither(second:).md)
  Creates a builder with the second component.
- [static func buildLimitedAvailability(some LanguageModelSession.DynamicProfile) -> LanguageModelSession.AnyDynamicProfile](languagemodelsession/dynamicprofilebuilder/buildlimitedavailability(_:).md)

## See Also

- [convenience init(profile: sending some LanguageModelSession.DynamicProfile, history: some Collection<Transcript.Entry>)](languagemodelsession/init(profile:history:).md)
  Creates a session with a profile.
- [convenience init(model: some LanguageModel, dynamicInstructions: sending some DynamicInstructions, history: some Collection<Transcript.Entry>)](languagemodelsession/init(model:dynamicinstructions:history:).md)
  Creates a session with dynamic instructions.
- [LanguageModelSession.DynamicProfile](languagemodelsession/dynamicprofile.md)
  A dynamic profile that contains one or more profiles.
- [LanguageModelSession.DynamicProfileModifier](languagemodelsession/dynamicprofilemodifier.md)
  A protocol for creating reusable wrappers around dynamic profile content.
- [LanguageModelSession.ConditionalDynamicProfile](languagemodelsession/conditionaldynamicprofile.md)
- [LanguageModelSession.DynamicProfileModifierContent](languagemodelsession/dynamicprofilemodifiercontent.md)
- [LanguageModelSession.ModifiedDynamicProfile](languagemodelsession/modifieddynamicprofile.md)
- [LanguageModelSession.AnyDynamicProfile](languagemodelsession/anydynamicprofile.md)
- [LanguageModelSession.Profile](languagemodelsession/profile.md)
  A profile that contains dynamic instructions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/languagemodelsession/dynamicprofilebuilder)*