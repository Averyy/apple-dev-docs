# init(id:toolName:segments:)

**Framework**: Foundation Models  
**Kind**: init

Creates a tool output that provides the result of a tool call back to the model.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+
- watchOS 27.0+

## Declaration

```swift
init(id: String, toolName: String, segments: [Transcript.Segment])
```

## Parameters

- `id`: A unique identifier for the tool output.
- `toolName`: The name of the tool that produced the output.
- `segments`: The segments that make up the output.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/transcript/tooloutput/init(id:toolname:segments:))*