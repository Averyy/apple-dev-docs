# Prompt

**Framework**: Foundation Models  
**Kind**: struct

A prompt from a person to the model.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+
- watchOS 27.0+ (Beta)

## Declaration

```swift
struct Prompt
```

## Mentions

- [Generating content and performing tasks with Foundation Models](generating-content-and-performing-tasks-with-foundation-models.md)
- [Prompting an on-device foundation model](prompting-an-on-device-foundation-model.md)

#### Overview

Prompts can contain content written by you, an outside source, or input directly from people using your app. You can initialize a `Prompt` from a string literal:

```swift
let prompt = Prompt("What are miniature schnauzers known for?")
```

Use [`PromptBuilder`](promptbuilder.md) to dynamically control the prompt’s content based on your app’s state. The code below shows if the Boolean is `true`, the prompt includes a second line of text:

```swift
let responseShouldRhyme = true
let prompt = Prompt {
    "Answer the following question: Do Siberian Huskies love cold weather?"
    if responseShouldRhyme {
        "Your response MUST rhyme!"
    }
}
```

If your prompt includes input from people, consider wrapping the input in a string template with your own prompt to better steer the model’s response. For more information on handling inputs in your prompts, see [`Improving the safety of generative model output`](improving-the-safety-of-generative-model-output.md).

Prompting the same session eventually leads to exceeding the context window size. You can recover from this error by removing entries from the transcript and trying again. For more information on managing the context window size, see [`Managing the context window`](managing-the-context-window.md).

## Topics

### Creating a prompt
- [init(_:)](prompt/init(_:).md)
- [struct PromptBuilder](promptbuilder.md)
  A type that represents a prompt builder.
- [protocol PromptRepresentable](promptrepresentable.md)
  A type whose value can represent a prompt.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Escapable](../Swift/Escapable.md)
- [PromptRepresentable](promptrepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [Prompting an on-device foundation model](prompting-an-on-device-foundation-model.md)
  Tailor your prompts to get effective results from an on-device model.
- [Managing the context window](managing-the-context-window.md)
  Optimize your app’s token usage when prompting a model with the Foundation Models framework.
- [Updating prompts for new model versions](updating-prompts-for-new-model-versions.md)
  Manage the prompts your app uses by versioning them to make the most out of model improvements.
- [class LanguageModelSession](languagemodelsession.md)
  An object that represents a session that interacts with a language model.
- [struct Instructions](instructions.md)
  Details you provide that define the model’s intended behavior on prompts.
- [struct GenerationOptions](generationoptions.md)
  Options that control how the model generates its response to a prompt.
- [struct ContextOptions](contextoptions.md)
  Options that configure details that should appear in the prompt.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/prompt)*