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

## Declaration

```swift
struct Instructions
```

## Mentions

- [Generating content and performing tasks with Foundation Models](generating-content-and-performing-tasks-with-foundation-models.md)
- [Improving the safety of generative model output](improving-the-safety-of-generative-model-output.md)
- [Prompting an on-device foundation model](prompting-an-on-device-foundation-model.md)
- [Supporting languages and locales with Foundation Models](supporting-languages-and-locales-with-foundation-models.md)

#### Overview

Instructions are typically provided by you to define the role and behavior of the model. In the code below, the instructions specify that the model replies with topics rather than, for example, a recipe:

```swift
let instructions = """
    Suggest related topics. Keep them concise (three to seven words) and make sure they \
    build naturally from the person's topic.
    """

let session = LanguageModelSession(instructions: instructions)

let prompt = "Making homemade bread"
let response = try await session.respond(to: prompt)
```

Apple trains the model to obey instructions over any commands it receives in prompts, so don’t include untrusted content in instructions. For more on how instructions impact generation quality and safety, see [`Improving the safety of generative model output`](improving-the-safety-of-generative-model-output.md).

All input to the model contributes tokens to the context window of the [`LanguageModelSession`](languagemodelsession.md) — including the [`Instructions`](instructions.md), [`Prompt`](prompt.md), [`Tool`](tool.md), and [`Generable`](generable.md) types, and the model’s responses. If your session exceeds the available context size, it throws [`LanguageModelSession.GenerationError.exceededContextWindowSize(_:)`](languagemodelsession/generationerror/exceededcontextwindowsize(_:).md).

Instructions can consume a lot of tokens that contribute to the context window size. To reduce your instruction size:

- Write shorter instructions to save tokens.
- Provide only the information necessary to perform the task.
- Use concise and imperative language instead of indirect or jargon that the model might misinterpret.
- Aim for one to three paragraphs instead of including a significant amount of background information, policy, or extra content.

For more information on managing the context window size, see [`TN3193: Managing the on-device foundation model’s context window`](https://developer.apple.com/documentation/Technotes/tn3193-managing-the-on-device-foundation-model-s-context-window).

## Topics

### Creating instructions
- [init(_:)](instructions/init(_:).md)
- [struct InstructionsBuilder](instructionsbuilder.md)
  A type that represents an instructions builder.
- [protocol InstructionsRepresentable](instructionsrepresentable.md)
  A type that can be represented as instructions.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [InstructionsRepresentable](instructionsrepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [Prompting an on-device foundation model](prompting-an-on-device-foundation-model.md)
  Tailor your prompts to get effective results from an on-device model.
- [Analyzing the runtime performance of your Foundation Models app](analyzing-the-runtime-performance-of-your-foundation-models-app.md)
  Optimize token consumption and improve response times by profiling your app’s model usage with Instruments.
- [class LanguageModelSession](languagemodelsession.md)
  An object that represents a session that interacts with a language model.
- [struct Prompt](prompt.md)
  A prompt from a person to the model.
- [struct Transcript](transcript.md)
  A linear history of entries that reflect an interaction with a session.
- [struct GenerationOptions](generationoptions.md)
  Options that control how the model generates its response to a prompt.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/instructions)*