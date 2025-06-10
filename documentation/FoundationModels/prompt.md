# Prompt

**Framework**: Foundation Models  
**Kind**: struct

A prompt from a person to the model.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
struct Prompt
```

## Mentions

- [Generating content and performing tasks with Foundation Models](generating-content-and-performing-tasks-with-foundation-models.md)

#### Overview

Prompts can contain content written by you, and outside source, or input directly from people using your app. You can initialize a `Prompt` from a string literal:

```swift
let prompt = Prompt("What are miniature schnauzers known for?")
```

To dynamically control the prompt’s content based on your app’s state, build a `Prompt` as a computed property. The code below shows if the Boolean is `true`, the prompt includes a second line of text:

```swift
let responseShouldRhyme = true
let prompt = Prompt {
    "Answer the following question from the user: \(userInput)"
    if responseShouldRhyme {
        "Your response MUST rhyme!"
    }
}
```

If your prompt includes input from people, consider wrapping the input in a string template with your own prompt to better steer the model’s response. For more information on handling inputs in your prompts, see [`Improving safety from generative model output`](improving-safety-from-generative-model-output.md).

## Topics

### Creating a prompt
- [init(_:)](prompt/init(_:).md)
- [struct PromptBuilder](promptbuilder.md)
  A type that represents a prompt builder.
- [protocol PromptRepresentable](promptrepresentable.md)
  A protocol that represents a prompt.
### Default Implementations
- [PromptRepresentable Implementations](prompt/promptrepresentable-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [PromptRepresentable](promptrepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class LanguageModelSession](languagemodelsession.md)
  An object that represents a session that interacts with a large language model.
- [struct Instructions](instructions.md)
  Instructions define the model’s intended behavior on prompts.
- [struct Transcript](transcript.md)
  A transcript that documents interactions with a language model.
- [struct GenerationOptions](generationoptions.md)
  Options that control how the model generates its response to a prompt.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/prompt)*