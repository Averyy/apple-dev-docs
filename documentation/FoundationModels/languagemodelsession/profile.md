# LanguageModelSession.Profile

**Framework**: Foundation Models  
**Kind**: struct

A profile that contains dynamic instructions.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
struct Profile
```

## Mentions

- [Composing dynamic sessions with instructions and profiles](composing-dynamic-sessions-with-instructions-and-profiles.md)

#### Overview

A profile binds [`DynamicInstructions`](dynamicinstructions.md) to a set of session-level configuration values. The [`DynamicInstructions`](dynamicinstructions.md) describes the content and tools and a [`LanguageModelSession.DynamicProfile`](languagemodelsession/dynamicprofile.md) orchestrates transitions betwen session configurations.

```swift
Profile {
    // Custom instructions and tools for a creative task.
}
.model(PrivateCloudComputeLanguageModel())
// Use a higher creative temperature value when a person likes poetry.
.temperature(likesPoetry ? 0.8 : 0.1)
// Perform deeper reasoning when a person likes astronomy.
.reasoningLevel(likesAstronomy ? .deep : .light)
```

A [`LanguageModelSession.Profile`](languagemodelsession/profile.md) conforms to [`LanguageModelSession.DynamicProfile`](languagemodelsession/dynamicprofile.md) and includes all the same modifiers that you use to configure a unit of work to perform. Observe and react to key moments during a session by using life cycle modifiers. When a profile and a subprofile both register a callback, the framework calls both. The following shows observing [`onToolOutput(perform:)`](languagemodelsession/dynamicprofile/ontooloutput(perform:).md) to handle logging after a tool provides output:

```swift
Profile {
    // Custom instructions and tools for the task.
}
.onToolOutput { toolCall, output in
    // Runs after the tool to log any necessary activity.
}
```

## Topics

### Creating a profile
- [init(() -> some DynamicInstructions)](languagemodelsession/profile/init(_:).md)
  Creates a profile that contains dynamic instructions.

## Relationships

### Conforms To
- [LanguageModelSession.DynamicProfile](languagemodelsession/dynamicprofile.md)

## See Also

- [Composing dynamic sessions with instructions and profiles](composing-dynamic-sessions-with-instructions-and-profiles.md)
  Adapt sessions dynamically at runtime by loading instructions and tools based on the state of your app.
- [Origami: Crafting a dynamic tutorial for Apple Intelligence](origami-crafting-a-dynamic-tutorial-for-apple-intelligence.md)
  Build interactive experiences with Foundation Models and Private Cloud Compute using multimodal prompts.
- [protocol DynamicInstructions](dynamicinstructions.md)
  A type that represents dynamic instructions.
- [LanguageModelSession.DynamicProfile](languagemodelsession/dynamicprofile.md)
  A dynamic profile that contains one or more profiles.
- [LanguageModelSession.DynamicProfileModifier](languagemodelsession/dynamicprofilemodifier.md)
  A protocol for creating reusable wrappers around dynamic profile content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/languagemodelsession/profile)*