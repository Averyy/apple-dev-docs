# LanguageModelSession.DynamicProfile

**Framework**: Foundation Models  
**Kind**: protocol  
**Role**: Protocol

A dynamic profile that contains one or more profiles.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
protocol DynamicProfile
```

## Mentions

- [Composing dynamic sessions with instructions and profiles](../composing-dynamic-sessions-with-instructions-and-profiles.md)
- [Expanding generation with tool calling](../expanding-generation-with-tool-calling.md)

#### Overview

A dynamic profile is the top-level coordination layer that manages profiles. It determines which [`LanguageModelSession.DynamicProfile.Profile`](./dynamicprofile/profile.md) is in an active state and allows a [`LanguageModelSession`](../languagemodelsession.md) to switch between entirely different configurations as app state changes. A body must resolve to a single profile.

[`DynamicInstructions`](../dynamicinstructions.md) declares what content and tools the model sees, and [`LanguageModelSession.DynamicProfile.Profile`](./dynamicprofile/profile.md) binds that content to how a single configuration runs. That configuration includes details like the model to use, temperature, reasoning level, and so on.

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

Use [`historyTransform(_:)`](./dynamicprofile/historytransform%28_%29.md) to perform stateless transcript transforms. This allows you to modify the transcript that’s sent to the model, but doesn’t impact the global transcript state. For example, the request might only need the last twenty entries instead of the full transcript:

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
- [var body: Self.Body](./dynamicprofile/body-swift.property.md)
  The content of the dynamic profile.
- [associatedtype Body : LanguageModelSession.DynamicProfile](./dynamicprofile/body-swift.associatedtype.md)
  The type of dynamic profile that represent this profile.
- [LanguageModelSession.DynamicProfile.DynamicProfile](./dynamicprofile/dynamicprofile.md)
  The dynamic profile type that a dynamic profile’s body composes.
- [LanguageModelSession.DynamicProfile.Profile](./dynamicprofile/profile.md)
  The profile type that a dynamic profile activates.
- [LanguageModelSession.DynamicProfile.SessionProperty](./dynamicprofile/sessionproperty.md)
  A property wrapper that provides access to a session property from within a dynamic profile.
### Transforming the history
- [func historyTransform(([Transcript.Entry]) -> [Transcript.Entry]) -> some LanguageModelSession.DynamicProfile](./dynamicprofile/historytransform%28_%29.md)
  Applies a transformation to the history prior to invoking the model.
### Observing life cycle modifiers
- [func onActivate(perform: sending () async -> Void) -> some LanguageModelSession.DynamicProfile](./dynamicprofile/onactivate%28perform%29.md)
  Runs an action when this dynamic profile becomes active.
- [func onDeactivate(perform: sending () async -> Void) -> some LanguageModelSession.DynamicProfile](./dynamicprofile/ondeactivate%28perform%29.md)
  Runs an action when this dynamic profile becomes inactive.
- [func onPrompt(perform:)](./dynamicprofile/onprompt%28perform%29.md)
  Runs an action before the model is invoked for this dynamic profile.
- [func onReasoning(perform:)](./dynamicprofile/onreasoning%28perform%29.md)
  Runs an action whenever this dynamic profile produces reasoning.
- [func onResponse(perform:)](./dynamicprofile/onresponse%28perform%29.md)
  Runs an action after this dynamic profile produces a response.
- [func onToolCall(perform:)](./dynamicprofile/ontoolcall%28perform%29.md)
  Runs an action whenever a tool is called within this dynamic profile.
- [func onToolOutput(perform:)](./dynamicprofile/ontooloutput%28perform%29.md)
  Runs an action whenever a tool call output is received within this dynamic profile.
### Applying tool modifiers
- [func toolCallingMode(GenerationOptions.ToolCallingMode?) -> some LanguageModelSession.DynamicProfile](./dynamicprofile/toolcallingmode%28_%29.md)
  Sets the tool-calling mode.
### Configuring the model
- [func model(_:)](./dynamicprofile/model%28_%29.md)
  Sets the model.
- [func temperature(Double?) -> some LanguageModelSession.DynamicProfile](./dynamicprofile/temperature%28_%29.md)
  Sets the model temperature.
- [func samplingMode(GenerationOptions.SamplingMode?) -> some LanguageModelSession.DynamicProfile](./dynamicprofile/samplingmode%28_%29.md)
  Sets the samping mode.
- [func reasoningLevel(ContextOptions.ReasoningLevel?) -> some LanguageModelSession.DynamicProfile](./dynamicprofile/reasoninglevel%28_%29.md)
  Sets the reasoning level.
- [func maximumResponseTokens(Int?) -> some LanguageModelSession.DynamicProfile](./dynamicprofile/maximumresponsetokens%28_%29.md)
  Sets the maximum response tokens.
- [func modifier<Modifier>(Modifier) -> some LanguageModelSession.DynamicProfile](./dynamicprofile/modifier%28_%29.md)
  Applies a modifier to the dynamic profile.
### Handling the error policy
- [func transcriptErrorHandlingPolicy(TranscriptErrorHandlingPolicy?) -> some LanguageModelSession.DynamicProfile](./dynamicprofile/transcripterrorhandlingpolicy%28_%29.md)
  Sets the policy for managing the transcript when errors occur.

## Relationships

### Conforming Types
- [LanguageModelSession.AnyDynamicProfile](./anydynamicprofile.md)
- [LanguageModelSession.ConditionalDynamicProfile](./conditionaldynamicprofile.md)
- [LanguageModelSession.DynamicProfileModifierContent](./dynamicprofilemodifiercontent.md)
- [LanguageModelSession.ModifiedDynamicProfile](./modifieddynamicprofile.md)
- [LanguageModelSession.Profile](./profile.md)

## See Also

### Dynamic profiles
- [Composing dynamic sessions with instructions and profiles](../composing-dynamic-sessions-with-instructions-and-profiles.md)
  Adapt sessions dynamically at runtime by loading instructions and tools based on the state of your app.
- [Origami: Crafting a dynamic tutorial for Apple Intelligence](../origami-crafting-a-dynamic-tutorial-for-apple-intelligence.md)
  Build interactive experiences with Foundation Models and Private Cloud Compute using multimodal prompts.
- [protocol DynamicInstructions](../dynamicinstructions.md)
  A type that represents dynamic instructions.
- [struct DynamicInstructionsForEach](../dynamicinstructionsforeach.md)
  Dynamic instructions that produce content for each element of a collection.
- [LanguageModelSession.DynamicProfileModifier](./dynamicprofilemodifier.md)
  A protocol for creating reusable wrappers around dynamic profile content.
- [LanguageModelSession.Profile](./profile.md)
  A profile that contains dynamic instructions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/languagemodelsession/dynamicprofile)*