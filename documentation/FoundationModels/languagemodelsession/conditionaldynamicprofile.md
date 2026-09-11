# LanguageModelSession.ConditionalDynamicProfile

**Framework**: Foundation Models  
**Kind**: struct

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
struct ConditionalDynamicProfile<TrueContent, FalseContent> where TrueContent : LanguageModelSession.DynamicProfile, FalseContent : LanguageModelSession.DynamicProfile
```

## Relationships

### Conforms To
- [LanguageModelSession.DynamicProfile](languagemodelsession/dynamicprofile.md)

## See Also

- [convenience init(profile: sending some LanguageModelSession.DynamicProfile, history: some Collection<Transcript.Entry>)](languagemodelsession/init(profile:history:).md)
  Creates a session with a profile.
- [convenience init(model: some LanguageModel, dynamicInstructions: sending some DynamicInstructions, history: some Collection<Transcript.Entry>)](languagemodelsession/init(model:dynamicinstructions:history:).md)
  Creates a session with dynamic instructions.
- [LanguageModelSession.DynamicProfile](languagemodelsession/dynamicprofile.md)
  A dynamic profile that contains one or more profiles.
- [LanguageModelSession.DynamicProfileModifier](languagemodelsession/dynamicprofilemodifier.md)
  A protocol for creating reusable wrappers around dynamic profile content.
- [LanguageModelSession.DynamicProfileBuilder](languagemodelsession/dynamicprofilebuilder.md)
  A type that represents a dynamic profile builder.
- [LanguageModelSession.DynamicProfileModifierContent](languagemodelsession/dynamicprofilemodifiercontent.md)
- [LanguageModelSession.ModifiedDynamicProfile](languagemodelsession/modifieddynamicprofile.md)
- [LanguageModelSession.AnyDynamicProfile](languagemodelsession/anydynamicprofile.md)
- [LanguageModelSession.Profile](languagemodelsession/profile.md)
  A profile that contains dynamic instructions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/languagemodelsession/conditionaldynamicprofile)*