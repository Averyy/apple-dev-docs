# init(model:dynamicInstructions:history:)

**Framework**: Foundation Models  
**Kind**: init

Creates a session with dynamic instructions.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
convenience init(model: some LanguageModel, dynamicInstructions: sending some DynamicInstructions, history: some Collection<Transcript.Entry> = [])
```

## Mentions

- [Composing dynamic sessions with instructions and profiles](composing-dynamic-sessions-with-instructions-and-profiles.md)

## Parameters

- `dynamicInstructions`: The instructions to use for this session.
- `history`: Transcript entries without the initial instructions, since that’s defined by the profile.

## See Also

- [convenience init(profile: sending some LanguageModelSession.DynamicProfile, history: some Collection<Transcript.Entry>)](languagemodelsession/init(profile:history:).md)
  Creates a session with a profile.
- [LanguageModelSession.DynamicProfile](languagemodelsession/dynamicprofile.md)
  A dynamic profile that contains one or more profiles.
- [LanguageModelSession.DynamicProfileModifier](languagemodelsession/dynamicprofilemodifier.md)
  A protocol for creating reusable wrappers around dynamic profile content.
- [LanguageModelSession.ConditionalDynamicProfile](languagemodelsession/conditionaldynamicprofile.md)
  A dynamic profile that resolves to one of two profiles, depending on a condition.
- [LanguageModelSession.DynamicProfileBuilder](languagemodelsession/dynamicprofilebuilder.md)
  A type that represents a dynamic profile builder.
- [LanguageModelSession.DynamicProfileModifierContent](languagemodelsession/dynamicprofilemodifiercontent.md)
  A type that represents the dynamic profile a modifier applies to.
- [LanguageModelSession.ModifiedDynamicProfile](languagemodelsession/modifieddynamicprofile.md)
  A dynamic profile with a modifier applied to it.
- [LanguageModelSession.AnyDynamicProfile](languagemodelsession/anydynamicprofile.md)
  A type-erased dynamic profile.
- [LanguageModelSession.Profile](languagemodelsession/profile.md)
  A profile that contains dynamic instructions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/languagemodelsession/init(model:dynamicinstructions:history:))*