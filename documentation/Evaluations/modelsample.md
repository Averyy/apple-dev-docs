# ModelSample

**Framework**: Evaluations  
**Kind**: struct

A general-purpose language model evaluation sample.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
struct ModelSample<ExpectedValue> where ExpectedValue : Decodable, ExpectedValue : Encodable, ExpectedValue : Sendable
```

## Mentions

- [Generating synthetic datasets](generating-synthetic-evaluation-datasets.md)

#### Overview

Accepts string-based prompts and instructions. For multimodal prompts, create a custom [`ModelSampleProtocol`](modelsampleprotocol.md) conformance or use the [`init(input:expected:expectations:)`](modelsample/init(input:expected:expectations:).md) initializer with a prebuilt [`ModelSampleInput`](modelsampleinput.md).

```swift
let sample = ModelSample(prompt: "The capital of France is...", expected: "Paris.")
```

## Topics

### Creating a sample
- [init(prompt: String, expected: ExpectedValue?, instructions: String?, generationSchema: GenerationSchema?, expectations: TrajectoryExpectation?)](modelsample/init(prompt:expected:instructions:generationschema:expectations:)-7daed.md)
  Creates a model sample with string-based prompt and instructions.
- [init(prompt: Prompt, expected: ExpectedValue?, instructions: Instructions?, generationSchema: GenerationSchema?, expectations: TrajectoryExpectation?)](modelsample/init(prompt:expected:instructions:generationschema:expectations:)-8mni.md)
  Creates a model sample with a FoundationModels prompt.
- [init(input: ModelSampleInput, expected: ExpectedValue?, expectations: TrajectoryExpectation?)](modelsample/init(input:expected:expectations:).md)
  Creates a model sample with a prebuilt input.
### Specifying the query
- [var prompt: Prompt](modelsample/prompt.md)
  The user’s prompt for this sample.
- [var promptDescription: String](modelsample/promptdescription.md)
  A text representation of the prompt, synthesized from its segments.
- [var instructions: Instructions?](modelsample/instructions.md)
  Optional instructions providing context to the model for this sample.
- [var instructionsDescription: String?](modelsample/instructionsdescription.md)
  A text representation of the instructions, synthesized from their segments.
- [var input: ModelSampleInput](modelsample/input.md)
  The bundled language model input (prompt, instructions, schema).
### Specifying expected output
- [var expected: ExpectedValue?](modelsample/expected.md)
  The expected output for comparison.
- [var output: ModelSampleOutput<ExpectedValue, TrajectoryExpectation>](modelsample/output.md)
  The expected output value and evaluation expectations.
### Specifying tool expectations
- [var expectations: TrajectoryExpectation?](modelsample/expectations.md)
  The expected pattern of tool calls for this sample.
### Configuring generation
- [var generationSchema: GenerationSchema?](modelsample/generationschema.md)
  The output schema for the model’s response.
### Bundled input and output
- [struct ModelSampleInput](modelsampleinput.md)
  The data sent to a language model for evaluation.
- [struct ModelSampleOutput](modelsampleoutput.md)
  The expected output value and evaluation expectations for a sample.
### Protocols
- [protocol ModelSampleProtocol](modelsampleprotocol.md)
  A type that defines language model evaluation samples with prompt, instructions, and expectations.
- [protocol SampleProtocol](sampleprotocol.md)
  A type that defines evaluation samples.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Escapable](../Swift/Escapable.md)
- [ModelSampleProtocol](modelsampleprotocol.md)
- [SampleProtocol](sampleprotocol.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [Generating synthetic datasets](generating-synthetic-evaluation-datasets.md)
  Expand a small set of manually written evaluation samples into a larger dataset.
- [Designing datasets to test your feature](designing-evaluation-datasets.md)
  Build categorized test datasets that reflect the full range of real-world use of your feature.
- [protocol Loader](loader.md)
  A protocol for types that supply a dataset for evaluation.
- [actor SampleGenerator](samplegenerator.md)
  An actor that generates evaluation samples using a language model.


---

*[View on Apple Developer](https://developer.apple.com/documentation/evaluations/modelsample)*