# init(toolCalls:toolOutputs:instructionText:prompts:responses:)

**Framework**: Evaluations  
**Kind**: init

Creates a structured transcript.

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