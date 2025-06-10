# init(id:segments:toolDefinitions:)

**Framework**: Foundation Models  
**Kind**: init

Initialize instructions by describing how you want the model to behave using natural language.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
init(id: String = UUID().uuidString, segments: [Transcript.Segment], toolDefinitions: [Transcript.ToolDefinition])
```

## Parameters

- `id`: A unique identifier for this instructions segment.
- `segments`: An array of segments that make up the instructions.
- `toolDefinitions`: Tools that the model should be allowed to call.

## See Also

- [init(from: any Decoder) throws](transcript/init(from:).md)
  Creates a new instance by decoding from the given decoder.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/transcript/instructions/init(id:segments:tooldefinitions:))*