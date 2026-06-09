# ModelSubject

**Framework**: Evaluations  
**Kind**: struct

The subject type for language model evaluations.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
struct ModelSubject<Value> where Value : Decodable, Value : Encodable, Value : Sendable
```

## Mentions

- [Evaluating language model responses](evaluating-language-model-responses.md)

#### Overview

Carries the model’s produced value and an optional structured transcript. The transcript is required for tool-call evaluation. [`ToolCallEvaluator`](toolcallevaluator.md) performs a runtime check and throws [`EvaluationError.missingTranscript(evaluatorType:)`](evaluationerror/missingtranscript(evaluatortype:).md) if the transcript is `nil`.

```swift
let subject = ModelSubject(value: "Paris, France")
```

## Topics

### Creating a subject
- [init(value: Value, transcript: StructuredTranscript?)](modelsubject/init(value:transcript:).md)
  Creates a model subject with a value and optional transcript.
### Accessing the content
- [var value: Value](modelsubject/value.md)
  The typed value produced by the model.
- [var transcript: StructuredTranscript?](modelsubject/transcript.md)
  The structured transcript from the model session.
### Inspecting tool calls
- [var toolCalls: [Transcript.ToolCall]](modelsubject/toolcalls.md)
  The tool calls from the transcript, or an empty array if no transcript was provided.
- [struct StructuredTranscript](structuredtranscript.md)

## Relationships

### Conforms To
- [EvaluationSubject](evaluationsubject.md)

## See Also

- [associatedtype Subject : EvaluationSubject](evaluation/subject.md)
  The type of the subject produced by the system under test.
- [func subject(from: Self.Sample) async throws -> Self.Subject](evaluation/subject(from:).md)
  Produces the subject of evaluation from a given sample.
- [protocol EvaluationSubject](evaluationsubject.md)
  A type that represents the output produced by the system under test.
- [var name: String](evaluation/name.md)
  The default name, derived from the type name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/evaluations/modelsubject)*