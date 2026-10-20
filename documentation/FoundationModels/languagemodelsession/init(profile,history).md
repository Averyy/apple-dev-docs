# init(profile:history:)

**Framework**: Foundation Models  
**Kind**: init  
**Role**: Initializer

Creates a session with a profile.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
convenience init(profile: sending some LanguageModelSession.DynamicProfile, history: some Collection<Transcript.Entry> = [])
```

## Mentions

- [Optimizing key-value caching in language model sessions](../optimizing-key-value-caching-in-language-model-sessions.md)
- [Composing dynamic sessions with instructions and profiles](../composing-dynamic-sessions-with-instructions-and-profiles.md)

## Parameters

- `profile`: The profile to use for this session.
- `history`: Transcript entries without the initial instructions, since that’s defined by the profile.

## See Also

### Creating a session with a dynamic profile
- [convenience init(model: some LanguageModel, dynamicInstructions: sending some DynamicInstructions, history: some Collection<Transcript.Entry>)](./init%28model,dynamicinstructions,history%29.md)
  Creates a session with dynamic instructions.
- [LanguageModelSession.DynamicProfile](./dynamicprofile.md)
  A dynamic profile that contains one or more profiles.
- [LanguageModelSession.DynamicProfileModifier](./dynamicprofilemodifier.md)
  A protocol for creating reusable wrappers around dynamic profile content.
- [LanguageModelSession.ConditionalDynamicProfile](./conditionaldynamicprofile.md)
  A dynamic profile that resolves to one of two profiles, depending on a condition.
- [LanguageModelSession.DynamicProfileBuilder](./dynamicprofilebuilder.md)
  A type that represents a dynamic profile builder.
- [LanguageModelSession.DynamicProfileModifierContent](./dynamicprofilemodifiercontent.md)
  A type that represents the dynamic profile a modifier applies to.
- [LanguageModelSession.ModifiedDynamicProfile](./modifieddynamicprofile.md)
  A dynamic profile with a modifier applied to it.
- [LanguageModelSession.AnyDynamicProfile](./anydynamicprofile.md)
  A type-erased dynamic profile.
- [LanguageModelSession.Profile](./profile.md)
  A profile that contains dynamic instructions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/languagemodelsession/init(profile:history:))*