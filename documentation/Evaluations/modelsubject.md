# ModelSubject

**Framework**: Evaluations  
**Kind**: struct  
**Role**: Structure

The subject type for language model evaluations.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+
- watchOS 27.0+
- Xcode 27.0+

## Declaration

```swift
struct ModelSubject<Value> where Value : Decodable, Value : Encodable, Value : Sendable
```

## Mentions

- [Evaluating language model responses](./evaluating-language-model-responses.md)

## Overview

Carries the value the model produces and an optional structured transcript. The transcript is required for tool-call evaluation. [`ToolCallEvaluator`](./toolcallevaluator.md) performs a runtime check and throws [`EvaluationError.missingTranscript(evaluatorType:)`](./evaluationerror/missingtranscript%28evaluatortype%29.md) if the transcript is `nil`.

```swift
let subject = ModelSubject(value: "Paris, France")
```

## Topics

### Creating a subject
- [init(value: Value, transcript: StructuredTranscript?)](./modelsubject/init%28value,transcript%29.md)
  Creates a model subject with a value and optional transcript.
### Accessing the content
- [var value: Value](./modelsubject/value.md)
  The typed value the model produces.
- [var transcript: StructuredTranscript?](./modelsubject/transcript.md)
  The structured transcript from the model session.
### Inspecting tool calls
- [var toolCalls: [Transcript.ToolCall]](./modelsubject/toolcalls.md)
  The tool calls from the transcript, or an empty array if no transcript was provided.
- [struct StructuredTranscript](./structuredtranscript.md)

## Relationships

### Conforms To
- [EvaluationSubject](./evaluationsubject.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Testing an intelligent feature
- [associatedtype Subject : EvaluationSubject](./evaluation/subject.md)
  The type of subject the system under test produces.
- [func subject(from: Self.Sample) async throws -> Self.Subject](./evaluation/subject%28from%29.md)
  Produces the subject of evaluation from a given sample.
- [protocol EvaluationSubject](./evaluationsubject.md)
  A type that represents the output the system under test produces.
- [var name: String](./evaluation/name.md)
  The evaluation’s name in results. Defaults to the type name; override for a custom one.


---

*[View on Apple Developer](https://developer.apple.com/documentation/evaluations/modelsubject)*