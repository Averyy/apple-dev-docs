# Instructions

**Framework**: Foundation Models  
**Kind**: struct

Details you provide that define the model’s intended behavior on prompts.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+
- watchOS 27.0+ (Beta)

## Declaration

```swift
struct Instructions
```

## Mentions

- [Improving the safety of generative model output](improving-the-safety-of-generative-model-output.md)
- [Composing dynamic sessions with instructions and profiles](composing-dynamic-sessions-with-instructions-and-profiles.md)
- [Generating content and performing tasks with Foundation Models](generating-content-and-performing-tasks-with-foundation-models.md)
- [Prompting an on-device foundation model](prompting-an-on-device-foundation-model.md)
- [Running a Core AI model in a Foundation Models session](running-a-core-ai-model-in-a-foundation-models-session.md)
- [Supporting languages and locales with Foundation Models](supporting-languages-and-locales-with-foundation-models.md)

#### Overview

You typically provide instructions to define the role and behavior of the model. In the code below, the instructions specify that the model replies with topics rather than, for example, a recipe:

```swift
let instructions = """
    Suggest related topics. Keep them concise (three to seven words) and make sure they \
    build naturally from the person's topic.
    """

let session = LanguageModelSession(instructions: instructions)

let prompt = "Making homemade bread"
let response = try await session.respond(to: prompt)
```

Don’t include untrusted content in instructions: the model is typically trained to obey instructions over any commands it receives in prompts. For more on how instructions impact generation quality and safety, see [`Improving the safety of generative model output`](improving-the-safety-of-generative-model-output.md).

All input to the model contributes tokens to the context window of the [`LanguageModelSession`](languagemodelsession.md) — including the [`Instructions`](instructions.md), [`Prompt`](prompt.md), [`Tool`](tool.md), and [`Generable`](generable.md) types, and the model’s responses. If your session exceeds the available context size, it throws  [`LanguageModelError.contextSizeExceeded(_:)`](languagemodelerror/contextsizeexceeded(_:).md).

Instructions can consume a lot of tokens that contribute to the context window size. To reduce your instruction size:

- Write shorter instructions to save tokens.
- Provide only the information necessary to perform the task.
- Use concise and imperative language instead of indirect or jargon that the model might misinterpret.
- Aim for one to three paragraphs instead of including a significant amount of background information, policy, or extra content.

For more information on managing the context window size, see [`Managing the context window`](managing-the-context-window.md).

## Topics

### Creating instructions
- [init(_:)](instructions/init(_:).md)
- [struct InstructionsBuilder](instructionsbuilder.md)
  A type that represents an instructions builder.
- [protocol InstructionsRepresentable](instructionsrepresentable.md)
  A type that can be represented as instructions.

## Relationships

### Conforms To
- [Copyable](../swift/copyable.md)
- [DynamicInstructions](dynamicinstructions.md)
- [Escapable](../swift/escapable.md)
- [InstructionsRepresentable](instructionsrepresentable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [Prompting an on-device foundation model](prompting-an-on-device-foundation-model.md)
  Tailor your prompts to get effective results from an on-device model.
- [Managing the context window](managing-the-context-window.md)
  Optimize your app’s token usage when prompting a model with the Foundation Models framework.
- [Updating prompts for new model versions](updating-prompts-for-new-model-versions.md)
  Manage the prompts your app uses by versioning them to make the most out of model improvements.
- [class LanguageModelSession](languagemodelsession.md)
  An object that represents a session that interacts with a language model.
- [struct Prompt](prompt.md)
  A prompt from a person to the model.
- [struct GenerationOptions](generationoptions.md)
  Options that control how the model generates its response to a prompt.
- [struct ContextOptions](contextoptions.md)
  Options that configure details that should appear in the prompt.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/instructions)*