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

Use [`PromptBuilder`](promptbuilder.md) to dynamically control the prompt’s content based on your app’s state. The code below shows that if the Boolean is `true`, the prompt includes a second line of text:

```swift
let responseShouldRhyme = true
let prompt = Prompt {
    "Answer the following question from the user: \(userInput)"
    if responseShouldRhyme {
        "Your response MUST rhyme!"
    }
}
```

If your prompt includes input from people, consider wrapping the input in a string template with your own prompt to better steer the model’s response. For more information on handling inputs in your prompts, see [`Improving the safety of generative model output`](improving-the-safety-of-generative-model-output.md).

All input to the model contributes tokens to the context window of the [`LanguageModelSession`](languagemodelsession.md) — including the [`Instructions`](instructions.md), [`Prompt`](prompt.md), [`Tool`](tool.md), and [`Generable`](generable.md) types, and the model’s responses. If your session exceeds the available context size, it throws [`LanguageModelSession.GenerationError.exceededContextWindowSize(_:)`](languagemodelsession/generationerror/exceededcontextwindowsize(_:).md).

Prompts can consume a lot of tokens, especially when you send multiple prompts to the same session. To reduce your prompt size when you exceed the context window size:

- Write shorter prompts to save tokens.
- Provide only the information necessary to perform the task.
- Use concise and imperative language instead of indirect or jargon that the model might misinterpret.
- Use a clear verb that tells the model what to do, like “Generate”, “List”, or “Summarize”.
- Include the target response length you want, like “In three sentences” or “List five reasons”.

Prompting the same session eventually leads to exceeding the context window size. When that happens, create a new context window by initializing a new instance of [`LanguageModelSession`](languagemodelsession.md). For more information on managing the context window size, see [`TN3193: Managing the on-device foundation model’s context window`](https://developer.apple.com/documentation/Technotes/tn3193-managing-the-on-device-foundation-model-s-context-window).

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
- [PromptRepresentable](promptrepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [Prompting an on-device foundation model](prompting-an-on-device-foundation-model.md)
  Tailor your prompts to get effective results from an on-device model.
- [Analyzing the runtime performance of your Foundation Models app](analyzing-the-runtime-performance-of-your-foundation-models-app.md)
  Optimize token consumption and improve response times by profiling your app’s model usage with Instruments.
- [class LanguageModelSession](languagemodelsession.md)
  An object that represents a session that interacts with a language model.
- [struct Instructions](instructions.md)
  Details you provide that define the model’s intended behavior on prompts.
- [struct Transcript](transcript.md)
  A linear history of entries that reflect an interaction with a session.
- [struct GenerationOptions](generationoptions.md)
  Options that control how the model generates its response to a prompt.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/prompt)*