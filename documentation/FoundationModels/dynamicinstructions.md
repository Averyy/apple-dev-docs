# DynamicInstructions

**Framework**: Foundation Models  
**Kind**: protocol

A type that represents dynamic instructions.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
protocol DynamicInstructions
```

## Mentions

- [Composing dynamic sessions with instructions and profiles](composing-dynamic-sessions-with-instructions-and-profiles.md)
- [Optimizing key-value caching in language model sessions](optimizing-key-value-caching-in-language-model-sessions.md)

#### Overview

Dynamic instructions provide a declarative approach to assembling instructions and tools that a [`LanguageModelSession`](languagemodelsession.md) uses. The framework evaluates them before every request to the model, so the body can contain conditional logic that’s based on current app state.

```swift
struct PresentationInstructions: DynamicInstructions {
    // The data source for conditional instructions.
    var isEditingImage = true

    var body: some DynamicInstructions {
        // The instructions and tools that remain the same across any use of this type.
        Instructions {
            "Help people improve their presentation."
        }
        ListPhotosTool()
        AddPhotoTool()

        // Depending on the state of the app, include additional instructions
        // that provide the model with more task-specific instructions and tools.
        if isEditingImage {
            ImageEditingInstructions()
        }
    }
}
```

## Topics

### Implementing dynamic instructions
- [var body: Self.Body](dynamicinstructions/body-swift.property.md)
  The content of the dynamic instructions.
- [associatedtype Body : DynamicInstructions](dynamicinstructions/body-swift.associatedtype.md)
  The type of dynamic instructions that represent these instructions.
- [DynamicInstructions.ForEach](dynamicinstructions/foreach.md)
- [DynamicInstructions.SessionProperty](dynamicinstructions/sessionproperty.md)
### Building dynamic instructions
- [struct DynamicInstructionsBuilder](dynamicinstructionsbuilder.md)
- [struct EmptyDynamicInstructions](emptydynamicinstructions.md)
  An empty dynamic instructions type..
- [struct ConditionalDynamicInstructions](conditionaldynamicinstructions.md)
  A dynamic instructions type that conditionally selects between two conditions.
- [struct AnyDynamicInstructions](anydynamicinstructions.md)
  A dynamic instructions type that’s type-erased.
- [struct TupleDynamicInstructions](tupledynamicinstructions.md)
  A dynamic instructions type that represents a tuple.
- [struct AnyTool](anytool.md)
  A tool that the framework invokes in dynamic instructions.

## Relationships

### Conforming Types
- [AnyDynamicInstructions](anydynamicinstructions.md)
- [ConditionalDynamicInstructions](conditionaldynamicinstructions.md)
- [EmptyDynamicInstructions](emptydynamicinstructions.md)
- [Instructions](instructions.md)
- [TupleDynamicInstructions](tupledynamicinstructions.md)

## See Also

- [Composing dynamic sessions with instructions and profiles](composing-dynamic-sessions-with-instructions-and-profiles.md)
  Adapt sessions dynamically at runtime by loading instructions and tools based on the state of your app.
- [Origami: Crafting a dynamic tutorial for Apple Intelligence](origami-crafting-a-dynamic-tutorial-for-apple-intelligence.md)
  Build interactive experiences with Foundation Models and Private Cloud Compute using multimodal prompts.
- [LanguageModelSession.DynamicProfile](languagemodelsession/dynamicprofile.md)
  A dynamic profile that contains one or more profiles.
- [LanguageModelSession.DynamicProfileModifier](languagemodelsession/dynamicprofilemodifier.md)
  A protocol for creating reusable wrappers around dynamic profile content.
- [LanguageModelSession.Profile](languagemodelsession/profile.md)
  A profile that contains dynamic instructions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/dynamicinstructions)*