# LanguageModelSession.DynamicProfile

**Framework**: Foundation Models  
**Kind**: protocol

A dynamic profile that contains one or more profiles.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
protocol DynamicProfile
```

## Mentions

- [Composing dynamic sessions with instructions and profiles](composing-dynamic-sessions-with-instructions-and-profiles.md)
- [Expanding generation with tool calling](expanding-generation-with-tool-calling.md)

#### Overview

A dynamic profile is the top-level coordination layer that manages profiles. It determines which [`LanguageModelSession.DynamicProfile.Profile`](languagemodelsession/dynamicprofile/profile.md) is in an active state and allows a [`LanguageModelSession`](languagemodelsession.md) to switch between entirely different configurations as app state changes. A body must resolve to a single profile.

[`DynamicInstructions`](dynamicinstructions.md) declares what content and tools the model sees, and [`LanguageModelSession.DynamicProfile.Profile`](languagemodelsession/dynamicprofile/profile.md) binds that content to how a single configuration runs. That configuration includes details like the model to use, temperature, reasoning level, and so on.

```swift
struct PresentationProfile: LanguageModelSession.DynamicProfile {
    // The data source for the profile.
    var isEditingImage = true
    var isEditingAnimation = false

    // Determine which profile to load based on the current state.
    var body: some LanguageModelSession.DynamicProfile {
        if isEditingImage {
            // Use the editing image profile.
        } else if isEditingAnimation {
            // Use the editing animation profile.
        } else {
            // Use the default profile.
        }
    }
}
```

Use [`historyTransform(_:)`](languagemodelsession/dynamicprofile/historytransform(_:).md) to perform stateless transcript transforms. This allows you to modify the transcript that’s sent to the model, but doesn’t impact the global transcript state. For example, the request might only need the last twenty entries instead of the full transcript:

```swift
Profile {
    // The instructions and tools necessary for the task.
}
.historyTransform { history in
    Array(history.suffix(20))
}
```

## Topics

### Implementing a dynamic profile
- [var body: Self.Body](languagemodelsession/dynamicprofile/body-swift.property.md)
  The content of the dynamic profile.
- [associatedtype Body : LanguageModelSession.DynamicProfile](languagemodelsession/dynamicprofile/body-swift.associatedtype.md)
  The type of dynamic profile that represent this profile.
- [LanguageModelSession.DynamicProfile.DynamicProfile](languagemodelsession/dynamicprofile/dynamicprofile.md)
- [LanguageModelSession.DynamicProfile.Profile](languagemodelsession/dynamicprofile/profile.md)
- [LanguageModelSession.DynamicProfile.SessionProperty](languagemodelsession/dynamicprofile/sessionproperty.md)
### Transforming the history
- [func historyTransform(([Transcript.Entry]) -> [Transcript.Entry]) -> some LanguageModelSession.DynamicProfile](languagemodelsession/dynamicprofile/historytransform(_:).md)
  Apply a transformation to the history prior to invoking the model.
- [func inputFilter(([Transcript.Entry]) -> [Transcript.Entry]) -> some LanguageModelSession.DynamicProfile](languagemodelsession/dynamicprofile/inputfilter(_:).md)
  Apply a transformation to the transcript prior to invoking the model.
### Observing life cycle modifiers
- [func onActivate(perform: sending () async -> Void) -> some LanguageModelSession.DynamicProfile](languagemodelsession/dynamicprofile/onactivate(perform:).md)
  Runs an action when this dynamic profile becomes active.
- [func onDeactivate(perform: sending () async -> Void) -> some LanguageModelSession.DynamicProfile](languagemodelsession/dynamicprofile/ondeactivate(perform:).md)
  Runs an action when this dynamic profile becomes inactive.
- [func onPrompt(perform:)](languagemodelsession/dynamicprofile/onprompt(perform:).md)
  Runs an action before the model is invoked for this dynamic profile.
- [func onResponse(perform:)](languagemodelsession/dynamicprofile/onresponse(perform:).md)
  Runs an action after this dynamic profile produces a response.
- [func onToolCall(perform:)](languagemodelsession/dynamicprofile/ontoolcall(perform:).md)
  Runs an action whenever a tool is called within this dynamic profile.
- [func onToolOutput(perform:)](languagemodelsession/dynamicprofile/ontooloutput(perform:).md)
  Runs an action whenever a tool call output is received within this dynamic profile.
### Applying tool modifiers
- [func toolCallingMode(GenerationOptions.ToolCallingMode?) -> some LanguageModelSession.DynamicProfile](languagemodelsession/dynamicprofile/toolcallingmode(_:).md)
- [func toolCalling(GenerationOptions.ToolCallingMode?) -> some LanguageModelSession.DynamicProfile](languagemodelsession/dynamicprofile/toolcalling(_:).md)
### Configuring the model
- [func model(some LanguageModel) -> some LanguageModelSession.DynamicProfile](languagemodelsession/dynamicprofile/model(_:).md)
  Sets the model.
- [func temperature(Double?) -> some LanguageModelSession.DynamicProfile](languagemodelsession/dynamicprofile/temperature(_:).md)
  Sets the model temperature.
- [func samplingMode(GenerationOptions.SamplingMode?) -> some LanguageModelSession.DynamicProfile](languagemodelsession/dynamicprofile/samplingmode(_:).md)
  Sets the samping mode.
- [func reasoningLevel(ContextOptions.ReasoningLevel?) -> some LanguageModelSession.DynamicProfile](languagemodelsession/dynamicprofile/reasoninglevel(_:).md)
  Sets the reasoning level.
- [func maximumResponseTokens(Int?) -> some LanguageModelSession.DynamicProfile](languagemodelsession/dynamicprofile/maximumresponsetokens(_:).md)
  Sets the maximum response tokens.
- [func modifier<Modifier>(Modifier) -> some LanguageModelSession.DynamicProfile](languagemodelsession/dynamicprofile/modifier(_:).md)
  Apply a modifier to the dynamic profile.
### Handling the error policy
- [func transcriptErrorHandlingPolicy(TranscriptErrorHandlingPolicy?) -> some LanguageModelSession.DynamicProfile](languagemodelsession/dynamicprofile/transcripterrorhandlingpolicy(_:).md)
  The session’s policy for managing the transcript when errors occur.

## Relationships

### Conforming Types
- [LanguageModelSession.ConditionalDynamicProfile](languagemodelsession/conditionaldynamicprofile.md)
- [LanguageModelSession.DynamicProfileModifierContent](languagemodelsession/dynamicprofilemodifiercontent.md)
- [LanguageModelSession.ModifiedDynamicProfile](languagemodelsession/modifieddynamicprofile.md)
- [LanguageModelSession.Profile](languagemodelsession/profile.md)

## See Also

- [Composing dynamic sessions with instructions and profiles](composing-dynamic-sessions-with-instructions-and-profiles.md)
  Adapt sessions dynamically at runtime by loading instructions and tools based on the state of your app.
- [Origami: Crafting a dynamic tutorial for Apple Intelligence](origami-crafting-a-dynamic-tutorial-for-apple-intelligence.md)
  Build interactive experiences with Foundation Models and Private Cloud Compute using multimodal prompts.
- [protocol DynamicInstructions](dynamicinstructions.md)
  A type that represents dynamic instructions.
- [LanguageModelSession.DynamicProfileModifier](languagemodelsession/dynamicprofilemodifier.md)
  A protocol for creating reusable wrappers around dynamic profile content.
- [LanguageModelSession.Profile](languagemodelsession/profile.md)
  A profile that contains dynamic instructions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/languagemodelsession/dynamicprofile)*