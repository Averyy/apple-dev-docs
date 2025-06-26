# Instructions

**Framework**: Foundation Models  
**Kind**: struct

Instructions define the model’s intended behavior on prompts.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
struct Instructions
```

## Mentions

- [Improving safety from generative model output](improving-safety-from-generative-model-output.md)
- [Generating content and performing tasks with Foundation Models](generating-content-and-performing-tasks-with-foundation-models.md)

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

Apple trains the model to obey instructions over any commands it receives in prompts, so don’t include untrusted content in instructions. For more on how instructions impact generation quality and safety, see [`Improving safety from generative model output`](improving-safety-from-generative-model-output.md).

## Topics

### Creating instructions
- [init(_:)](instructions/init(_:).md)
- [struct InstructionsBuilder](instructionsbuilder.md)
  A type that represents an instructions builder.
- [protocol InstructionsRepresentable](instructionsrepresentable.md)
  Conforming types represent instructions.
### Default Implementations
- [InstructionsRepresentable Implementations](instructions/instructionsrepresentable-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [InstructionsRepresentable](instructionsrepresentable.md)

## See Also

- [class LanguageModelSession](languagemodelsession.md)
  An object that represents a session that interacts with a large language model.
- [struct Prompt](prompt.md)
  A prompt from a person to the model.
- [struct Transcript](transcript.md)
  A transcript that documents interactions with a language model. Transcripts contain an ordered list of entries, representing inputs to and outputs from the model.
- [struct GenerationOptions](generationoptions.md)
  Options that control how the model generates its response to a prompt.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/instructions)*