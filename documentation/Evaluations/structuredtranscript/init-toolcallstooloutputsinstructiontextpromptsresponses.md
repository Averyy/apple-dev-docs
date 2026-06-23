# init(toolCalls:toolOutputs:instructionText:prompts:responses:)

**Framework**: Evaluations  
**Kind**: init

Creates a structured transcript.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
init(toolCalls: [Transcript.ToolCall] = [], toolOutputs: [Transcript.ToolOutput] = [], instructionText: String = "", prompts: [String] = [], responses: [Transcript.Response] = [])
```

## Parameters

- `toolCalls`: The tool calls from the session.
- `toolOutputs`: The tool outputs from the session.
- `instructionText`: The system instructions text.
- `prompts`: The user prompts.
- `responses`: The model responses.


---

*[View on Apple Developer](https://developer.apple.com/documentation/evaluations/structuredtranscript/init(toolcalls:tooloutputs:instructiontext:prompts:responses:))*