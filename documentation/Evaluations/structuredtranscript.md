# StructuredTranscript

**Framework**: Evaluations  
**Kind**: struct

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)
- Xcode 27.0+ (Beta)

## Declaration

```swift
struct StructuredTranscript
```

## Topics

### Creating a transcript
- [init(toolCalls: [Transcript.ToolCall], toolOutputs: [Transcript.ToolOutput], instructionText: String, prompts: [String], responses: [Transcript.Response])](structuredtranscript/init(toolcalls:tooloutputs:instructiontext:prompts:responses:).md)
  Creates a structured transcript.
### Inspecting prompts and responses
- [var instructionText: String](structuredtranscript/instructiontext.md)
  The system instruction text from the transcript.
- [var prompts: [String]](structuredtranscript/prompts.md)
  The user prompt strings from the transcript.
- [var responses: [Transcript.Response]](structuredtranscript/responses.md)
  The model responses from the transcript.
### Inspecting tool interactions
- [var toolCalls: [Transcript.ToolCall]](structuredtranscript/toolcalls.md)
  The tool calls extracted from the transcript.
- [var toolOutputs: [Transcript.ToolOutput]](structuredtranscript/tooloutputs.md)
  The tool outputs extracted from the transcript.
- [enum StructuredValue](structuredvalue.md)
  A type-safe representation of JSON values.

## Relationships

### Conforms To
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [var toolCalls: [Transcript.ToolCall]](modelsubject/toolcalls.md)
  The tool calls from the transcript, or an empty array if no transcript was provided.


---

*[View on Apple Developer](https://developer.apple.com/documentation/evaluations/structuredtranscript)*