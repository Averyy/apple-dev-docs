# LanguageModelSession.DynamicProfileModifier

**Framework**: Foundation Models  
**Kind**: protocol

A protocol for creating reusable wrappers around dynamic profile content.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
protocol DynamicProfileModifier
```

## Mentions

- [Composing dynamic sessions with instructions and profiles](composing-dynamic-sessions-with-instructions-and-profiles.md)

## Topics

### Implementing a profile modifier
- [func body(content: Self.Content) -> Self.Body](languagemodelsession/dynamicprofilemodifier/body(content:).md)
  The content of the dynamic profile modifier.
- [LanguageModelSession.DynamicProfileModifier.Content](languagemodelsession/dynamicprofilemodifier/content.md)
- [associatedtype Body : LanguageModelSession.DynamicProfile](languagemodelsession/dynamicprofilemodifier/body.md)
  The type of dynamic profile modifier that represents this modifier.
- [LanguageModelSession.DynamicProfileModifier.SessionProperty](languagemodelsession/dynamicprofilemodifier/sessionproperty.md)
- [LanguageModelSession.DynamicProfileModifier.DynamicProfile](languagemodelsession/dynamicprofilemodifier/dynamicprofile.md)

## See Also

- [Composing dynamic sessions with instructions and profiles](composing-dynamic-sessions-with-instructions-and-profiles.md)
  Adapt sessions dynamically at runtime by loading instructions and tools based on the state of your app.
- [Origami: Crafting a dynamic tutorial for Apple Intelligence](origami-crafting-a-dynamic-tutorial-for-apple-intelligence.md)
  Build interactive experiences with Foundation Models and Private Cloud Compute using multimodal prompts.
- [protocol DynamicInstructions](dynamicinstructions.md)
  A type that represents dynamic instructions.
- [LanguageModelSession.DynamicProfile](languagemodelsession/dynamicprofile.md)
  A dynamic profile that contains one or more profiles.
- [LanguageModelSession.Profile](languagemodelsession/profile.md)
  A profile that contains dynamic instructions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/languagemodelsession/dynamicprofilemodifier)*