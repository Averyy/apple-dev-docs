# init(id:segments:toolDefinitions:)

**Framework**: Foundation Models  
**Kind**: init

Initialize instructions by describing how you want the model to behave using natural language.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
init(id: String = UUID().uuidString, segments: [Transcript.Segment], toolDefinitions: [Transcript.ToolDefinition])
```

## Parameters

- `id`: A unique identifier for this instructions segment.
- `segments`: An array of segments that make up the instructions.
- `toolDefinitions`: Tools that the model should be allowed to call.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/transcript/instructions/init(id:segments:tooldefinitions:))*