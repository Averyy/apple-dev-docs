# toolCalls

**Framework**: Evaluations  
**Kind**: property  
**Role**: Instance Property

The tool calls from the transcript, or an empty array if no transcript was provided.

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
var toolCalls: [Transcript.ToolCall] { get }
```

Available when `Value` conforms to `Decodable`, `Encodable`, and `Sendable`.

## See Also

### Inspecting tool calls
- [struct StructuredTranscript](../structuredtranscript.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/evaluations/modelsubject/toolcalls)*